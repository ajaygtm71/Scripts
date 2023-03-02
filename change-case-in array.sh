#!/bin/bash

declare -a arr=("FirstWord" "SecondWord" "thirdword")

#echo ${arr[@]}

#echo ${#arr[@]}
declare -a res
for word in ${arr[@]}
do
        res=(${res[@]} `echo -ne "$word "|tr [:lower:] [:upper:]`)
done

echo ${res[@]}
