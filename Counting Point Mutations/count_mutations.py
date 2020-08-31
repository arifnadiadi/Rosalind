#!/usr/bin/python
import itertools
#user inputs string of nt, stored as list
ref = str(raw_input("Reference: "))
aln = str(raw_input("Sequence: "))
#counting variables
count = 0 #for loop count
mutations = 0 #total differences

#iterate through each nt to check if they differ
#for i in aln:
 #   if i != ref[count]:
  #      mutations += 1
   # count += 1

#print mutations

#rosalind solution, pairs lists together to iterate through, works on strings too
print sum(a != b for a, b in itertools.izip(ref, aln))