#coding=utf8
import time
import Data
import FM
import Bayes
import term_select
time1 = time.clock()
# SA_pos, SA_neg       = Data.load_lexicon_ntusd()
# SA_not               = Data.load_lexicon_not()
pos_test , neg_test, neu_test   = Data.load_test_3()
test_set, test_class            = Data.three_to_one(pos_test , neg_test, neu_test)
pos_train, neg_train, neu_train = Data.load_train_3()
train_set, train_class          = Data.three_to_one(pos_train, neg_train, neu_train)
my_vocab                        = Data.create_vocab(train_set)
my_vocab                        = term_select.TF(train_set, list(my_vocab))
print len(my_vocab)
for i in my_vocab:
    print i
my_vocab                        = dict([(word, i) for i, word in enumerate(my_vocab)])
# train, train_class = Data.two_to_one(pos_train, neg_train)
# test, test_class   = Data.two_to_one(pos_test , neg_test)

train_mat = Data.doc2VecMat(train_set, my_vocab)
test_mat  = Data.doc2VecMat(test_set , my_vocab)
# print type(Bayes.train_f(train_mat, train_class)[1])

real_class = Bayes.test_3(train_mat, train_class, test_mat)
FM.f_measure(real_class, test_class)
time2 = time.clock()
print '总计耗时:%fs' % (time2 - time1)













##########################################################
# count_pos = 0
# count_neg = 0
# count_no = 0
# real_class_pos = []
# real_class_neg = []
# data_class_pos = []
# data_class_neg = []
# for sentence in pos:
#     count_pos = 0
#     count_neg = 0
#     data_class_pos.append(sentence.polarity)
#     for word in sentence.words:
#         if word in SA_no:
#             count_no += 1
#         if word in SA_pos:
#             count_pos += 1
#         if word in SA_neg:
#             count_neg += 1
#     if count_pos > count_neg:
#         real_class_pos.append(1)
#     elif count_pos < count_neg:
#         real_class_pos.append(0)
#     else:
#         real_class_pos.append(-1)
# for sentence in neg:
#     count_pos = 0
#     count_neg = 0
#     data_class_neg.append(sentence.polarity)
#     for word in sentence.words:
#         if word in SA_no:
#             count_no += 1
#         if word in SA_pos:
#             count_pos += 1
#         if word in SA_neg:
#             count_neg += 1
#     if count_pos > count_neg:
#         real_class_neg.append(1)
#     elif count_pos < count_neg:
#         real_class_neg.append(0)
#     else:
#         real_class_neg.append(-1)
# print real_class_pos
# FM.test(pos,real_class_pos,data_class_pos)
###########################################################

# weibo = Data.load_lexicon_weibo()
# score = 0.0
# real_class_pos = []
# real_class_neg = []
# data_class_pos = []
# data_class_neg = []
# for sentence in pos:
#     score = 0.0
#     count_not = 1
#     data_class_pos.append(sentence.polarity)
#     for word in sentence.words:
#         # if word in SA_not:
#         #     count_not *= -1
#         if word in weibo and word not in SA_not:
#             score += float(weibo[word])
#     score *= count_not
#     if score > 0:
#         real_class_pos.append(1)
#     elif score < 0:
#         real_class_pos.append(0)
#     else:
#         real_class_pos.append(-1)
#
# for sentence in neg:
#     score = 0.0
#     count_not = 1
#     data_class_neg.append(sentence.polarity)
#     for word in sentence.words:
#         # if word in SA_not:
#         #     count_not *= -1
#         # elif word in weibo:
#         if word in weibo:
#             score += float(weibo[word])
#     score = score * count_not
#
#     if score > 0.0:
#         real_class_neg.append(1)
#     elif score < 0.0:
#         real_class_neg.append(0)
#     else:
#         real_class_neg.append(-1)
#
# # FM.test(pos, real_class_pos, data_class_pos)
# FM.test(neg, real_class_neg, data_class_neg)
