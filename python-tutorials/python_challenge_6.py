import zipfile

with zipfile.ZipFile('channel.zip','r') as zippedFile:
	list_of_names = zippedFile.namelist()
	dict_contents = {}
	print(list_of_names)
	counter = 0
	name = '90052.txt'
	answer = ''
	while counter < 5000:
		counter += 1
		input_text = zippedFile.read(name).decode('UTF-8')
		input_list = input_text.split()
		print('current nothing: {}  Input text: {}  next nothing: {}'.format(name, input_text, input_list[-1]))
		name = input_list[-1] + '.txt'

		answer += zippedFile.getinfo(name).comment.decode('UTF-8')
		print(answer)
		#input_number = int(input_list[-1])
		#dict_contents[name] = input_number

print(dict_contents)