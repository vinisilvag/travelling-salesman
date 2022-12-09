#! /bin/bash

declare -a algorithms=("bnb" "tat" "christofides")
declare -a distances=("euclidean" "manhattan")

for i in {4..10}; do
    entrie="2^$i"

    for algo in "${algorithms[@]}"; do
        for distance in "${distances[@]}"; do
            timeout 10s ping google.com
            EXIT_STATUS=$?

            if [ $EXIT_STATUS -eq 124 ]
            then
                echo "Entrie: 2^$i-$distance - Algorithm: $algo - failed!"
            else
                echo "Entrie: 2^$i-$distance - Algorithm: $algo - success!"
            fi
        done
    done
done
