cal > out1.txt
date >> out1.txt
cat out1.txt
tail -n 3 out1.txt
head -n 7 out1.txt | tail -n 5
head -n 7 out1.txt | tail -n 5 | wc -l
echo "This day is awesome." >> out2.txt
cat out2.txt
cat out2.txt | wc -w
echo "I am looking forward to the day." >> out2.txt
cat out2.txt | wc -l
cat out1.txt | awk '{ print $5 }'
cat out1.txt | cut -d ' ' -f4-9
cat out1.txt | cut -d ' ' -f3-
cat out2.txt | cut -d ' ' -f2,4
