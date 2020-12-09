#!/usr/bin/env python
# encoding: utf-8

## DATA
filepath = "./input.txt"

## FUNCTIONS
def recursive(color):
  total = 0
  # search bag with outer color 'color'
  for item in chain:
    if item[0] == color:
      if len(item[1:]):
        # if this bag contains other bags
        for qt, innercolor in item[1:]:
          # count the bag itself, and this bag contains other bags : going to deeper check. 
          total += int(qt) * recursive(innercolor) + int(qt)
        return total
      else:
        # dead end: this bag dont contains other bags
        return 0
  # bag not found in chain. This error shouldn't happen.
  print('holy macaroni')
  return 0

## MAIN
#create data structure
chain = []
with open(filepath) as fp:
  for line in fp:
    colors = []
    colors.append(line.split()[0] + line.split()[1])  #color of external bag
    if line.split()[4] != 'no':
      # if bag not empty
      colors.append((line.split()[4], line.split()[5] + line.split()[6])) # amount , color of internal bag
      for i in range(0, line.count(',')):
        # there are more bags inside
        colors.append((line.split()[i * 4 + 8], line.split()[i * 4 + 9] + line.split()[i * 4 + 10]))
    chain.append(colors)

total = 0
for alice in chain:
  # we explore only shinygold bag
  if alice[0] == 'shinygold':
    # explore all nested bags
    if len(alice[1:]):
      # if bag contain other bags
      for qt, color in alice[1:]:
        # count the bag itself and go deeper
        total += int(qt) * recursive(color) + int(qt)

print('Total bags in a single shiny gold bag :', total)