from PIL import Image, ImageFilter

im = Image.open('oxygen.png')
rgb_img = im.convert('RGB')
width, height = rgb_img.size
y = x = 0
correct_y = 0
while y < height:
	r, g, b = rgb_img.getpixel((x,y))
	if r == g == b:
		correct_y = y
		y = height
	y += 1
previous_value = 0
counter = 0
output = ''
for x in range(0,width, 7):
	r, g, b = rgb_img.getpixel((x,correct_y))
	if r == g == b:
		output += chr(r)
print(output)

next_input = [105, 110, 116, 101, 103, 114, 105, 116, 121]
next_output = ''
for x in next_input:
	next_output += chr(x)
print(next_output)
