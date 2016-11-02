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
baseOriginImage=`basename ${originImage}`
python JND_slice.py compressionDir compressionDir_crop  label.txt
#sed 's/INPUTIAMGE/compressionDir_crop\/label.txt/g' ./test.prototxt.template  test.prototxt
num=`wc -l compressionDir_crop/label.txt|awk '{print $1}'`
sh test_quick.sh $num result_dir/${baseOriginImage}.txt
cp compressionDir_crop/label.txt result_dir/${baseOriginImage}.label
#python JND_judger.py >> JND_juder.log
