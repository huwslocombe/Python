#Writing to a file

writeMe = 'Example text' #variable

saveFile = open('exampleWrite.txt','w')#open = built in function

#the 'w' means write to file

saveFile.write(writeMe)
saveFile.close()
