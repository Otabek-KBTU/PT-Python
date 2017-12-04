from PIL import Image, ImageDraw
im = Image.open("passport.jpg")
rgb_im = im.convert('RGB')
size = im.size
new_im = im.resize((80,80))
# size = new_im.size
new_im.save('passport1.jpg')
# print(size)
pix = rgb_im.load()
r1 = 253  
g1 = 201
b1 = 187
