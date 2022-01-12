# Write a function to remove all the red from an image.

from PIL import Image

# def redRemoval(image):
#     """Sets the R value of every pixel in an image to 0"""
#     for row in range(image.size[1]):
#         for col in range(image.size[0]):
#             r,g,b = image.getpixel( (col , row) )
#             image.setpixel(0 , g , b)


img = Image.open("luther.jpg")

r,g,b = img.getpixel( (50 , 50) )

img.putpixel([50 , 50] , [0 , 255 , 0])
img.show()

# print(r,g,b)

# Going to put the image processing stuff on hold. Pillow is asking some concepts I don't quite get yet,
# but I'd rather learn them and come back to this than use the simplified module in the book.