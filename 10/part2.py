#!/usr/bin/env python
# encoding: utf-8

## DATA
filepath = "./input.txt"

## FUNCTIONS
def compat(source, adapter):
  if adapter - source < 4 and adapter - source > 0:
    return adapter - source
  return False

## MAIN
numlist = []
with open(filepath) as fp:
  for line in fp:
    numlist.append(int(line))

# add the source
numlist.append(0)

# sort the list
slist = sorted(numlist)

i = 0
jolt1 = 0
jolt2 = 0
jolt3 = 0
for s in slist[0:len(slist) - 1]:
  r = compat(s, slist[i + 1])
  if not r:
    print('ERROR : source :', s, 'adapter : ', slist[i + 1])
    break
  elif r == 1:
    jolt1 += 1
  elif r == 2:
    jolt2 += 1
  elif r == 3:
    jolt3 += 1
  i += 1

# our device has a +3 jolt bonus
jolt3 += 1

print('jolt1 : ', jolt1, 'jolt2 : ', jolt2, 'jolt3 : ', jolt3, 'answer is : ', jolt1 * jolt3)