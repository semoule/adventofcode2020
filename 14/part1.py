#!/usr/bin/env python
# encoding: utf-8

import re

## DATA
filepath = "./short.txt"

## FUNCTIONS
def compute(operation):
  mask = operation[0]
  memlist = operation[1]
  total = 0
  for mem in memlist:
    total += applymask(mask,mem)
  return total

def applymask(mask, mem):
  addr = mem[0]
  val = mem[1]
  result = 0
  print(mask,addr,val)
  return result

## MAIN
# load data
write_list = []
memlist = []
with open(filepath) as fp:
  for line in fp:
    if line[0:4] == 'mask':
      if memlist:
        write_list.append((mask,memlist))
      memlist = []
      mask = line[7:].strip()
    if line[0:3] == 'mem':
      address, val = re.match(r".*\[(\d+)\] = (\d+)", line).groups()
      memlist.append((address, val))
  write_list.append((mask,memlist))

print(write_list)

total = 0
for operation in write_list:
  total += compute(operation)

print(total)
