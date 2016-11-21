text = ""

with open("input.txt","r") as textFile:
	text += textFile.read()

output_text = ""
for letter in text:


	value = ord(letter)
	if value >= 97 and value <= 122:
		output_text += chr(value)


print(output_text)

print(ord('a'))

print(ord('z'))
