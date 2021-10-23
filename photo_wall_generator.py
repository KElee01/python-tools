# -*- coding: UTF-8 -*-
import os
from PIL import Image
from PIL import ImageFile
# create a file name list
photo_path = "COPY PATH OF PHOTOS HERE (Finished with '/')"
image_list = os.listdir(photo_path)
print(image_list)
# lines and rows
lines = 5
rows = 5
# image' height and width
image_width = 1200
image_height = 1200
# create a image wall
image_wall = Image.new("RGB", (image_width*lines, image_height*raws))
# create coordinate
x = 0
y = 0
# range should be fit to the image wall lines
for i in range(0, lines*rows-1):
    # read the images
    image = Image.open(phto_path + image_list[i])
    # read the size of images
    (a, b) = image.size
    # create a box for crop
    box = (a/2-b/2, 0, a/2+b/2, b)
    # crop the images
    image = image.crop(box)
    # resize the images
    image = image.resize((image_width, image_height))
    # insert the image
    image_wall.paste(image, (x*image_width, y*image_height))
    # when I want to insert by line
    x += 1
    # image_wall.show()
    if x == lines:
        x = 0
        y += 1
# save the image wall
image_wall.save("%swall.png" % photo_path)
print('Complete!')