#!/usr/bin/env python
# encoding: utf-8

import time
from rich.console import Console
from rich.traceback import install
from rich.progress import track
install()
start_time = time.time()

## DATA
filepath = "./input.txt"

## FUNCTIONS
def getnewstate(state, x, y, z):
  # return new state of conway cube at pos x,y,z
  #console.print('consider :', state, x, y, z)
  activecount = 0
  for wz in range(z - 1, z + 2):
    for wy in range(y - 1, y + 2):
      for wx in range(x - 1, x + 2):
        if not (wx == x and wy == y and wz == z):
          #console.print('check :', wx, wy, wz)
          if next((item["active"] for item in grid if item["coord"] == (wx, wy, wz)), False):
            #console.print('active found :', wx, wy, wz)
            activecount += 1
  if state and (activecount == 2 or activecount == 3):
    return True
  if not state and activecount == 3:
    return True
  return False

## MAIN
console = Console()

# load data
grid = []
with open(filepath) as fp:
  y = 0
  for line in fp:
    x = 0
    for char in line.strip():
      if char == '.':
        state = False
      else:
        state = True
      grid.append({'active': state, 'coord': (x, y, 0)})
      x += 1
    y += 1

# init
xmin = 0
ymin = 0
zmin = 0
xmax = x
ymax = y
zmax = 0

# boot sequence
for i in track(range(0, 6)):
  xmin -= 1
  ymin -= 1
  zmin -= 1
  xmax += 1
  ymax += 1
  zmax += 1
  cyclegrid = []
  for z in range(zmin, zmax+1):
    for y in range(ymin, ymax+1):
      for x in range(xmin, xmax+1):
        current_state = next((item["active"] for item in grid if item["coord"] == (x, y, z)), False)
        new_state = getnewstate(current_state, x, y, z)
        cyclegrid.append({'active': new_state, 'coord': (x, y, z)})
  grid = cyclegrid

# count and print result
count = 0
for cube in grid:
  if cube["active"]:
    count += 1
console.print('Conway cube active count is :', count)
console.print('Duration : %.2f seconds' % (time.time() - start_time))