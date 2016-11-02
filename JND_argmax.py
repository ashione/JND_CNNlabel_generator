#!/usr/bin/python
import numpy as np
import sys
import re

if __name__ == '__main__':
    if len(sys.argv) < 3 :
        print 'usage : argmax resultfile records'
        exit(1)

    result_file = sys.argv[1]
    record_file = sys.argv[2]
    labels = np.loadtxt(result_file,dtype = { 'names' : ('image_patch','patch_lable'), 'formats' : ('S100','i4')})
    record_label = np.loadtxt(record_file,dtype = np.uint8 )#{ 'names' : ('patch_lable') , 'formats' : ('i4')})
    labels['patch_lable'] = record_label

    remtch = re.compile("((\S*)_(\d*).jpg$)")
    #print np.sort(labels)
    np.savetxt('patch_label.txt',np.sort(labels),fmt='%s %d')
    lables_dict = {}

    for i,item in enumerate(labels['image_patch']):
        item_matched = remtch.findall(item)[0]
        if lables_dict.has_key(item_matched[1]):
            lables_dict[item_matched[1]].append(labels['patch_lable'][i])
        else:
            lables_dict[item_matched[1]] = [labels['patch_lable'][i]]
    #print lables_dict
    #for it in lables_dict.keys():
    #    print it,len(lables_dict[it])
