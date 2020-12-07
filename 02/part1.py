#!/usr/bin/env python
# encoding: utf-8

import sys
import re

## DATA
filepath = "./input.txt"
# 9-10 m: mmmmnxmmmwm

## MAIN

pwlist = []
with open(filepath) as fp:
  for line in fp:
    pos1, pos2, char, pwd = re.match(r"(\d+)-(\d+) (\w): (\w+)", line).groups()
    pwlist.append((pos1,pos2,char,pwd))

passvalid = 0
for item in pwlist:
  charcount = item[3].count(item[2])
  if charcount >= int(item[0]) and charcount <= int(item[1]):
    passvalid = passvalid + 1

print(passvalid)