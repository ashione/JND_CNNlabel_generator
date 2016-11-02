#!/usr/bin/python
import os,sys
class JNDLevel:

    def __init__(self,fileName='../SQF_data/Image_%d_l_h.txt',fileNums=50,jpegFactor=100):
        self.fileName = fileName
        self.fileNums = fileNums
        self.jpegFactor = jpegFactor
        self.generate()

    def readFile(self,fileName):
        tempFile = open(fileName)
        lines = map(lambda x : filter(lambda f : f!='',x.replace('\r','').replace('\n','').split(' ')),tempFile.readlines())
        return map(lambda x : (int(x[0]),float( x[1] )),zip(lines[0],lines[1]))

    def generate(self):
        self.jnd = []
        self.maxJND_level = 0
        for i in range(1,self.fileNums+1):
            tempFileName = self.fileName.replace('%d',str(i))
            self.jnd.append( self.readFile(tempFileName))
            self.maxJND_level = max(self.maxJND_level,len(self.jnd[len(self.jnd)-1]))


# added at 2016-11-02 for libsvm training number of JND
# there are ordered by number from 1 to 50 in MCL database
def generateJNDNumberTrainingLabel(jnd,filename='./JND_label_number.txt'):
    
    fp = open(filename,'w+')
    for i,item in enumerate(jnd):
        fp.write('{no} {levels}'.format(no=i+1,levels=len(item)))
        for order in item :
            fp.write(' {0}'.format(order[0]))
        fp.write('\n')
    fp.close()
    print 'jnd label number file written done'


if __name__ == '__main__':
    jnd = JNDLevel()
    print jnd.jnd
    generateJNDNumberTrainingLabel(jnd.jnd)
    #print jnd.maxJND_level


