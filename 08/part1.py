#!/usr/bin/env python
# encoding: utf-8

## DATA
filepath = "./input.txt"

## MAIN
#create data structure
inslist = []
with open(filepath) as fp:
  for line in fp:
    ins = line[0:3]
    sign = line[4]
    val = line[5:].strip()
    inslist.append((ins, sign, val))

# run code
acc = 0
offset = 0
insvisitedlist = []
while True:
  if offset in insvisitedlist:
    break
  insvisitedlist.append(offset)
  if inslist[offset][0] == 'nop':
    offset += 1
  elif inslist[offset][0] == 'acc':
    if inslist[offset][1] == '+':
      acc += int(inslist[offset][2])
    else:
      acc -= int(inslist[offset][2])
    offset += 1
  elif inslist[offset][0] == 'jmp':
    if inslist[offset][1] == '+':
      offset += int(inslist[offset][2])
    else:
      offset -= int(inslist[offset][2])

print('Accumulator value before infinite loop :',acc)