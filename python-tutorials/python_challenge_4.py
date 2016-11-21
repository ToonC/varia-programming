from urllib import request
from lxml import html


with request.urlopen('http://python.org/') as response:
   page = html.fromstring(response.read())

   print(page)