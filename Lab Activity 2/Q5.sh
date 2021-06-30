#!/bin/bash
awk '{print $4" "$3" "$2" "$1}' "$1"