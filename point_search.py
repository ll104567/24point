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

def search(number):
    if check(number):
        try:
            s = []
            with open('point_lib/'+number+'.txt') as f:
                for i in f:
                    s.append(i.strip())
            return s
        except:
            return False

    else:
        print_help()

if __name__ == '__main__':

    if len(sys.argv) == 5:
        number = ''.join(sys.argv[1:])

    elif len(sys.argv) == 2:
        number = sys.argv[1]

    else:
        print_help()
    
    result = search(number)
    if result:
        for i in result:
            print(i)
    else:
        print('No answer')
