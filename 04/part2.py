#!/usr/bin/env python
# encoding: utf-8

import re

## DATA
filepath = "./input.txt"

## FUNCTIONS
def isvalid(document):
  validcount = 0
  for item in document:
    if item[0] == 'byr':
      if item[1].isdecimal() and len(item[1]) == 4:
        if int(item[1]) >= 1920 and int(item[1]) <= 2002:
          validcount += 1
    elif item[0] == 'iyr':
      if item[1].isdecimal() and len(item[1]) == 4:
        if int(item[1]) >= 2010 and int(item[1]) <= 2020:
          validcount += 1
    elif item[0] == 'eyr':
      if item[1].isdecimal() and len(item[1]) == 4:
        if int(item[1]) >= 2020 and int(item[1]) <= 2030:
          validcount += 1
    elif item[0] == 'hgt':
      if item[1][-2:] == 'in':
        if item[1][:-2].isdecimal():
          if int(item[1][:-2]) >= 59 and int(item[1][:-2]) <= 76:
            validcount += 1
      elif item[1][-2:] == 'cm':
        if item[1][:-2].isdecimal():
          if int(item[1][:-2]) >= 150 and int(item[1][:-2]) <= 193:
            validcount += 1
    elif item[0] == 'hcl':
      if re.match(r"^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$", item[1]):
        validcount += 1
    elif item[0] == 'ecl':
      if item[1] == 'amb' or item[1] == 'blu' or item[1] == 'brn' or item[1] == 'gry' or item[1] == 'grn' or item[1] == 'hzl' or item[1] == 'oth':
        validcount += 1
    elif item[0] == 'pid':
      if item[1].isdecimal() and len(item[1]) == 9:
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
  if isvalid(document):
    passportcount += 1

# results
print('valid document :', passportcount)