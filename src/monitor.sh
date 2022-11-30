#! /bin/bash

declare -a algorithms=("bnb" "tat" "christofides")
declare -a distances=("euclidean" "manhattan")

for i in {4..10}; do
    entrie="2^$i"

    for algo in "${algorithms[@]}"; do
        for distance in "${distances[@]}"; do
            timeout 10s echo "hello $i" || [ $? -eq 124 ] && echo timeouted
        done
    done
done
