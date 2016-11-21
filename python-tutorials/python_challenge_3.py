from re import findall

text = ""

with open("input.txt","r") as textFile:
	text += textFile.read()


found = findall( "[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]", text)

if not found == None:
	print("Found it!")
	print(str(found))