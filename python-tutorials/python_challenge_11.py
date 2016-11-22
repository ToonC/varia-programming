from PIL import Image, ImageDraw

original = Image.open('cave.jpg')


half_tuple = tuple([int(x / 2) for x in original.size])
im_even = Image.new(original.mode, original.size)
im_odd = Image.new(original.mode, original.size)

width, height = original.size



for x in range(width):
	for y in range(height):
		if (x+y) % 2 == 0:
			im_even.putpixel((x//2,y//2),original.getpixel((x,y)))
		else:
			im_odd.putpixel((x//2,y//2),original.getpixel((x,y)))
im_even.save('output1.jpg','JPEG')
im_odd.save('output2.jpg','JPEG')
			

