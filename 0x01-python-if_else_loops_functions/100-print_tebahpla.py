#!/usr/bin/python3
for i in range(122, 96, -1):
    chr = i
    if i % 2 !=0:
        char = char - 32
    print("{:c}".format(char), end='')
