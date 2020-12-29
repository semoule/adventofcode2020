#!/usr/bin/env python
# encoding: utf-8

import time
import re
from rich.console import Console
from rich.traceback import install
from rich.progress import track
install()
start_time = time.time()

## DATA
filepath = "./input.txt"

## FUNCTIONS
def isvalid(field):
  for rule in rules:
    if (field >= rule[1] and field <= rule[2]) or (field >= rule[3] and field <= rule[4]):
      return True
  return False

## MAIN
console = Console()

# step 1 : load data
rules = []
tickets = []
filesection = 0
with open(filepath) as fp:
  for line in fp:
    if not len(line.strip()):
      filesection += 1
      fp.readline()
    elif filesection == 0:
      # rules
      rulename, range1_min, range1_max, range2_min, range2_max = re.match(r"(.*): (\d+)-(\d+) or (\d+)-(\d+)", line).groups()
      rules.append((rulename, int(range1_min), int(range1_max), int(range2_min), int(range2_max)))
    elif filesection >= 1:
      # my ticket and then nearbytickets
      tickets.append(line.strip().split(','))

# step 2 : filter valid tickets only
valid_tickets = []
for ticket in tickets[1:]:
  valid = True
  for field in ticket:
    if not isvalid(int(field)):
      valid = False
      break
  if valid:
    valid_tickets.append(ticket)
#console.print('valid tickets :', valid_tickets)

# step 3.1 : create an empty invalid list of field for each rule
invalid_list = []
for rule in rules:
  invalid_list.append([])

# step 3.2 : construct invalid list : for each ticket and rule add invalid fields 
for ticket in valid_tickets:
  field_id = 0
  for field in ticket:
    rule_id = 0
    for rule in rules:
      if not ((int(field) >= rule[1] and int(field) <= rule[2]) or (int(field) >= rule[3] and int(field) <= rule[4])):
        invalid_list[rule_id].append(field_id)
      rule_id += 1
    field_id += 1

# just print invalid list
#i = 0
#for item in invalid_list:
#  console.print('%s invalid positions : %s' % (rules[i][0],sorted(item)))
#  i += 1

# step 4 : identify field position by elimination
field_position_list = []
field_found = []
field_list = [ i for i in range(0,len(rules)) ]
fields_remains_count = len(rules)

while fields_remains_count:
  i = 0
  for item in invalid_list:
    if len(item) == fields_remains_count - 1:
      # we found a candidate, get its position
      for x in field_list:
        if x not in item + field_found:
          pos = x
          break
      field_found.append(pos)
      field_position_list.append((rules[i][0], pos))
      fields_remains_count -= 1
    i += 1

# step 4 : compute result
console.print('My ticket :')
answer = 1
for field in field_position_list:
  if field[0][0:9] == 'departure':
    console.print(field[0], tickets[0][field[1]])
    answer *= int(tickets[0][field[1]])

print("multiplied together :", answer)