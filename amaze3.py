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


im = Image.open('thanos.jpg')
im_key = Image.open('test_3.jpg')
im_thumb_key = crop_max_square(im_key)
im_thumb_key.save('key_square.jpg', quality=99)
im_thumb = crop_max_square(im)
im_thumb.save('data_square.jpg', quality=99)


numpy.set_printoptions(threshold=sys.maxsize)
im_1 = Image.open('data_square.jpg')
image_file1 = im_1.convert('1')
im_2 = Image.open('key_square.jpg')
image_file2 = im_2.convert('1')

ar1 = array(image_file1)
ar2 = array(image_file2)

original=ar1.astype(numpy.int)
key1=ar2.astype(numpy.int)
key2 = key1[0]

originaT = original.T
key3 = abs(originaT-key2)

#b = numpy.where(originaT==0,1,0)
#originaT[originaT == 0] = 1
#originaT[originaT == 1] = 0
#print(originaT)
key_original = numpy.linalg.inv(originaT)
key_modified = numpy.linalg.inv(key3)


encrypted = numpy.dot(original,key3)

decrypted = numpy.dot(encrypted,key_modified)


im1 = Image.fromarray((encrypted * 255).astype(numpy.uint8))
im2 = Image.fromarray((decrypted * 255).astype(numpy.uint8))
im1.save("nencrypted.png")
im2.save('decrypted.png')
