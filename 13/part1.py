#!/usr/bin/env python
# encoding: utf-8

## DATA
filepath = "./input.txt"

## MAIN
# load data
bus_list = []
with open(filepath) as fp:
  timestamp = int(fp.readline().strip())
  busline = fp.readline().strip()
  for bus in busline.split(','):
    if bus != 'x':
      bus_list.append(bus)

# part1
line_list = []
for bus in bus_list:
  line = []
  timeline = 0
  line.append(timeline)
  while (timeline <= timestamp):
    timeline += int(bus)
    line.append(timeline)
  line_list.append(line)

i = 0
timewait = line_list[i][-1] - timestamp
bestbus = i
for line in line_list:
  if line[-1] - timestamp < timewait:
    bestbus = i  
  i += 1

print('Time to wait :',(line_list[bestbus][-1] - timestamp) * int(bus_list[bestbus]))