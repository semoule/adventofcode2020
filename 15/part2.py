#!/usr/bin/env python
# encoding: utf-8

import time
start_time = time.time()

## DATA
input = [18, 11, 9, 0, 5, 1]
#input = [0, 3, 6]  # 436
#maxturns = 10
#maxturns = 2020
maxturns = 30000000

numbers = {input[i]: (i,-1) for i in range(0, len(input))}
lastspoken = list(numbers.items())[-1][0]
turn = len(input) -1
print(turn, lastspoken, numbers)
turn += 1
printcounter = 0

while turn < maxturns:
  # firstime : if the lastposken number has before_last value False
  if numbers[lastspoken][1] == -1:
    lastspoken = 0
    numbers[0] = (turn, numbers[0][0])
  else:
    numbersaid = numbers[lastspoken][0] - numbers[lastspoken][1]
    if numbersaid not in numbers:
      numbers[numbersaid] = (turn, -1)
    else:
      numbers[numbersaid] = (turn, numbers[numbersaid][0])
    lastspoken = numbersaid

  if (printcounter == 1000000):
    print('.')
    printcounter = 0
  printcounter += 1

  turn += 1

print('number said on 30000000th turn :', lastspoken)
print('duration :', (time.time() - start_time), 'seconds')
