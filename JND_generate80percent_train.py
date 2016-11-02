import os
import random
import sys
import numpy as np
import re

def write2File(data,fileName):
    fp = open(fileName,'w+')
    for item in data :
        fp.write("{name} {label}\n".format(name=item[0],label=item[1]))
    fp.close()
    print 'write',fileName,' OK'

prefix = '/home/zlx/workspace/IQA_CNN/image_data/MCL-JCI/distored_image_crop/'

jnd = range(1,51)
random.shuffle(jnd)

jnd_shuffle_train = jnd[:40]
jnd_shuffle_test = jnd[40:]

print jnd_shuffle_train,jnd_shuffle_test
data = np.loadtxt('JND_label_crop.txt',dtype=np.str)
train_data  = []
test_data  = []
for item in data:
    #print item,item[0]
    rp = re.match(r'\S+(\d{2})/.*',item[0])
    index = int(rp.groups()[0])
    if index in jnd_shuffle_train :
        train_data.append((os.path.join(prefix,item[0]),item[1]))
    else :
        test_data.append((os.path.join(prefix,item[0]),item[1]))

write2File(train_data,'JND_retrain_80percent_train.txt')
write2File(test_data,'JND_retrain_20percent_test.txt')
#print train_data
#print test_data

