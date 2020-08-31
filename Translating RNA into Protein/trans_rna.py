#!/usr/bin/python
#RNA translator
#Given n length RNA sequence, return corresponding protein sequence
import re #import regex

file = open(raw_input("File name: "), 'r') #user input of RNA seq
rna = file.read()
prot = open('protein_out.txt', 'w')
codons = re.findall('.{1,3}', rna) #split RNA seq into codon list
protein = '' #initial string to add protein letters

#dictionary of Protein keys to codon values
codes = {'F': ('UUU', 'UUC'), \
    'L': ('UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'), \
    'S': ('UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'), \
    'Y': ('UAU', 'UAC'), \
    ' ': ('UAA', 'UAG', 'UGA'), \
    'C': ('UGU', 'UGC'), \
    'W': ('UGG'), \
    'P': ('CCU', 'CCC', 'CCA', 'CCG'), \
    'H': ('CAU', 'CAC'), \
    'Q': ('CAA', 'CAG'), \
    'R': ('CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'), \
    'I': ('AUU', 'AUC', 'AUA'), \
    'M': ('AUG'), \
    'T': ('ACU', 'ACC', 'ACA', 'ACG'), \
    'N': ('AAU', 'AAC'), \
    'K': ('AAA', 'AAG'), \
    'V': ('GUU', 'GUC', 'GUA', 'GUG'), \
    'A': ('GCU', 'GCC', 'GCA', 'GCG'), \
    'D': ('GAU', 'GAC'), \
    'E': ('GAA', 'GAG'), \
    'G': ('GGU', 'GGC', 'GGA', 'GGG')}

#iterate through codon list
#for each codon, iterate through dictionary
#when match, add corresponding key to protein string
for codon in codons:
    for key, value in codes.items():
        if codon in value:
            protein = protein + key

prot.write(protein)
prot.close()
file.close()