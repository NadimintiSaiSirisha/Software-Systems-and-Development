#!/bin/bash
read op
read n
read result
for (( i=1;i<n;i++ ))
do
read input
result=$(echo "$result $op $input" | bc -l) 
done
answer=$(echo $result | xargs printf "%.4f")
echo $answer