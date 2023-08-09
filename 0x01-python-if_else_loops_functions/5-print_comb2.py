#!/usr/bin/python3

for i in range(0, 100):
    if i < 99:
        print('{}, '.format("%02d" % i), end="")
    else:
        print(i)
