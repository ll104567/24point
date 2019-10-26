#!/usr/bin/python3

import sys
from point import point

def print_help():

    print('Usage:python3 {} 4 4 6 8/4468'.format(sys.argv[0]))
    sys.exit(1)

def check(number):

    if len(number) != 4:
        return False
    for i in number:
        try:
            i = int(i)
        except:
            return False
    return True

if len(sys.argv) == 5:
    number = sys.argv[1:]

elif len(sys.argv) == 2:
    number = list(sys.argv[1])

else:
    print_help()

if check(number):
    point(number)
else:
    print_help()




