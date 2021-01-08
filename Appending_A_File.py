#Appending a file

appendMe = 'Hello there!'

saveFile = open('exampleWrite.txt','a')

#the 'a' means to append a file

saveFile.write('\n')
saveFile.write(appendMe)
saveFile.close()
