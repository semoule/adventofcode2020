#!/usr/bin/env python
# encoding: utf-8

import copy

## DATA
filepath = "./input.txt"

## FUNCTIONS
def split(word): 
  return [char for char in word]

def findneighbours(x, y):
  neighbourslist = []
  if x - 1 >= 0 and y - 1 >= 0:       neighbourslist.append((x - 1, y - 1))
  if x - 1 >= 0 and y >= 0:           neighbourslist.append((x - 1, y ))
  if x - 1 >= 0 and y + 1 <= ymax:    neighbourslist.append((x - 1, y + 1))
  if x >= 0 and y - 1 >= 0:           neighbourslist.append((x, y - 1))
  if x >= 0 and y + 1 <= ymax:        neighbourslist.append((x, y + 1))
  if x + 1 <= xmax and y - 1 >= 0:    neighbourslist.append((x + 1, y - 1))
  if x + 1 <= xmax and y >= 0:        neighbourslist.append((x + 1, y))
  if x + 1 <= xmax and y + 1 <= ymax: neighbourslist.append((x + 1, y + 1))
  return neighbourslist

def swap(x, y):
  global seatmapcurrent
  global seatmapfuture
  if seatmapcurrent[y][x] == '.':
    return False

  neighbourlist = findneighbours(x, y)
  changecount = 0
  occupiedcount = 0

  for neighbour in neighbourlist:
    if seatmapcurrent[neighbour[1]][neighbour[0]] == '#':
      occupiedcount += 1

  if seatmapcurrent[y][x] == 'L':
    if occupiedcount == 0:
      seatmapfuture[y][x] = '#'
      changecount += 1

  if seatmapcurrent[y][x] == '#':
    if occupiedcount >= 4:
      seatmapfuture[y][x] = 'L'
      changecount += 1

  if changecount:
    return True
  else:
    return False


## MAIN
#create data structure
seatmap = []
with open(filepath) as fp:
  for line in fp:
    seatmap.append(split(line.strip()))

# init
xmax = len(seatmap[0]) - 1
ymax = len(seatmap) - 1
round = 0
seatmapcurrent = copy.deepcopy(seatmap)
seatmapfuture = copy.deepcopy(seatmap)
stabilized = False

# round loop
while True:
  if stabilized:
    break

  changecount = 0
  y = 0
  for row in seatmapcurrent:
    x = 0
    for seat in row:
      if swap(x, y):
        changecount += 1
      x += 1
    y += 1

  seatmapcurrent = copy.deepcopy(seatmapfuture)
  round += 1
  if changecount == 0:
    stabilized = True

# result : count occupied seat
total = 0
for row in seatmapcurrent:
  for seat in row:
    if seat == '#':
      total += 1
      
print('Occupied seat count at stabilization:', total, '!', round, 'rounds computed !')