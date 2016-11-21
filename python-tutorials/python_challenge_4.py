from urllib import request
from lxml import html
import requests
import re

uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={:d}"
nothing = 12345

r = requests.get(uri.format(nothing))

while True:
	r = requests.get(uri.format(nothing))

	if r.status_code == 200:
		p = re.compile("\d+")
		found = p.findall(r.text)[0]
		print(str(found))
		nothing = int(found)
		print(str(nothing))
		print(r.text)
	else:
		break