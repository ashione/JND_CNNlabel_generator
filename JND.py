#!/usr/bin/python
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



if __name__ == '__main__':
    jnd = JNDLevel()
    print jnd.maxJND_level


