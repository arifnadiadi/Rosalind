#!/usr/bin/python
## Given seq 's' find locations of motif 't'
## return each starting location of motif in sequence

# Open input file and store first line as seq and second line as motif, removing endline chararcters
with open(('rosalind_subs.txt')) as file:
    seq = file.readline().rstrip()
    motif = file.readline().rstrip()

print seq
print motif

locations = [] # list for motif locations
loc = 0 # starting location for find method
while True: # loop to keep searching for motif after each occurance
    if seq.find(motif, loc) != -1: # only search if motif is found
        locations.append(seq.find(motif, loc) + 1) # add index location + 1 for 1-based numbering
        loc = seq.find(motif, loc) + 1 # update starting search location to next character
    else: # break loop if motif not found
        break

# print results
if not locations: # if list is empty
    print "No matches found."
else:  #print locations separated by spaces
    for x in range(len(locations)): 
        print locations[x],
