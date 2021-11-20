#!/usr/bin/env python
# encoding: utf-8

import time
import re
from rich.console import Console
from rich.traceback import install
from rich.progress import track
install()
start_time = time.time()

## DATA
filepath = "./short.txt"

## FUNCTIONS
def get_sides(tile, mode):
  # return ordered list of side (up, right, down, left) for the tile
  # mode apply rotation and/or flip :
  # 0 = no change
  # 1 = rotate 90 clockwise
  # 2 = rotate 180 clockwise
  # 3 = rotate 270 clockwise
  # 4 = flipped
  # 5 = flipped + rotate 90 clockwise
  # 6 = flipped + rotate 180 clockwise
  # 7 = flipped + rotate 270 clockwise
  slist = []
  
  # 0 = no change
  if mode == 0:
    # up
    slist.append(tile['value'][0])
    # right
    side = ''
    for i in range(0, 10):
      side = side + tile['value'][i][9]
    slist.append(side)
    # down
    slist.append(tile['value'][9])
    # left
    side = ''
    for i in range(0, 10):
      side = side + tile['value'][i][0]
    slist.append(side)

  # 1 = rotate 90 clockwise
  elif mode == 1:
    # up
    side = ''
    for i in range(0, 10):
      side = side + tile['value'][i][0]
    slist.append(side[::-1])
    # right
    slist.append(tile['value'][0])
    # down
    side = ''
    for i in range(0, 10):
      side = side + tile['value'][i][9]
    slist.append(side[::-1])
    # left
    slist.append(tile['value'][9])

  # 2 = rotate 180 clockwise
  elif mode == 2:
    # up
    slist.append(tile['value'][9][::-1])
    # right
    side = ''
    for i in range(0, 10):
      side = side + tile['value'][i][0]
    slist.append(side[::-1])
    # down
    slist.append(tile['value'][0][::-1])
    # left
    side = ''
    for i in range(0, 10):
      side = side + tile['value'][i][9]
    slist.append(side[::-1])

  # 3 = rotate 270 clockwise
  elif mode == 3:
    # up
    side = ''
    for i in range(0, 10):
      side = side + tile['value'][i][9]
    slist.append(side)
    # right
    slist.append(tile['value'][9][::-1])
    # down
    side = ''
    for i in range(0, 10):
      side = side + tile['value'][i][0]
    slist.append(side)
    # left
    slist.append(tile['value'][0][::-1])

  # 4 = flipped
  elif mode == 4:
    # up
    slist.append(tile['value'][0][::-1])
    # right
    side = ''
    for i in range(0, 10):
      side = side + tile['value'][i][0]
    slist.append(side)
    # down
    slist.append(tile['value'][9][::-1])
    # left
    side = ''
    for i in range(0, 10):
      side = side + tile['value'][i][9]
    slist.append(side)

  # 5 = flipped + rotate 90 clockwise
  elif mode == 5:
    # up
    side = ''
    for i in range(0, 10):
      side = side + tile['value'][i][0]
    slist.append(side)
    # right
    slist.append(tile['value'][0])
    # down
    side = ''
    for i in range(0, 10):
      side = side + tile['value'][i][9]
    slist.append(side)
    # left
    slist.append(tile['value'][9])

  # 6 = flipped + rotate 180 clockwise
  elif mode == 6:
    # up
    slist.append(tile['value'][9])
    # right
    side = ''
    for i in range(0, 10):
      side = side + tile['value'][i][0]
    slist.append(side[::-1])
    # down
    slist.append(tile['value'][0])
    # left
    side = ''
    for i in range(0, 10):
      side = side + tile['value'][i][9]
    slist.append(side)

  # 7 = flipped + rotate 270 clockwise
  elif mode == 7:
    # up
    side = ''
    for i in range(0, 10):
      side = side + tile['value'][i][9]
    slist.append(side[::-1])
    # right
    slist.append(tile['value'][9][::-1])
    # down
    side = ''
    for i in range(0, 10):
      side = side + tile['value'][i][0]
    slist.append(side[::-1])
    # left
    slist.append(tile['value'][0][::-1])
  return slist

def tile_friends(candidate):
  #console.print(candidate)
  friends_count = 0
  for tile in tiles_side:
    if tile['id'] != candidate['id']:
      for side in tile['sides']:
        for candidate_side in candidate['sides']:
          if candidate_side == side:
            friends_count += 1
  return friends_count

## MAIN
console = Console()

# load data
tiles = []
tile = []
with open(filepath) as fp:
  for line in fp:
    if line[0:4] == "Tile":
      tile_id = line[5:9]
    elif line[0] == '#' or line[0] == '.':
      tile.append(line.strip())
    else:
      if len(tile):
        tiles.append({'id': tile_id, 'value': tile})
        tile = []



# create board list and place the first tile.
# board items: x, y, tile, mode (0-7)
board = []
board.append((0, 0, tiles[0], 0))
tiles_left = tiles[1:]

while len(board) < len(tiles):
  for tile in tiles_left:
    for tileset in board:
      success, mode, position = compare(tileset[2], tile)
      if success:
        if position == "up":
          board.append(tileset[0], tileset[1] + 1, tile, mode)
        elif position == "right":
          board.append(tileset[0] + 1, tileset[1], tile, mode)
        elif position == "down":
          board.append(tileset[0], tileset[1] - 1, tile, mode)
        elif position == "left":
          board.append(tileset[0] - 1, tileset[1], tile, mode)
        tiles_left.remove(tile)
        break



console.print(board)
quit()











# find the corners
corner_count = 0
corners = []
for tile in tiles_side:
  friends = tile_friends(tile)
  console.print(tile, 'friends :', friends)
  
  if friends == 2:
    corners.append(tile['id'])
    corner_count += 1
  #if corner_count == 4:
  #  break

for corner in corners:
  print(corner)









  #console.print(tiles)
#for tile in tiles:
#  console.print()
#  console.print('Tile', tile['id'], ':')
#  for val in tile['value']:
#    console.print(val)

#tiles_side = []
#for tile in tiles:
#  sides = get_sides(tile,0)
#  tiles_side.append({'id': tile['id'], 'sides': sides})

#console.print('Tile', tiles[0]['id'], ':')
#for line in tiles[0]['value']:
#  console.print(line)
#
#console.print()
#console.print(tiles_side[0])
#for tile in tiles_side:
#  console.print('Tile', tile['id'], ':')
#  for side in tile['sides']:
#    console.print(side)

#quit()
# create board list
# items: x, y, tileid, tilerotation (0,1,2,3)
#board = []
#board.append((0, 0, tiles_side[0]['id'], 0))
#console.print(board)


