#!/usr/bin/env python
# encoding: utf-8

import sys
import re

## DATA
filepath = "./input.txt"

## MAIN
pwlist = []
with open(filepath) as fp:
  for line in fp:
    pos1, pos2, char, pwd = re.match(r"(\d+)-(\d+) (\w): (\w+)", line).groups()
    pwlist.append((pos1, pos2, char, pwd))

passvalid = 0
for item in pwlist:
  candidate = 0
  try:
    if item[3][int(item[0]) - 1] == item[2]:
      candidate += 1
  except:
    pass
  try:
    if item[3][int(item[1]) - 1] == item[2]:
      candidate += 1
  except:
    pass
  if candidate == 1:
    passvalid += 1

print('Valid password count :', passvalid)