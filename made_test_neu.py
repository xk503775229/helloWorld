import random
# 3119222

fu_data = open(r'F:\Corpus_Set\restaurant\test\neu_new.txt', 'rb')
fu_train = open(r'F:\Corpus_Set\restaurant\test\neu_end.txt', 'wb')

# for line in fu_data:
#     count += 1
# print count

neu_list = random.sample(range(3119222), 2000)
neu_list.sort()

neu_dict = dict([(word, i) for i, word in enumerate(neu_list)])




for i in range(3119222):
    line = fu_data.readline()
    if i in neu_dict:
        fu_train.write(line)
