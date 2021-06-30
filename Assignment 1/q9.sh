#!/bin/bash
read input
input=$(echo $input | tr -d ' ')
length=${#input}
if [ "$(echo "$input" | sed 's/[0-9]//g')" ]
then
{
    echo "Invalid"
    exit
}
fi
if [ $length -le 1 ]
then
{
    echo "Invalid"
    exit
}
fi
sum=0
even=0
for ((i=$length-1;i>=0;i--))
do
digit=${input:$i:1}
if [ $even -eq 0 ]
then 
{ 
sum=$(( $sum+$digit ))
even=1
}
else
{
double=$(( $digit*2 ))
if [ $double -gt 9 ]
then
{
    double=$(( $double-9 ))
}
fi
sum=$(( $sum+$double ))    
even=0
}
fi
done
if [ $(( $sum%10)) -eq 0 ]
then
{
echo "Valid"
}
else
{
echo "Invalid"
}
fi