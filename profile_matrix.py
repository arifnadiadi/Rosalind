#!/usr/bin/python
# Given fasta of 10 sequences, Return consensus string and profile matrix.

# function to parse fasta, create tuples (id, seq)
def read_fasta(fasta):
        id, seq = None, [] # creates id and seq variables, nothing in id and list in seq
        for line in fasta:
            line = line.rstrip() # remove endline/newline characters
            if line.startswith(">"): # lines that start with '>' are id
                if id: yield (id, ''.join(seq))
                id, seq = line, []
            else:
                seq.append(line)
        if id: yield (id, ''.join(seq))

with open('profile.txt') as fasta:
    for id, seq in read_fasta(fasta):