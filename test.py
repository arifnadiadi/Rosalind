#!/usr/bin/python
def gc_counter(seq):
    count = 0.0
    seq_len = (len(seq))
    for nt in seq: 
        if nt == 'G' or nt == 'C':
            count += 1
    gc_percent = (((count)/(seq_len))*100)
    return gc_percent


def count(seq):
    count = float(seq.count('C') + seq.count('G'))
    gc_percent = (((count)/len(seq))*100)
    return gc_percent

seq ='CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT'

print gc_counter(seq)
print count(seq)