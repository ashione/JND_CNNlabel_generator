#!/bin/bash
if [ $# -lt 1 ]; then
    echo 'usage % dir'
    exit 1
fi

rm -rf result_dir
mkdir result_dir

rootdir=$1
for f in `ls $rootdir` ; do
    sh ./test_origin.sh $rootdir/$f 
done
