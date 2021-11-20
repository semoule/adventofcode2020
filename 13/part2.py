#!/usr/bin/env python
# encoding: utf-8

## DATA
filepath = "./short.txt"

## MAIN
# load data
bus_list = []
line_list = []
with open(filepath) as fp:
  fp.readline()
  i = 0
  busline = fp.readline().strip()
  for bus in busline.split(','):
    if bus != 'x':
      bus_list.append((bus, i))
      line_list.append(0)
    i += 1

# part1
line_list = []
for bus in bus_list:
  line = []
  timeline = 0
  line.append(timeline)
  while True:
    timeline += int(bus)
    line.append(timeline)
  line_list.append(line)


print(line_list)