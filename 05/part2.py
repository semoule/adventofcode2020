#!/usr/bin/env python
# encoding: utf-8

## DATA
filepath = "./input.txt"

## FUNCTIONS
def getseatid(seat):
  seat = seat.replace('F', '0')
  seat = seat.replace('B', '1')
  seat = seat.replace('L', '0')
  seat = seat.replace('R', '1')
  return int(seat, 2)

def find_missing(lst): 
  return [x for x in range(lst[0], lst[-1] + 1) if x not in lst]

## MAIN
seatlist = []
with open(filepath) as fp:
  for line in fp:
    seatlist.append(line.strip())

seatidlist = []
for seat in seatlist:
  seatid = getseatid(seat)
  seatidlist.append(seatid)

print('Free seat :', find_missing(seatidlist)[0])