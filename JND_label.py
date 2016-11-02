#!/usr/bin/python
from JND import JNDLevel
from random import shuffle
class JNDLabel:
    def __init__(self,jndlevel=None,
                 imageFileNameFormat='ImageJND_SRC{src:02d}/ImageJND_SRC{src:02d}_{jpg:03d}.jpg'):
        self.imageFileNameFormat = imageFileNameFormat
        if jndlevel is not None:
            self.jndlevel = jndlevel
        else :
            self.jndlevel = JNDLevel()

        self.jnd_level = map(lambda x : x+[(0,0)],self.jndlevel.jnd)

    def order_level(self,src,jpg):
        for level,item in enumerate(self.jnd_level[src-1]):
            if item[0] < jpg:
                #return len(self.jnd_level[src-1])-level
                return level-1
        return -1

    def generate(self):
        self.jnd_label = []
        for src in range(1,self.jndlevel.fileNums+1):
            for jpg in range(1,self.jndlevel.jpegFactor+1):
                imageFileName = self.imageFileNameFormat.format(src=src,jpg=jpg)
                imageLevel = self.order_level(src,jpg)
                self.jnd_label.append(( imageFileName,imageLevel))
        return self.jnd_label

def writeLabelToFile(label,fileName='./JND_label.txt'):
    shuffle(label)
    writeFile = open(fileName,'w')
    for item in label:
        writeFile.write('{} {}\n'.format(item[0],item[1]))
    writeFile.close()
    print 'write label file finished'

# write lable for slices of original image
def sliceLable(label):
    slicelbs = []
    print label
    for item in label :
        index = item[0].find('.')
        for i in range(0,480):
            slicelbs.append((item[0][:index]+'_'+str(i)+item[0][index:],item[1]))
    return slicelbs

if __name__ == '__main__':

    JNDlabel = JNDLabel()
    writeLabelToFile(JNDlabel.generate())
    writeLabelToFile(sliceLable(JNDlabel.generate()),'./JND_label_crop.txt')

