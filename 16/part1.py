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

# load data
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

# compute error rate. skip my ticket.
error_rate = 0
for ticket in tickets[1:]:
  for field in ticket:
    if not isvalid(int(field)):
      error_rate += int(field)

console.print('error rate :', error_rate)