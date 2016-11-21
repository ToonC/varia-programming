text = "http://www.pythonchallenge.com/pc/def/map.html"
output_text = ""
for letter in text:


	value = ord(letter)
	if value >= 97 and value <= 122:
		value += 2
		if value > 122:
			value -= 26
		output_text += chr(value)
	else:
		output_text += letter

translation_table = text.maketrans('abcdefghijklmnopqrstuvwxyz','cdefghijklmnopqrstuvwxyzab')
second_output_text = text.translate(translation_table)

print(second_output_text)

print(output_text)

print(ord('a'))

print(ord('z'))
