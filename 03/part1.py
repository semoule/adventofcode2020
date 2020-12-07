#!/usr/bin/env python
# encoding: utf-8

import sys

## DATA
filepath = "./input.txt"

## functions
def istree(landline, position):
  newpos = position % len(landline)
  return landline[newpos] == '#'

## MAIN
land = []
with open(filepath) as fp:
  for line in fp:
    land.append(line.strip())

x = 0
treecount = 0
for landline in land:
  if istree(landline, x):
    treecount += 1
  x += 3

print('You hit', treecount, 'trees')