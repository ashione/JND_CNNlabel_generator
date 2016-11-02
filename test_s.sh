#!/usr/bin/env sh
TOOLS=/home/tj/newdisk1/IQA_CNN/caffe/build/tools

#$TOOLS/caffe.bin train \

rt_predict.bin  \
  --gpu=0 \
  --model=test.prototxt \
  --weights=../../../JND/models/train_ICME/JND_iter_400000.caffemodel \
  --image=/home/zlx/workspace/IQA_CNN/image_data/MCL-JCI/source_images/[BMP]/ImageJND_SRC50.bmp \
  --classnum=8 \
  --batchsize=480 

#  --image=/home/tj/zlx/image_test/Whiplash20181080p.jpg \

