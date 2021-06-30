#!/bin/bash
# Display all occurences of word "to"
grep -i -w 'to' hamlet.txt
# Display all occurences of word "is"
grep -w "is" hamlet.txt
#Display two lines below the word "bear"
grep -w "bear" -A 2 hamlet.txt | grep -v "bear"
#Removing rwx access for group and others using symbolic way
chmod o-rwx hamlet.txt
chmod g-rwx hamlet.txt
#Removing rwx access for group and others using octal way
chmod 600 hamlet.txt
#Allow everyone to rwx the file
chmod 777 hamlet.txt
#View all the groups the current user is attached to
groups
# Change the group of hamlet.txt to sudo
chown :sudo hamlet.txt
# List all the files from home directory for which group has execute permissions
ls -l -p | grep -v / | grep "^.........x" | awk '{ print $9 }'

