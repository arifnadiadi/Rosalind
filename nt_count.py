#!/usr/bin/python
temp = str(raw_input("Input: ")) #Ask user for string input
dic = {'A':0, 'C':0, 'G':0, 'T':0} #create empty dictionary to work in

#count letters in input string
for nt in temp:
    if nt in dic:
        dic[nt] += 1
        

#print values
print dic['A'],
print dic['C'],
print dic['G'],
print dic['T']