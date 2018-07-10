#coding=utf8
import time
import numpy as np


class Documents:
    '''
    语料+极性
    '''
    def __init__(self, words, polarity):
        self.words    = words
        self.polarity = polarity


def load_train_2():
    '''
    训练集
    :return:
    '''
    time1 = time.clock()
    fp = open(r'home\qlu\Corpus_Set\restaurant\train\pos\pos.txt', 'rb')
    fn = open(r'home\qlu\Corpus_Set\restaurant\train\neg\neg.txt', 'rb')
    pos = []
    neg = []
    for line in fp:
        line = line.strip().split()
        pos.append(Documents(line, 1))
    for line in fn:
        line = line.strip().split()
        neg.append(Documents(line, 0))
    time2 = time.clock()
    print 'train cost:%fs' % (time2 - time1)
    return pos, neg




def load_train_3():
    N = 10
    time1 = time.clock()
    fp = open('F:/Corpus_Set/restaurant/train/pos/pos.txt', 'rb')
    fn = open('F:/Corpus_Set/restaurant/train/neg/neg.txt', 'rb')
    fu = open('F:/Corpus_Set/restaurant/train/neu/neu.txt', 'rb')
    pos = []
    neg = []
    neu = []
    count = 0
    for line in fp:
        count += 1
        if count > N:
            break
        line = line.strip().split()
        pos.append(Documents(line, 1))
    count = 0
    for line in fn:
        count += 1
        if count > N:
            break
        line = line.strip().split()
        neg.append(Documents(line, 0))
    count = 0
    for line in fu:
        count += 1
        if count > N:
            break
        line = line.strip().split()
        neu.append(Documents(line, 2))
    time2 = time.clock()
    print 'Load Train Cost:%fs' % (time2 - time1)
    return pos, neg, neu



def load_test():
    '''
    :return: 测试集
    '''
    fn = open('neg.txt', 'rb')
    fp = open('pos.txt', 'rb')
    pos = []
    neg = []
    for line in fn:
        line = line.strip().split('###')
        neg.append(Documents(line[-1].split(), 0))
    for line in fp:
        line = line.strip().split('###')
        pos.append(Documents(line[-1].split(), 1))
    return pos, neg


def load_test_3():
    '''
    :return: 测试集
    '''
    fn = open('neg.txt', 'rb')
    fp = open('pos.txt', 'rb')
    fu = open('neu.txt', 'rb')
    pos = []
    neg = []
    neu = []
    for line in fn:
        line = line.strip().split('###')
        neg.append(Documents(line[-1].split(), 0))
    for line in fp:
        line = line.strip().split('###')
        pos.append(Documents(line[-1].split(), 1))
    for line in fu:
        line = line.strip().split('###')
        neu.append(Documents(line[-1].split(), 2))
    return pos, neg, neu


def load_lexicon_not():
    '''
    :return: 否定词表
    '''
    f = open(r'lexicon\not', 'rb')
    SA_not = []
    for line in f:
        line = line.strip()
        SA_not.append(line)
    return SA_not


def create_vocab_2(pos, neg):
    '''
    创建词表
    :param pos :
    :param neg :
    :return    : 词表
    '''
    time1 = time.clock()
    my_vocab = {}
    i = 0
    for document in pos:
        for word in document.words:
            if word not in my_vocab:
                my_vocab[word] = i
                i += 1
    for document in neg:
        for word in document.words:
            if word not in my_vocab:
                my_vocab[word] = i
                i += 1
    time2 = time.clock()
    print 'create vocab cost:%fs' % (time2 - time1)
    return my_vocab


def create_vocab(train_set):
    time1 = time.clock()
    my_vocab = {}
    i = 0
    for sentence in train_set:
        for word in sentence:
            if word not in my_vocab:
                my_vocab[word] = i
                i += 1
    time2 = time.clock()
    print 'Create Vocab Cost:%fs' % (time2 - time1)
    return my_vocab


def create_vocab_3(pos, neg, neu):
    '''
    创建词表
    :param pos :
    :param neg :
    :return    : 词表
    '''
    time1 = time.clock()
    my_vocab = {}
    i = 0
    for document in pos:
        for word in document.words:
            if word not in my_vocab:
                my_vocab[word] = i
                i += 1
    for document in neg:
        for word in document.words:
            if word not in my_vocab:
                my_vocab[word] = i
                i += 1
    for document in neu:
        for word in document.words:
            if word not in my_vocab:
                my_vocab[word] = i
                i += 1
    time2 = time.clock()
    print 'Create Vocab Cost:%fs' % (time2 - time1)
    return my_vocab

def doc2VecMat(trains, vocabDict):
    '''
    将文本转为向量模型
    :param trains    : 语料
    :param vocabDict : 词向量
    :return          : 语料的向量模型
    '''
    time1 = time.clock()
    documentsLen = len(trains)
    vocabDictLen = len(vocabDict.keys())
    docMat       = [[0] * vocabDictLen] * documentsLen
    for i in range(documentsLen):
        wordsVec = [0] * vocabDictLen
        for word in trains[i] :
            if word in vocabDict :
                wordsVec[vocabDict[word]] = 1
        docMat[i] = wordsVec
    time2 = time.clock()
    print 'doc_mat cost:%fs' % (time2 - time1)
    return docMat


def two_to_one(pos, neg):
    '''
    :param pos :
    :param neg :
    :return    : 合并训练集_list_list
    '''
    time1 = time.clock()
    train_set = []
    train_class = []
    for sentence in pos:
        train_set.append(sentence.words)
        train_class.append(1)
    for sentence in neg:
        train_set.append(sentence.words)
        train_class.append(0)
    time2 = time.clock()
    print '合并训练集:%fs' % (time2 - time1)
    return train_set, train_class


def three_to_one(pos, neg, neu):
    set = []
    mark = []
    for sentence in pos:
        set.append(sentence.words)
        mark.append(1)
    for sentence in neg:
        set.append(sentence.words)
        mark.append(0)
    for sentence in neu:
        set.append(sentence.words)
        mark.append(2)
    return set, mark




# if __name__ == '__main__':
#     pos, neg = load_test()
#     # my_vocab = create_vocab(pos, neg)
#     SA_pos, SA_neg = load_lexicon()

