## writing text to file

text = "this will be written to the file"


saveFile = open("textfile.txt", "w")
saveFile.write(text)
saveFile.close()


##text to be added to the file
appendMe = "New info for file"

##appending more text to the file
appendFile = open("textfile.txt", "a")
appendFile.write('\n')
appendFile.write(appendMe)
appendFile.close()

##reading the file
readMe = open("textfile.txt", "r").readlines()
print(readMe)
