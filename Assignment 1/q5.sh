#!/bin/bash
read input
s=$(echo "${input,,}")
if [[ $(rev <<< "$s") == "$s" ]]
then
    echo Yes
else echo No
fi