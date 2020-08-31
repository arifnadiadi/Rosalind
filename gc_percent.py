#!/usr/bin/python
#Calculate GC percentage
#Given fasta format file with up to 10 sequences, return ID with highest GC content, including GC%


##FUNCTIONS

#function to parse fasta, create tuples (id, seq)
def read_fasta(fasta):
        id, seq = None, [] #creates id and seq variables, nothing in id and list in seq
        for line in fasta:
            line = line.rstrip() #remove endline/newline characters
            if line.startswith(">"): #lines that start with '>' are id
                if id: yield (id, ''.join(seq))
                id, seq = line, []
            else:
                seq.append(line)
        if id: yield (id, ''.join(seq))

#calculate gc percentage for input sequence
def gc_counter(seq):
    count = 0.0 #must be float or gc percent rounds to zero
    for nt in seq: #iterates through seq adding 1 to count if equal to 'g' or 'c'
        if nt == 'G' or nt == 'C': 
            count += 1
    ##count = seq.count('C') + seq.count('G') , counts G and C without for loop
    gc_percent = (count/len(seq))*100 #calculates percent of nt that are G/C in sequence
    return gc_percent

#gives key with max value in dictionary
def max_value(dic):    
     v=list(dic.values()) #makes list of values in dictionary
     return list(dic.keys())[v.index(max(v))] #returns list of keys that have the max value, can return more than one key 

##READ FASTA FILE AND RETURN MAX GC ID AND PERCENT

#dictionary of id:gc% to be filled
gc_content = {}

#open input fasta file and fill gc_content
with open((raw_input("Fasta File: "))) as fasta:
    for id, seq in read_fasta(fasta): #iterate through tuples created by read_fasta
        gc_content[id] = gc_counter(seq) #fill gc_content dictionary with id as key and gc% as value

#print ID of sequence with max GC content followed by its GC percentage
print max_value(gc_content)
print gc_content[max_value(gc_content)]        
