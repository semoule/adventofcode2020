#!/usr/bin/env python
# encoding: utf-8

import copy

## DATA
filepath = "./input.txt"

## FUNCTIONS
def split(word): 
  return [char for char in word]

def left(x, y):
  global seatmapcurrent
  for xx in range(x - 1, -1, -1):
    if seatmapcurrent[y][xx] == '#': return True
    if seatmapcurrent[y][xx] == 'L': return False
  return False

def right(x, y):
  global seatmapcurrent
  for xx in range(x + 1, xmax + 1, 1):
    if seatmapcurrent[y][xx] == '#': return True
    if seatmapcurrent[y][xx] == 'L': return False
  return False

def down(x, y):
  global seatmapcurrent
  for yy in range(y + 1, ymax + 1, 1):
    if seatmapcurrent[yy][x] == '#': return True
    if seatmapcurrent[yy][x] == 'L': return False
  return False

def up(x, y):
  global seatmapcurrent
  for yy in range(y - 1, -1, -1):
    if seatmapcurrent[yy][x] == '#': return True
    if seatmapcurrent[yy][x] == 'L': return False
  return False

def upleft(x, y):
  global seatmapcurrent
  yy = y - 1
  if yy >= 0:
    for xx in range(x - 1, -1, -1):
      if yy < 0: break
      if seatmapcurrent[yy][xx] == '#': return True
      if seatmapcurrent[yy][xx] == 'L': return False
      yy -= 1
  return False

def downleft(x, y):
  global seatmapcurrent
  yy = y + 1
  if yy <= ymax:
    for xx in range(x - 1, -1, -1):
      if yy > ymax: break
      if seatmapcurrent[yy][xx] == '#': return True
      if seatmapcurrent[yy][xx] == 'L': return False
      yy += 1
  return False

def upright(x, y):
  global seatmapcurrent
  yy = y - 1
  if yy >= 0:
    for xx in range(x + 1, xmax + 1, 1):
      if yy < 0: break
      if seatmapcurrent[yy][xx] == '#': return True
      if seatmapcurrent[yy][xx] == 'L': return False
      yy -= 1
  return False

def downright(x, y):
  global seatmapcurrent
  yy = y + 1
  if yy <= ymax:
    for xx in range(x + 1, xmax + 1, 1):
      if yy > ymax: break
      if seatmapcurrent[yy][xx] == '#': return True
      if seatmapcurrent[yy][xx] == 'L': return False
      yy += 1
  return False

def get_neighbours_status(x, y):
  status_list = []
  status_list.append(upleft(x,y))
  status_list.append(up(x,y))
  status_list.append(upright(x,y))
  status_list.append(left(x,y))
  status_list.append(right(x,y))
  status_list.append(downleft(x,y))
  status_list.append(down(x,y))
  status_list.append(downright(x, y))
  return status_list.count(True)

def swap(x, y):
  global seatmapcurrent
  global seatmapfuture
  if seatmapcurrent[y][x] == '.':
    return False

  occupiedcount = get_neighbours_status(x, y)
  changecount = 0

  if seatmapcurrent[y][x] == 'L':
    if occupiedcount == 0:
      seatmapfuture[y][x] = '#'
      changecount += 1

  if seatmapcurrent[y][x] == '#':
    if occupiedcount >= 5:
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