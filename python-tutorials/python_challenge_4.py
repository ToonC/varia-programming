from urllib import request

uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%d"
nothing = 12345

response = request.urlopen(uri % nothing)

print(str(response))