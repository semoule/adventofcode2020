#!/usr/bin/env python
# encoding: utf-8

## DATA
filepath = "./input.txt"

## FUNCTIONS
def recursive(color):
  # search bag with outer color 'color'
  for item in chain:
    if item[0] == color:
      if len(item[1:]):
        # if this bag can contain other bags
        for qt, innercolor in item[1:]:
          if innercolor == 'shinygold':
            # this bag contains directly the shinygold
            return True
          else:
            # this bag contains other bags, going to deeper check
            result = recursive(innercolor)
            if result:
              # This bag as a match, don't need to check other bags
              return True
      else:
        # dead end: this bag dont contains other bags
        return False
  # bag not found in chain. This error shouldn't happen.
  return False

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

colorlist = []
for alice in chain:
  # explore all bags
  if len(alice[1:]):
    # if bag contain other bags
    for qt, color in alice[1:]:
      if color == 'shinygold':
        # the bag contains directly the shinygold, save it
        colorlist.append(alice[0])
        break
      else:
        # the bag contain other color, going deeper
        if recursive(color):
          colorlist.append(alice[0])
          break

# create set 
myset = set(colorlist)
print('Bags that can contain a shiny gold bag :',len(myset))