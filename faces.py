from face import Image, ImageDraw, ImageFont
im = Image.open("face1.jpeg")
size = im.size
rgb_im = im.convert('RGB').resize((100, 100))
pix = rgb_im.load()
size = rgb_im.size
h, w = rgb_im.size
skins = [(226, 161, 131), (233, 202, 184), (194, 152, 112), (222, 182, 147), (195, 169, 146)]
s = 0
wp = 0
for y in range(0, size[1]):
	for x in range(0, size[0]):
		r, g, b = pix[x, y]
		if (r, g, b) == (244, 244, 244):
			wp = wp + 1
			continue
		for r1, g1, b1 in skins:
			r, g, b = pix[x, y]
			k = 0
			if abs(r1 - r) < 20:
				k = k + 1
			if abs(g1 - g) < 20:
				k = k + 1
			if abs(b1 - b) < 20:
				k = k + 1
			if k == 3:
				s = s + 1
				pix[x, y] = (0, 255, 0)
				break
total = h * w
total = total - wp
print(s/total*100)
im.convert('L').resize((100, 100)).save("face02-ii.jpeg")