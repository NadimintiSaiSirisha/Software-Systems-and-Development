#!/bin/bash
mkdir Assignment1
cd Assignment1
touch lab{1..5}.txt 
ls *.txt | sed 's/.txt/''/g' | xargs -I {} mv {}.txt {}.c
ls -lSr
find /home/$HOSTNAME/ -mindepth 0 -maxdepth 2
ls *.txt &>/dev/null
if [ $? -eq 0 ];
 then
    ls *.txt | xargs realpath
fi
