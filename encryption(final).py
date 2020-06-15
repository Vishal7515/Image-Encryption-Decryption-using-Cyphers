from PIL import Image, ImageDraw, ImageFilter, ImageOps                         #imported the required objects from the Python Image Library
import sys                                                                      #imported sys so zas to view the entire numpy array
import numpy as np
from random import randint
np.seterr(divide='ignore', invalid='ignore')
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

data_image = Image.open('thanos.jpg')
ar1 = np.array(data_image)
print(ar1)

size_dat = min(data_image.size)
print(size_dat)
key = random_with_N_digits(size_dat)
key = str(key)

key_image = Image.open('test_3.jpg')
ar2 = np.array(key_image)
maink = np.sum(ar2,axis=0)#/size_dat
maink = maink.astype('uint8')
print(maink)
print(ar2)
ar3 = ar1 - maink
print(ar3)

im1 = Image.fromarray(ar3)
im1.save('inotded.jpg')
