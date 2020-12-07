#!/usr/bin/env python
# encoding: utf-8

## DATA
filepath = "./input.txt"

## functions
def istree(landline, position):
  newpos = position % len(landline)
  return landline[newpos] == '#'

def runslope(land, x, y):
  land_iter=iter(land)
  xpos = 0
  treecount = 0
  for landline in land_iter:
    if istree(landline, xpos):
      treecount += 1
    xpos += x
    for skippedy in range(0, y - 1):
      try:
        next(land_iter)
      except:
        pass
  print('run (',x,',',y,') : you hit', treecount, 'trees')
  return treecount

## MAIN
land = []
with open(filepath) as fp:
  for line in fp:
    land.append(line.strip())

print(runslope(land, 1, 1) * runslope(land, 3, 1) * runslope(land, 5, 1) * runslope(land, 7, 1) * runslope(land, 1, 2))