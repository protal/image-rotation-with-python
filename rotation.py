import numpy
import matplotlib.pyplot as plt
from copy import deepcopy
from PIL import Image
from math import cos, sin

def rotaion(x,y,angle):
    PIPI = 3.14156
    angle = angle * PIPI / 180.0
    nx = x * cos(angle) - y * sin(angle)
    ny = x * sin(angle) + y * cos(angle)
    nx = int(nx)
    ny = int(ny)
    return [nx,ny]
    





img = Image.open('shapesAs4.png')
img = numpy.asarray(img)

# copy list not reference
rot90 = deepcopy(img)
rot270 = deepcopy(img)


for i in range(len(img)):
    for j in range(len(img[i])):
        r90 = rotaion(i,j,90)
        r270 = rotaion(i, j, 270)
        rot90[ r90[0] ][ r90[1] ] = img[i][j]
        rot270[ r270[0] ] [r270[1] ] = img[i][j]


plt.subplot(2, 2, 1)
plt.imshow(img)
plt.subplot(2, 2, 2)
plt.imshow(rot90)
plt.subplot(2, 2, 3)
plt.imshow(rot270)

plt.show()
