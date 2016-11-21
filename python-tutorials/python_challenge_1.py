text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
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
