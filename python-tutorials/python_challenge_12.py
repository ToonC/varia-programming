with open("evil2.gfx","rb") as input_file:
	data = input_file.read()

for i in range(5):
	with open("{}.jpg".format(i),'wb') as output_file:
		output_file.write(data[i::5])

