#!/bin/bash
args=("$@")
echo ${args}
start=`date +%s`
$@
end=`date +%s`
runtime=$((end-start))

echo "Duration: $runtime seconds"
python /Users/jordan/Source/bash-notify/test.py $runtime
