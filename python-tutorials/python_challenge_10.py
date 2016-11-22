def look_and_say(length, previous_string='1'):
	count_couples = get_counts(previous_string)
	new_string = make_new_string(count_couples)
	length -= 1
	if length > 0:
		return look_and_say(length, new_string)
	else:
		return new_string

def get_counts(input_string):
	current_letter = ''
	couples = []
	counter = 0
	for letter in input_string:
		if letter == current_letter:
			counter += 1
		else:
			if counter > 0:
				couples.append((counter, current_letter))
				counter = 0
			current_letter = letter
			counter = 1
	if counter > 0:
		couples.append((counter, current_letter))
	return couples

def make_new_string(couples_list):
	output = ''

	for couple in couples_list:
		output += str(couple[0])+couple[1]
	return output

print(len(look_and_say(30)))