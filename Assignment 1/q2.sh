#!/bin/bash
read input
length=${#input}
sorted_input=$(echo $input | grep -o . | sort | tr -d "\n")
i=$(compgen -c | grep -x '.\{'$length'\}')
for var in $i 
do 
    sorted_command=$(echo $var | grep -o . | sort | tr -d "\n")
     if [ $sorted_input == $sorted_command ]
     then 
         echo "Yes"
         echo $var
         exit
     fi
done
echo "No"