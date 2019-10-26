#!/usr/bin/python

from point import point


s = []
for i in range(1111,9999):
    s.append(str(i))


for i in s:
    result = point(list(i))
    with open(i+'.txt','w') as f:
        for j in result:
            f.write(j+'\n')
