#!/bin/bash
cat ~/.bash_history | tail -n 10 | awk '{ print $1 }' | sort | uniq -c | sort -r $1 |awk '{ print $2 " " $1}'
