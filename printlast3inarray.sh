#!/bin/bash

declare -a arr=("FirstWord" "SecondWord" "thirdword" '4' 'kk' 's')

echo ${arr[@]}

#echo ${#arr[@]}
declare -a res
n=${#arr[@]}

echo ${arr[@]:$n-3:3}
