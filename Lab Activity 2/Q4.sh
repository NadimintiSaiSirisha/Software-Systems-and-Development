#!/bin/bash
awk '/^TS(-|[ \s])(S|5)(S|5)(-|[ \s])(S|5).*0/ {print}' "$1"