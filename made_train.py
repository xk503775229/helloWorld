#coding=utf8
'''
构造pos、neg和neu语料
'''
f  = open(r'F:\Corpus_Set\restaurant\review2id.txt', 'rb')
# fp = open(r'F:\Corpus_Set\restaurant\pos\pos.txt', 'wb')
# fn = open(r'F:\Corpus_Set\restaurant\neg\neg.txt', 'wb')
fu = open(r'F:\Corpus_Set\restaurant\neu\neu.txt', 'wb')
for line in f:
    line = line.strip().split('###')
    # if line[2] == '1':
    #     fn.write(line[-1] + '\n')
    # if line[2] == '5':
    #     fp.write(line[-1] + '\n')
    if line[2] == '3':
        fu.write(line[3] + '###' + line[-1] + '\n')

