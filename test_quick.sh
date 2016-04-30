#!/usr/bin/env sh
#TOOLS=/home/tj/caffe/distribute/bin

#$TOOLS/caffe.bin train \

TOOLS=/home/tj/newdisk1/IQA_CNN/caffe/build/tools

$TOOLS/caffe.bin test --gpu=1 \
  --weights=../../../JND/models/bvlc_alexnet/JND__iter_450000.caffemodel \
  --model=./test.prototxt \
  --outfile=JND_outfile.txt \
  --iterations=100
# reduce learning rate by factor of 10 after 8 epochs
#$TOOLS/caffe train \
#  --solver=examples/cifar10/cifar10_quick_solver_lr1.prototxt \
#  --snapshot=examples/cifar10/cifar10_quick_iter_4000.solverstate
