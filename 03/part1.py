#!/usr/bin/env python
# encoding: utf-8

import sys

## DATA
filepath = "./input.txt"
# ............#....#.............

## functions
def istree(landline, position):
  newpos = position % len(landline)
  if landline[newpos] == '#':
    return 1
  else:
    return 0

## MAIN
land = []
with open(filepath) as fp:
  for line in fp:
    land.append(line.strip())

x = 0
treecount = 0
for landline in land:
  if istree(landline, x) == 1:
    treecount += 1
  x += 3

print('You hit', treecount, 'trees')