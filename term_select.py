# coding=utf8
import time
def TF_2(pos, neg, vocabList):
    '''
    去掉词频小于3的词
    :param pos       :
    :param neg       :
    :param vocabList : 原始词表
    :return          :
    '''
    time1 = time.clock()
    vocabDict = dict([(word, 0) for i, word in enumerate(vocabList)])
    my_vocab = []
    for sentence in pos:
        for word in sentence.words:
            if word in vocabDict:
                vocabDict[word] += 1
    for sentence in neg:
        for word in sentence.words:
            if word in vocabDict:
                vocabDict[word] += 1
    for word in vocabDict:
        if vocabDict[word] >= 3:
            my_vocab.append(word)
    time2 = time.clock()
    print 'TF cost:%fs' % (time2 - time1)
    return my_vocab

def TF(train_set, vocabList):
    time1 = time.clock()
    vocabDict = dict([(word, 0) for i, word in enumerate(vocabList)])
    my_vocab = []
    for sentence in train_set:
        for word in sentence:
            if word in vocabDict:
                vocabDict[word] += 1
    for word in vocabDict:
        if vocabDict[word] >= 10:
            my_vocab.append(word)
    time2 = time.clock()
    print 'TF Cost:%fs' % (time2 - time1)
    return my_vocab
