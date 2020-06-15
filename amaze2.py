from PIL import Image
from numpy import array
import numpy as np
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)
im_1 = Image.open('test_1.jpg')
image_file = im_1.convert('1') # convert image to black and white
ar = array(image_file)
C=ar.astype(np.int)
print(C)
new_im = Image.fromarray(ar)
new_im.save("numpy_altered_test_2.png")
