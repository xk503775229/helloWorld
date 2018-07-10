# coding=utf8
from __future__ import division

# def f_measure(real_class, test_class):
#     print '#############################'
#     n       = len(real_class)
#     error = 0
#     for i in range(n):
#         if real_class[i] != test_class[i]:
#             error += 1
#     print 'right rate:%f' % (error / n)


def f_measure(real_class, test_class):
    '''
    :param real_class: 测试结果
    :param test_class: 正确结果
    :return          : 分析结果
    '''
    print '#############################'
    right_1 = 0
    right_0 = 0
    right_2 = 0
    count_1 = 0
    count_0 = 0
    count_2 = 0
    count_neg = 0
    count_pos = 0
    count_neu = 0
    n       = len(real_class)
    for i in range(n):
        if test_class[i] == 0:
            count_neg += 1
        elif test_class[i] == 1:
            count_pos += 1
        else:
            count_neu += 1
    for i in range(n):
        if real_class[i] == 1:
            count_1 += 1
            if test_class[i] == 1:
                right_1 += 1
        elif real_class[i] == 0:
            count_0 += 1
            if test_class[i] == 0:
                right_0 += 1
        else:
            count_2 += 1
            if test_class[i] == 2:
                right_2 += 1
    right_rate_0  = right_0 / count_0
    recall_rate_0 = right_0 / count_neg
    right_rate_1  = right_1 / count_1
    recall_rate_1 = right_1 / count_pos
    right_rate_2  = right_2 / count_2
    recall_rate_2 = right_2 / count_neu
    print 'positive precision  :%f' % right_rate_1,\
    '\n', 'positive recall rate:%f' % recall_rate_1,\
    '\n', 'positive F-measure  :%f' % ((right_rate_1 * recall_rate_1 * 2) / (right_rate_1 + recall_rate_1)),\
    '\n', 'negative precision  :%f' % right_rate_0,\
    '\n', 'negative recall rate:%f' % recall_rate_0,\
    '\n', 'negative F-measure  :%f' % ((right_rate_0 * recall_rate_0 * 2) / (right_rate_0 + recall_rate_0)),\
    '\n', 'neutral  precision  :%f' % right_rate_2,\
    '\n', 'neutral  recall rate:%f' % recall_rate_2,\
    '\n', 'neutral  F-measure  :%f' % ((right_rate_2 * recall_rate_2 * 2) / (right_rate_2 + recall_rate_2)),\
    '\n', 'right rate          :%f' % ((right_1 + right_0 + right_2) / n)