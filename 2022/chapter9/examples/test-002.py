from PIL import Image
import numpy as np
im = np.array(Image.open("fcity.jpg"))
print(im)
print(im.shape, im.dtype)

im = np.array(Image.open("fcity.jpg").convert('L'))
print(im)
print(im.shape, im.dtype)