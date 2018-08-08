from PIL import Image, ImageFilter

im = Image.open('BolsoSimpson.jpg') # Can be many different formats.
pix = im.load()
x = 1
y = 1
value = 0
print im.size  # Get the width and hight of the image for iterating over
print pix[x,y]  # Get the RGBA Value of the a pixel of an image

for i in range(im.width):
    for j in range(im.width):
        pix[i,j] = (2, 252, 6)

# pix[x,y] = value  # Set the RGBA Value of the image (tuple)
im.save('saida.png')  # Save the modified pixels as .png