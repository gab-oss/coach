#!/bin/bash

cd experiments
for dir in */; do
    echo "$dir"
    dashboard -d "${dir}/experiments"
done
