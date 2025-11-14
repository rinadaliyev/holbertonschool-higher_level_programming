#!/usr/bin/python3
for i in range(10):
    for j in range(i+1, 10):
        num = i*10 + j
        if num == 89:
            print(num)
        else:
            print("{:02d}".format(num), end=", ")
