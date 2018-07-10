# coding=utf8
from __future__ import division
import numpy as np
import time


def classify_2(vector, p0, p1, pn):
    p1 = sum(vector * p1) + np.log(pn)
    p0 = sum(vector * p0) + np.log(1.0 - pn)
    if p1 > p0:
        return 1
    else:
        return 0


def classify_3(vector, px_0, px_1, px_2, p_neg, p_pos, p_neu):
    p0_x = sum(vector * px_0) + np.log(p_neg)
    p1_x = sum(vector * px_1) + np.log(p_pos)
    p2_x = sum(vector * px_2) + np.log(p_neu)
    if   p0_x > p1_x and p0_x > p2_x:
        return 0
    elif p1_x > p0_x and p1_x > p2_x:
        return 1
    else:
        return 2


def train_2(docMat, mark):
    time1      = time.clock()
    doc_num    = len(docMat)
    vec_num    = len(docMat[0])
    p_positive = sum(mark) / float(doc_num)
    p0_vector  = np.ones(vec_num)
    p1_vector  = np.ones(vec_num)
    p0_num     = 2.0
    p1_num     = 2.0
    for i in range(doc_num):
        if mark[i] == 1:
            p1_vector += docMat[i]
            p1_num    += sum(docMat[i])
        else:
            p0_vector += docMat[i]
            p0_num    += sum(docMat[i])
    p1_vector_matrix = np.log(p1_vector / p1_num)
    p0_vector_matrix = np.log(p0_vector / p0_num)
    time2            = time.clock()
    print '训练用时:%fs' % (time2 - time1)
    return p0_vector_matrix, p1_vector_matrix, p_positive


def train_3(docMat, mark):
    '''
    0:neg|1:pos|2:neu
    '''
    time1   = time.clock()
    doc_num = len(docMat)
    vec_num = len(docMat[0])
    p0_vec  = np.ones(vec_num)
    p1_vec  = np.ones(vec_num)
    p2_vec  = np.ones(vec_num)
    p0_num  = p1_num = p2_num = 2.0
    count0  = count1 = count2 = 0.0
    for i in range(doc_num):
        if  mark[i]  == 0:
            p0_vec   += docMat[i]
            p0_num   += sum(docMat[i])
            count0   += 1.0
        elif mark[i] == 1:
            p1_vec   += docMat[i]
            p1_num   += sum(docMat[i])
            count1   += 1.0
        else:
            p2_vec += docMat[i]
            p2_num += sum(docMat[i])
            count2 += 1.0
    px_0  = np.log(p0_vec / p0_num)
    px_1  = np.log(p1_vec / p1_num)
    px_2  = np.log(p2_vec / p2_num)
    p_neg = count0 / doc_num
    p_pos = count1 / doc_num
    p_neu = count2 / doc_num
    time2 = time.clock()
    print 'Train cost:%fs' % (time2 - time1)
    print p0_vec,'\n',p1_vec,'\n',p2_vec,'\n'
    print p0_num,'\n',p1_num,'\n',p2_num
    print '##################################'
    print px_0,'\n',px_1
    print '#################################'
    return px_0, px_1, px_2, p_neg, p_pos, p_neu


def test_2(train_set, train_class, test_set):
    time1 = time.clock()
    p0v, p1v, p_n = train_2(train_set, train_class)
    real_class    = []
    for word in test_set:
        real_class.append(classify_2(np.array(word), p0v, p1v, p_n))
    time2 = time.clock()
    print 'test cost:%fs' % (time2 - time1)
    return real_class


def test_3(train_set, train_class, test_set):
    time1      = time.clock()
    real_class = []
    px_0, px_1, px_2, p_neg, p_pos, p_neu = train_3(train_set, train_class)
    for word in test_set:
        real_class.append(classify_3(np.array(word),px_0, px_1, px_2, p_neg, p_pos, p_neu))
    time2 = time.clock()
    print 'Test Cost:%fs' % (time2 - time1)
    return real_class
