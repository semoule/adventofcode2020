#!/usr/bin/env python
# encoding: utf-8

from itertools import cycle

## DATA
filepath = "./input.txt"

## FUNCTIONS
def getposition(instruction, value):
  global direction
  
  if instruction == 'N':
    return (positionlist[-1][0], positionlist[-1][1] + value)
  if instruction == 'S':
    return (positionlist[-1][0], positionlist[-1][1] - value)
  if instruction == 'E':
    return (positionlist[-1][0] + value, positionlist[-1][1])
  if instruction == 'W':
    return (positionlist[-1][0] - value, positionlist[-1][1])

  if instruction == 'F':
    if direction == 'N':
      return (positionlist[-1][0], positionlist[-1][1] + value)
    if direction == 'S':
      return (positionlist[-1][0], positionlist[-1][1] - value)
    if direction == 'E':
      return (positionlist[-1][0] + value, positionlist[-1][1])
    if direction == 'W':
      return (positionlist[-1][0] - value, positionlist[-1][1])

  if instruction == 'L':
    direction = left(value)
  if instruction == 'R':
    direction = right(value)
  return(positionlist[-1][0], positionlist[-1][1])

def right(val):
  for i in range(0, int(val / 90)):
    res = next(compass)
  return res

def left(val):
  for i in range(0, int((360 - val) / 90)):
    res = next(compass)
  return res

## MAIN
#create data structure
movelist = []
with open(filepath) as fp:
  for line in fp:
    movelist.append((line[0], int(line[1:].strip())))

# origin state
positionlist = [(0, 0)]
direction = 'E'
compass = cycle(['S', 'W', 'N', 'E'])

# move ship
for move in movelist:
  positionlist.append(getposition(move[0], move[1]))

manhattandistance = abs(positionlist[-1][0]) + abs(positionlist[-1][1])
print('Manhattan distance :', manhattandistance)