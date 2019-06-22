import numpy as np
import cv2

img = cv2.imread('pclub.png')
x, y, z = img.shape
i=0
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
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
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
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
