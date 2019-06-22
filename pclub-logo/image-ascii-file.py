import numpy as np
import cv2

# create file object to write
file = open('ascii_logo.txt', 'w');

# create image object to get image data
img = cv2.imread('pclub.png')
# dimensions of the image
x, y, z = img.shape
# convert image to gray scale for better performance
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# define a theshold value between 0 to 255
thrsh = 170
# set pixel to either 0 or 255 compared to threshold
i=0
while i<x:
    j=0
    while j<y:
        z = int(img.item(i,j))
        if z > thrsh:
            img[i,j] = 255
        else :
            img[i,j] = 0
        j = j+1
    i = i+1
# write your data to text file
# pixel dimensions are > 400x400
# that's why we consider only one-third of the pixels
i=0
while i<x:
    j=0
    while j<y:
        if int(img.item(i,j)) == 255:
            file.write('1') # change to other ascii ;experiment
        else :
            file.write('0') # change to other ascii ;experiment
        j = j + 3
    i = i + 3
    file.write('\n')
# close the file and exit
file.close()
