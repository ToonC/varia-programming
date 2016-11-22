from PIL import Image

with Image.open('wire.png') as im:
	print(im.getpixel((0,0)))		