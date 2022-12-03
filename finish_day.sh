#!/bin/bash

if [ "$#" != "1" ]; then
    echo "Error: missing day argument"
else
    git add "Day-$1"
    git commit -m "Day $1"
    git push origin main
fi