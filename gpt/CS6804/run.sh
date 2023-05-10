#!/bin/bash

increment=3
for (( i = 0; i < 16090; i=i+3 ));
do
  end=$(($i + $increment))
  python3 gpt/dataloader/loader.py $i $end
  sleep 1m
done