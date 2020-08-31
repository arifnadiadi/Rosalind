#!/usr/bin/python
"""
Reverse Complement program. Returns the reverse complement of a valid string.
"""

#Add functions
def is_valid(seq):
    """Returns False if invalid character present"""
    valid_base = ['A', 'T', 'C', 'G']
    for i in seq:
        if i not in valid_base:
            return False
    return True

def complement(seq):
    """Returns the complement of input sequence"""
    complement_dict = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
    seq_list = list(seq)
    seq_list = [complement_dict[base] for base in seq_list]
    return ''.join(seq_list)

def reverse_complement(seq):
    """"Returns a reverse complement of input sequence"""
    seq = complement(seq[::-1])
    return seq


def main():
    print('**********************Reverse Complement Program**********************')
    # Prompt user here
    sequence = raw_input("Enter a nucleotide sequence: ").upper()
    
    if is_valid(sequence) == True:
        print "Reverse Complement: " + reverse_complement(sequence)
    else:
        print "Invalid Sequence"
    print('*' * 70)



if __name__ == '__main__':
    main()

""""Will do the same thing, but inefficiently, as it reads through the sequence multiple times."""
##st = "AAAACCCGGT"
##st = st.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
##print st