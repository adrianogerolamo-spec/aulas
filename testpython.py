#!/usr/bin/env python3
import sys
arg = int(sys.argv[1])
#arg = input("input a number: ")
#arg = int(arg)
if arg == 0:
    print("zero")
elif arg > 0:
    print("positive")
    if arg < 50:
        print("menor que 50")
    if arg%2 == 0:
        print("o numero e par")
    else:
        print("o numero e impar")
else:
    print("negative")
