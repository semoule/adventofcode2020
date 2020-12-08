#!/usr/bin/env python
# encoding: utf-8

## DATA
filepath = "./input.txt"

## MAIN
# create data structure
grouplist = []
answers = ''
peoplecount = 0
with open(filepath) as fp:
  for line in fp:
    if len(line.strip()) != 0:
      answers += line.strip()
      peoplecount += 1
    else:
      grouplist.append((peoplecount, answers))
      answers = ''
      peoplecount = 0

total = 0
for answers in grouplist:
  uniquechars = set(answers[1])
  for char in uniquechars:
    if answers[1].count(char) == answers[0]:
      total += 1

print('Total answers "yes" by everyone in a group is :', total)