#!/usr/bin/env python
# encoding: utf-8

## DATA
filepath = "./input.txt"

## MAIN
# create data structure
grouplist = []
answers = ''
with open(filepath) as fp:
  for line in fp:
    if len(line.strip()) != 0:
      answers += line.strip()
    else:
      grouplist.append(answers)
      answers = ''

total = 0
for answers in grouplist:
  s=set(answers)
  total += len(s)

print('Total answers "yes" at least once per group is :',total)