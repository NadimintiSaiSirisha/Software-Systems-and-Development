#!/bin/bash
ps -au | awk '{ print $2 }' | tail -n +2 > pid.txt
read input
maxPIDs=$(cat pid.txt | wc -l)
if [ $input -gt $maxPIDs ] 
then
input=$maxPIDs
fi
cat pid.txt | head -n $input
