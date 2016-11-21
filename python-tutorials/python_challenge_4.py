from urllib import request
from lxml import html

uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={:d}"
nothing = 12345


with request.urlopen(uri.format(nothing)) as response:
   page = html.fromstring(response.read())
   
   print(uri.format(nothing))
   print(response)
   print(page)