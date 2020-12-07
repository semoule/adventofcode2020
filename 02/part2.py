#!/usr/bin/env python
# encoding: utf-8

import sys

## DATA
filepath = "./input.txt"
# 9-10 m: mmmmnxmmmwm

## MAIN

pwlist = []
with open(filepath) as fp:
  line = fp.readline()
  while line:
    wqt, wchar, wpass = line.strip().split(' ')
    wmin, wmax = wqt.strip().split('-')
    pwlist.append((wmin,wmax,wchar[0],wpass))
    line = fp.readline()

passvalid = 0
for item in pwlist:
  # pos1,pos2,char,pass
  candidate = 0
  try:
    if item[3][int(item[0]) - 1] == item[2]:
      candidate = candidate + 1
  except:
    pass
  try:
    if item[3][int(item[1]) - 1] == item[2]:
      candidate = candidate + 1
  except:
    pass
  if candidate == 1:
    passvalid = passvalid + 1

print(passvalid)