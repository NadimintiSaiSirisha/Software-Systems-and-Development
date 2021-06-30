#!/bin/bash
awk '/^s[^a]/ {print}' "$1"