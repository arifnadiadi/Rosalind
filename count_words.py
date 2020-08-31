#!/usr/bin/python
temp = str(raw_input("Input: ")) #Ask user for string input
dic = {} #create empty dictionary to work in

#count words in input string
for word in temp.split(' '):
    if word in dic:
        dic[word] += 1
        #return dic
    else:
        dic[word] = 1
        #return dic

#print dictionary
for key, value in dic.items():
    print key,
    print value