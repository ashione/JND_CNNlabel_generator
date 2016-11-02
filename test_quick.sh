#!/usr/bin/env sh
#TOOLS=/home/tj/caffe/distribute/bin

#$TOOLS/caffe.bin train \
NUM=${1:-100}
TOOLS=/home/tj/newdisk1/IQA_CNN/caffe/build/tools
OUTFILE=${2:-JND_outfile.txt}

$TOOLS/caffe.bin test --gpu=1 \
  --weights=../../../JND/models/train_ICME/JND_iter_400000.caffemodel \
  --model=./test.prototxt \
  --outfile=${OUTFILE} \
  --iterations=${NUM}

# reduce learning rate by factor of 10 after 8 epochs
#$TOOLS/caffe train \
#  --solver=examples/cifar10/cifar10_quick_solver_lr1.prototxt \
#  --snapshot=examples/cifar10/cifar10_quick_iter_4000.solverstate
