from PIL import Image, ImageDraw, ImageFilter, ImageOps                                #imported the required objects from the Python Image Library
import sys                                                                      #imported sys so zas to view the entire numpy array
import numpy as np
import cv2
from matplotlib import pyplot as plt
import PyDIP as dip

key_image = Image.open('test_3.jpg')
ar2 = np.array(key_image)
maink = np.sum(ar2,axis=0)#/size_dat
maink = maink.astype('uint8')

encrypted_image = Image.open('inotded.jpg')
ar1 = np.array(encrypted_image)

ar3 = ar1 + maink

im1 = Image.fromarray((ar3))#.astype(np.uint8))
im1.save('ided.jpg')
