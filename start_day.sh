#!/bin/bash

if [ "$#" != "1" ]; then
    echo "Error: missing day argument"
else
    mkdir "Day-$1"
    cd "Day-$1"
    touch input
    touch main.py
    code ..
fi