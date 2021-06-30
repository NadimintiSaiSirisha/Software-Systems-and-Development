#!/bin/bash
number=$#
inputs=( "$@" )
exp=${inputs[0]}
for k in ${inputs[@]:1}
do
exp=$(($exp ** $k))
done
echo $exp
