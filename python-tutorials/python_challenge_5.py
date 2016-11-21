import pickle


with open("banner.p","rb") as input_file:
	text = pickle.load( open("banner.p","rb"))

for item in text:
	for each_item in item:
		for i in range(int(each_item[1])):
			print(each_item[0], end='')
	print()