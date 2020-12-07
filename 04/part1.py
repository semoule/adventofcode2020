#!/usr/bin/env python
# encoding: utf-8

import re

## DATA
filepath = "./input.txt"

## FUNCTIONS
def isvalidpassport(document):
  validcount = 0
  for item in document:
    if item[0] == 'byr' or item[0] == 'iyr' or item[0] == 'eyr' or item[0] == 'hgt' or item[0] == 'hcl' or item[0] == 'ecl' or item[0] == 'pid' or item[0] == 'cid':
      validcount += 1
  if validcount == 8:
    return True
  else:
    return False

def isvalidnpc(document):
  validcount = 0
  for item in document:
    if item[0] == 'byr' or item[0] == 'iyr' or item[0] == 'eyr' or item[0] == 'hgt' or item[0] == 'hcl' or item[0] == 'ecl' or item[0] == 'pid':
      validcount += 1
  if validcount == 7:
    return True
  else:
    return False

## MAIN
# create data structure
passportlist = []
document = []
with open(filepath) as fp:
  for line in fp:
    if len(line.strip()) == 0:
      passportlist.append(document)
      document = []
      continue

    for elem in line.strip().split():
      key, val = re.match(r"(\w+):(.*)", elem).groups()
      document.append((key, val))

# analyze data
passportcount = 0
npccount = 0
for document in passportlist:
  if isvalidpassport(document):
    passportcount += 1
  elif isvalidnpc(document):
    npccount += 1

# results
print('valid passport :', passportcount, 'valid npc :', npccount, 'total valid :', passportcount + npccount)