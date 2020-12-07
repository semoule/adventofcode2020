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
  charcount = item[3].count(item[2])
  if charcount >= int(item[0]) and charcount <= int(item[1]):
    passvalid = passvalid + 1

print(passvalid)