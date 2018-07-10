#coding=utf8
import lexicon

pos_list, neg_list = lexicon.load_6type()
pos_dict = dict([(word, i) for i, word in enumerate(pos_list)])
neg_dict = dict([(word, i) for i, word in enumerate(neg_list)])
fu = open(r'F:\Corpus_Set\restaurant\test\neu.txt', 'rb')
fu_new = open(r'F:\Corpus_Set\restaurant\test\neu_new.txt', 'wb')
for line in fu:
    s = 1
    sentence = line.strip().split('###')[-1].split()
    for word in sentence:
        if word in pos_dict or word in neg_dict:
            s = 0
            break
    if s == 1:
        fu_new.write(line)