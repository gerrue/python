#!/usr/bin/python

import sys

for i in range(1, 1000):
  if i%3==0:
        sys.stdout.write('Fizz ')
  if i%5==0:
        sys.stdout.write('Buzz ')
  if (i%5<>0 and i%3<>0 and i%7<>0 and i%9<>0):
        print i,
  print
