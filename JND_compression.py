import Image
import os,sys
from joblib import Parallel, delayed

class  JNDJpegCompression:

    def __init__(self,srcImg=None,saveDir='./compressionDir'):

        #print os.path.isfile(srcImg)

        if srcImg is not None and os.path.isfile(srcImg) :
            self.src_img_path = os.path.basename(srcImg)
            self.src_img = Image.open(srcImg)
            if os.path.exists(saveDir):
                os.system("rm -r {0}".format(saveDir))
            os.system("mkdir {0}".format(saveDir))
            self.save_dir = saveDir
        else :
            print 'Error srcImage path or saveDir'
            sys.exit(1)

    def compressImage (self,quality=100):
        temp_image_format = '{0}_{1:03d}.jpg'.format(os.path.join(self.save_dir,'.'.join(self.src_img_path.split('.')[:-1])),quality)
        self.src_img.save(temp_image_format,'JPEG',quality=quality)
        self.src_jpg_namelist.append(os.path.abspath(temp_image_format))


    def batchCompressImage(self, num=100):
        #Parallel(n_jobs=2)(delayed(compressImage)(self.src_img,self.src_img_path,self.save_dir,i) for i in range(1,num+1))
        self.src_jpg_namelist = []
        [self.compressImage(i) for i in range(1,num+1)]
        #print self.src_jpg_namelist
        self.writeLabel()

    def writeLabel(self,classN=0):
        with open(os.path.join(self.save_dir,'label.txt'),'w') as fp:
            map(lambda x : fp.write('{0} {1}\n'.format(x,classN)),self.src_jpg_namelist)
            fp.close()

if __name__ == '__main__':
    srcImg = sys.argv[1]
    jndc = JNDJpegCompression(srcImg=srcImg)
    jndc.batchCompressImage()
