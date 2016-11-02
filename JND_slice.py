#!/usr/bin/python
import sys,os
from imseg import ImageWalk,ImgCrop
import numpy as np


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print 'usage : crop source_dir destination_dir destination-label-path'
        exit(1)
    source_dir = sys.argv[1]
    crop_dir = sys.argv[2]
    label_txt = sys.argv[3]

    if os.path.exists(crop_dir) and os.path.isdir(crop_dir) :
        #os.rmdir(crop_dir)
        #os.removedirs(crop_dir)
        os.system(" rm -rf "+crop_dir)

    os.mkdir(crop_dir)
    walker = ImageWalk(source_dir)
    imcroper = ImgCrop(walker.getImageFile(),crop_dir,64,64);
    imcroper.crop()
    #print walker.getImageFile()

    label_walker = ImageWalk(crop_dir) 
    images_name = np.array(label_walker.getImageFile());
    images_fake_label = np.empty_like(images_name,dtype=np.uint8)
    images_fake_label[:] = 0
    data = np.column_stack((images_name,images_fake_label))
    #with open(os.path.join(crop_dir,label_txt),'w') as fp:
    #    for item in data :
    #        fp.write('%s %d\n' %(item[0],item[1]))
    #    fp.close()
    #print data[0,0]
    np.savetxt(os.path.join(crop_dir,label_txt),data,delimiter=' ',fmt='%s %s')
