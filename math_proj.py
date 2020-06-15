from PIL import Image, ImageDraw, ImageFilter
from numpy import array
import sys
import numpy
import os
import glob


def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))
def crop_max_square(pil_img):
    return crop_center(pil_img, min(pil_img.size), min(pil_img.size))


im = Image.open('test_1.jpg')
im_thumb = crop_max_square(im)
im_thumb.save('max_square.jpg', quality=95)

numpy.set_printoptions(threshold=sys.maxsize)
im_1 = Image.open('max_square.jpg')
image_file = im_1.convert('1') # convert image to black and white
ar = array(image_file)
original=ar.astype(numpy.int)
originaT = original.T
key = numpy.linalg.inv(originaT)

encrypted = numpy.dot(original,originaT)

decrypted = numpy.dot(encrypted,key)


im1 = Image.fromarray((encrypted * 255).astype(numpy.uint8))
im2 = Image.fromarray((decrypted * 255).astype(numpy.uint8))
im1.save("nencrypted.png")
im2.save('decrypted.png')
