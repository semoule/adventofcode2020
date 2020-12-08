#!/usr/bin/env python
# encoding: utf-8

## DATA
filepath = "./input.txt"

## FUNCTIONS
def getseatid(seat):
  seat = seat.replace('F', '0')
  seat = seat.replace('B', '1')
  seat = seat.replace('R', '1')
  seat = seat.replace('L', '0')
  return int(seat, 2)

## MAIN
seatlist = []
with open(filepath) as fp:
  for line in fp:
    seatlist.append(line.strip())

seatidlist = []
for seat in seatlist:
  seatid = getseatid(seat)
  seatidlist.append(seatid)

print('greatest seat id is :', max(seatidlist))