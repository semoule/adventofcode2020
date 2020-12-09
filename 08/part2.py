#!/usr/bin/env python
# encoding: utf-8

## DATA
filepath = "./input.txt"

## FUNCTIONS
def trycode(inslist):
  acc = 0
  offset = 0
  insvisitedlist = []
  success = False
  while True:
    # exit conditions
    if offset in insvisitedlist:
      # infinite loop detected
      break
    if offset == len(inslist):
      success = True
      break

    # execute code
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

  return success, acc

## MAIN
#create data structure
inslist = []
with open(filepath) as fp:
  for line in fp:
    ins = line[0:3]
    sign = line[4]
    val = line[5:].strip()
    inslist.append((ins, sign, val))

# try code change
index = 0
acc = 0
for ins in inslist:
  if ins[0] == 'nop':
    newlist = inslist.copy()
    newtuple = ('jmp', ins[1], ins[2])
    newlist[index] = newtuple
    success, acc = trycode(newlist)
    if success:
      break
  if ins[0] == 'jmp':
    newlist = inslist.copy()
    newtuple = ('nop', ins[1], ins[2])
    newlist[index] = newtuple
    success, acc = trycode(newlist)
    if success:
      break
  index += 1

print('Accumulator value with a fixed code :',acc)