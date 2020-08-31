a = raw_input("File name: ") #user inputs file to read
f = open(a, 'r') #python opens user input file
b = open('output.txt', 'w+') #create new file to write into

f2 = f.readlines() #read input file into list
count = 1 #create count variable for loop

#loop prints item in list if count is even
for i in f2:
    if count % 2 == 0:
        b.write(str(i) + '\n') 
    count += 1 
    
print b.read() #print out written file

#close files
f.close()
b.close()
