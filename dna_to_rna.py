#!/usr/bin/python
a = raw_input("In: ")
temp = []
for i in a:
    if i == 'T':
        temp.append('U')
    else:
        temp.append(i)

print ''.join(temp)