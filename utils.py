# -*- coding: utf-8 -*-

import numpy as np
from PIL import Image
from random import randint

# img: an Image object
# height: the height of the img
# width: the width of the img
# h1, w1: the height and width of the pic to be saved
def get_random_pics(img, h1, w1, num):
    (width, height) = img.size
    for i in range(num):
        h_start = randint(0, height - h1 - 1)
        w_start = randint(0, width - w1 -1)
        cropped_img = img.crop((w_start, h_start, w_start + w1, h_start + h1))
        # cropped_img.save("D:\\projects\\python\\compression\\cropped\\cropped_img%d.jpg" % i)
        yield (cropped_img)

# img: an Image object
# return: an ndarray num * h1 * w1 * 3
def get_batch_pics(img, h1, w1, num):
    batch_pics = np.zeros((num, h1, w1, 3))
    batch_num = 0
    for pic in get_random_pics(img, h1, w1, num):
        # pic: (h1, w1, 3)
        batch_pics[batch_num, :, :, :] = np.asarray(pic)
        batch_num += 1
    return batch_pics

# img: an Image object
def get_all_pics(img, h1, w1):
    (width, height) = img.size
    for i in range(0, height, h1):
        for j in range(0, width, w1):
            cropped_img = img.crop((j, i, j + w1, i + h1))
            yield (i, j, cropped_img)

