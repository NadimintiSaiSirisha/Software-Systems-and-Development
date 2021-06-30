#!/bin/bash
awk '{if($3=="work") {$3="good"};print }' "$1"