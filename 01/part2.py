#!/usr/bin/env python
# encoding: utf-8

import sys

## DATA
filepath = "./input.txt"

## MAIN
sourcelist = []
with open(filepath) as fp:
  for line in fp:
    sourcelist.append(int(line.strip()))

for i in range(0, len(sourcelist)):
  for j in range(i + 1, len(sourcelist)):
    for k in range(j + 1, len(sourcelist)):
      if sourcelist[i] + sourcelist[j] + sourcelist[k] == 2020:
        print('Result :', sourcelist[i], '+', sourcelist[j], '+', sourcelist[k], '= 2020 and', sourcelist[i], '*', sourcelist[j], '*', sourcelist[k], '=', sourcelist[i] * sourcelist[j] * sourcelist[k])
        quit()