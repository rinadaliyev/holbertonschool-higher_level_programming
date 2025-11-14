#!/usr/bin/python3
def uppercase(str):
    res = ""
    for i in str:
        if (97 <= ord(i) <= 122):
            i_up = chr(ord(i)-32)
            res += i_up
        else:
            res += i
    print("{}".format(res))
