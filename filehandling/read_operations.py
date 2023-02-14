#for writing

file = open('ravi.txt','w')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()

#for reading

file = open('ravi.txt','r')
print(file.read())