#!/bin/bash
if [ $# -lt 1 ]  
then
    echo 'usage -originImage'
    exit 1
fi

originImage=$1
if [ ! -f $originImage  ]; then
    echo $1,'not exist'
    exit 1
fi

python JND_compression.py $originImage
sed 's/INPUTIAMGE/compressionDir\/lable.txt/g' ./test.prototxt.template test.prototxt
sh test_quick.sh
python JND_judger.py
