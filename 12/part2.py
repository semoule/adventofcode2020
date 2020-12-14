#!/usr/bin/env python
# encoding: utf-8

from itertools import cycle

## DATA
filepath = "./input.txt"

## FUNCTIONS
def getposition(instruction, value):
  if instruction == 'N':
    return ((positionlist[-1][0][0], positionlist[-1][0][1]), (positionlist[-1][1][0], positionlist[-1][1][1] + value))
  if instruction == 'S':
    return ((positionlist[-1][0][0], positionlist[-1][0][1]), (positionlist[-1][1][0], positionlist[-1][1][1] - value))
  if instruction == 'E':
    return ((positionlist[-1][0][0], positionlist[-1][0][1]), (positionlist[-1][1][0] + value, positionlist[-1][1][1]))
  if instruction == 'W':
    return ((positionlist[-1][0][0], positionlist[-1][0][1]), (positionlist[-1][1][0] - value, positionlist[-1][1][1]))

  if instruction == 'F':
    return ((positionlist[-1][0][0] + value * positionlist[-1][1][0], positionlist[-1][0][1] + value * positionlist[-1][1][1]), (positionlist[-1][1][0], positionlist[-1][1][1]))

  if instruction == 'L':
    waypoint = (positionlist[-1][1][0], positionlist[-1][1][1])
    for i in range(0, int(360 - value / 90)):
      waypoint = (waypoint[1], waypoint[0] * -1)
      
  if instruction == 'R':
    waypoint = (positionlist[-1][1][0], positionlist[-1][1][1])
    for i in range(0, int(value / 90)):
      waypoint = (waypoint[1], waypoint[0] * -1)

  return ((positionlist[-1][0][0], positionlist[-1][0][1]), (waypoint[0], waypoint[1]))

## MAIN
#create data structure
movelist = []
with open(filepath) as fp:
  for line in fp:
    movelist.append((line[0], int(line[1:].strip())))

# origin state
# ship(x,y), waypoint(x,y)
positionlist = [((0, 0), (10, 1))]

# move ship
for move in movelist:
  positionlist.append(getposition(move[0], move[1]))
  #print(positionlist)

manhattandistance = abs(positionlist[-1][0][0]) + abs(positionlist[-1][0][1])
print('Manhattan distance :', manhattandistance)