#!/usr/bin/env python
# encoding: utf-8

from itertools import combinations

## DATA
filepath = "./input.txt"
plen = 25

## FUNCTIONS
def verify(mylist, candidate):
  for pair in list(combinations(mylist, 2)):
    if pair[0] + pair[1] == candidate:
      return True
  return False

## MAIN
numlist = []
with open(filepath) as fp:
  for line in fp:
    numlist.append(int(line))

offset = 0
while offset + plen < len(numlist):
  testlist = numlist[offset:offset + plen]
  candidate = numlist[offset + plen]
  valid = verify(testlist, candidate)
  if not valid: break
  offset += 1

print('Part 1 : The first invalid number is :', candidate)

offset = 0
listfound = []
while offset < len(numlist) and listfound == []:
  sum = 0
  i = 0
  for n in numlist[offset::]:
    sum += n
    i += 1
    if sum == candidate:
      listfound = numlist[offset:offset + i ]
      break
    if sum > candidate:
      break
  offset += 1

print('Part 2 : lowest :', min(listfound), 'highest :', max(listfound), 'sum :', min(listfound) + max(listfound))