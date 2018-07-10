#coding=utf8
'''
用5、1、3三种极性构造训练集pos、neg和neu
长度各10w，保存在train文件夹中

原始长度：
# pos:679707
# neg:153347
# neu:985676
'''
import random
fp_train = open(r'F:\Corpus_Set\restaurant\train\pos\pos.txt', 'wb')
fn_train = open(r'F:\Corpus_Set\restaurant\train\neg\neg.txt', 'wb')
fu_train = open(r'F:\Corpus_Set\restaurant\train\neu\neu.txt', 'wb')

fp_data = open(r'F:\Corpus_Set\restaurant\pos\pos.txt', 'rb')
fn_data = open(r'F:\Corpus_Set\restaurant\neg\neg.txt', 'rb')
fu_data = open(r'F:\Corpus_Set\restaurant\neu\neu.txt', 'rb')

# count = 0
# for line in fp_data:
#     count += 1
# print count
# count = 0
# for line in fn_data:
#     count += 1
# print count
# count = 0
# for line in fu_data:
#     count += 1
# print count


neg_list = random.sample(range(153347), 100000)
pos_list = random.sample(range(679707), 100000)
neu_list = random.sample(range(985676), 100000)
neg_list.sort()
pos_list.sort()
neu_list.sort()
neg_dict = dict([(word, i) for i, word in enumerate(neg_list)])
pos_dict = dict([(word, i) for i, word in enumerate(pos_list)])
neu_dict = dict([(word, i) for i, word in enumerate(neu_list)])



for i in range(679707):
    line = fp_data.readline()
    if i in pos_dict:
        fp_train.write(line)

for i in range(153347):
    line = fn_data.readline()
    if i in neg_dict:
        fn_train.write(line)

for i in range(985676):
    line = fu_data.readline()
    if i in neu_dict:
        fu_train.write(line)
