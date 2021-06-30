#!/bin/bash
read input
echo $input | sed 's/[()]/ /g' | tr -s " " |sed -e 's/^[[:space:]]//'| sed -e 's/[[:space:]]$//' | sed 's/\(^.*$\)/\(\1\)/g'



