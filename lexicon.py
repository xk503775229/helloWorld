#coding=utf8
import time
import Data
import FM


def read_file(f):
    f_list = []
    for line in f:
        line = line.strip()
        f_list.append(line)
    return f_list


def load_6type():
    '''
    :return: 多用途情感词表
    '''
    fp_sa = open(r'E:\restaurant\lexicon\6type\pos_sa.txt', 'rb')
    fp_eva = open(r'E:\restaurant\lexicon\6type\pos_eva.txt', 'rb')
    fn_sa = open(r'E:\restaurant\lexicon\6type\neg_sa.txt', 'rb')
    fn_eva = open(r'E:\restaurant\lexicon\6type\neg_eva.txt', 'rb')
    pos_sa = read_file(fp_sa)
    pos_eva = read_file(fp_eva)
    neg_sa = read_file(fn_sa)
    neg_eva = read_file(fn_eva)
    pos_list = pos_eva + pos_sa
    neg_list = neg_eva + neg_sa
    return pos_list, neg_list


def load_lexicon_ntusd():
    '''
    :return: ntusd情感词表
    '''
    fn = open('lexicon/ntusd/ntusd-negative.txt')
    fp = open('lexicon/ntusd/ntusd-positive.txt')
    SA_neg = read_file(fn)
    SA_pos = read_file(fp)
    return SA_pos, SA_neg


def load_lexicon_weibo():
    '''
    :return: 微博情感词典
    '''
    f = open('lexicon/weibo.txt', 'rb')
    weibo = {}
    for line in f:
        line = line.strip().split()
        weibo[line[0]] = line[1]
    return weibo


def load_lexicon_not():
    '''
    :return: 否定词表
    '''
    f = open(r'lexicon\not', 'rb')
    SA_not = read_file(f)
    return SA_not


def classify(sentence, pos_list, neg_list):
    count_pos = 0
    count_neg = 0
    for word in sentence:
        if word in pos_list:
            count_pos += 1
        if word in neg_list:
            count_neg += 1
    if count_pos > count_neg:
        return 1
    elif count_pos<count_neg:
        return 0
    else:
        return -1


def test(test_set, pos_list, neg_list):
    time1 = time.clock()
    test_class = []
    for sentence in test_set:
        test_class.append(classify(sentence, pos_list, neg_list))
    time2 = time.clock()
    print 'time cost:%fs' % (time2 - time1)
    return test_class


def error_analysis(not_class, test_set):
    j = 0
    for i in range(len(test_set)):
        if i == not_class[j]:
            j += 1
            print test_set[i]


if __name__ == '__main__':
    time1 = time.clock()
    pos_test , neg_test  = Data.load_test()
    test_set, test_class = Data.two_to_one(pos_test, neg_test)
    pos_list, neg_list = load_6type()
    real_class = test(test_set, pos_list, neg_list)
    not_class = FM.f_measure(real_class, test_class)
    error_analysis(not_class, test_set)