a = raw_input('File: ')
with open('out2.txt', 'w+') as b:
    with open(a, 'r') as f:
        b.write(''.join(f.readlines()[1::2]) + '\n')
    