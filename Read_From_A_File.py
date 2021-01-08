#Reading from a file 

readMe = open('exampleWrite.txt','r').read()

#the 'r' means to read from a file

print(readMe)

readMe2 = open('exampleWrite.txt','r').readlines()
print(readMe2)
