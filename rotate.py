import PIL.Image
import PIL.ImageOps
import numpy as np


def rotate(file):
    img = PIL.Image.open(file)
    img = PIL.ImageOps.exif_transpose(img)
    img = img.convert(mode='RGB')
    return np.array(img)