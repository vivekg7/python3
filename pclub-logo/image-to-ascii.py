import numpy as np
import cv2

# create image object with your image to edit
img = cv2.imread('pclub.png')
# get image dimensions
x, y, z = img.shape
# convert image to gray scale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# set pixels to 0 or 255 compared to a threshold value
i=0
while i<x:
    j=0
    while j<y:
        z = int(img.item(i,j))
        if z > 170:
            img[i,j] = 255
        else :
            img[i,j] = 0
        j = j+1
    i = i+1
# show your new creation on screen
# wait for a key to be pressed
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# write data directly to standard output
# this can be piped into a file if need
# image may have dimensions more than 400x400 pixels
# that's why we increment 3 pixels at a time
# change this if image dimensions are different
i=0
while i<x:
    j=0
    while j<y:
        if int(img.item(i,j)) == 255:
            print('#',end = '')
        else :
            print('.',end = '')
        j = j + 3
    i = i + 3
    print('\n',end = '')
