from urllib import request
from lxml import html
import requests
import re

uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={:d}"
nothing = 63579

r = requests.get(uri.format(nothing))

while True:
	r = requests.get(uri.format(nothing))

	if r.status_code == 200:

		print(r.text)
		p = re.compile("the next nothing is \d+")
		found = p.findall(r.text)[0]
		found_number = found.split()[-1]
		nothing = int(found_number)
		print(str(nothing))
	else:
		break