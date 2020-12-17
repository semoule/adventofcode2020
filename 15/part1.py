#!/usr/bin/env python
# encoding: utf-8

input = [18, 11, 9, 0, 5, 1]

# samples
#input = [0, 3, 6]  # 436
#input = [1, 3, 2]  # 1
#input = [2, 1, 3]  # 10
#input = [1, 2, 3]  # 27
#input = [2, 3, 1]  # 78
#input = [3, 2, 1]  # 438
#input = [3, 1, 2]  # 1836

saylist = []
turn = 0
while turn < 2020:
  if turn < len(input):
    #print('turn :', turn, 'last spoken :         say :', input[turn - 1])
    saylist.append(input[turn])
  else:
    #firstime
    if saylist.count(saylist[-1]) == 1:
      #print('turn :', turn, 'last spoken :', saylist[-1], '      say : 0')
      saylist.append(0)
    else:
      i = 0
      for said in reversed(saylist):
        if said == saylist[-1] and i != 0:
          #print('turn :', turn, 'last spoken :', saylist[-1], 'i :', i, 'say :', i)
          saylist.append(i)
          break
        i += 1
  turn += 1

print('number said on 2020th turn :',saylist[-1])