# -*- coding: utf-8 -*-
"""
Created on Thu May 17 09:31:42 2018

@author: Lenovo
"""
import numpy as np
from PIL import Image
from random import randint

# return a n * 3 matrix
def get_a_frame(filename, height, width, frameId):
    y = bytes()
    u = bytes()
    v = bytes()
    with open(filename, "rb") as f:
        f.seek(height * width * 3 * (frameId - 1))
        y = f.read(height * width)
        u = f.read(height * width)
        v = f.read(height * width)
    y = list(y)
    u = list(u)
    v = list(v)
    y = np.asarray(y)
    u = np.asarray(u)
    v = np.asarray(v)
    return np.vstack([y, u, v]).T

# return a n * 3 matrix
def get_all_frames(filename, height, width, num_frames):
    y = bytes()
    u = bytes()
    v = bytes()
    with open(filename, "rb") as f:
        for i in range(num_frames):
            y = f.read(height * width)
            u = f.read(height * width)
            v = f.read(height * width)
            y = list(y)
            u = list(u)
            v = list(v)
            y = np.asarray(y)
            u = np.asarray(u)
            v = np.asarray(v)
            yield np.vstack([y, u, v]).T, i

#ref: https://www.vocal.com/video/rgb-and-yuv-color-space-conversion/
# return a n * 3 matrix
def yuv_to_rgb(yuv_frame):
    rgb_frame = np.copy(yuv_frame)
    v1 = [1.164, 0, 1.596]
    v2 = [1.164, -0.391, -0.813]
    v3 = [1.164, 2.018, 0]    
    mat1 = np.array([v1, v2, v3])
    mat1 = mat1.T
    v4 = np.array([[16, 128, 128]], dtype="uint8")
    rgb_frame -= v4
    rgb_frame = np.clip(np.matmul(rgb_frame, mat1), 0, 255)
    return np.uint8(rgb_frame.reshape(yuv_frame.shape))

# return a n*3 matrix
def rgb_to_yuv(rgb_frame):
    yuv_frame = np.copy(rgb_frame)
    v1 = [0.257, 0.504, 0.098]
    v2 = [-0.148, -0.291, 0.439]
    v3 = [0.439, -0.368, 0.071]    
    mat1 = np.array([v1, v2, v3])
    mat1 = mat1.T
    v4 = np.array([[16, 128, 128]], dtype="uint8")
    yuv_frame = np.matmul(yuv_frame, mat1) + v4
    yuv_frame[:, 0] = np.clip(yuv_frame[:, 0], 16, 235)
    yuv_frame[:, 1] = np.clip(yuv_frame[:, 1], 16, 240)
    yuv_frame[:, 2] = np.clip(yuv_frame[:, 2], 16, 240)    
    return np.uint8(yuv_frame.reshape(rgb_frame.shape))

# img: an Image object
# height: the height of the img
# width: the width of the img
# h1, w1: the height and width of the pic to be saved
def get_random_pics(img, height, width, h1, w1, num):
    for i in range(num):
        h_start = randint(0, height - h1 - 1)
        w_start = randint(0, width - w1 -1)
        cropped_img = img.crop((w_start, h_start, w_start + w1, h_start + h1))
        # cropped_img.save("D:\\projects\\python\\compression\\cropped\\cropped_img%d.jpg" % i)
        yield (cropped_img)

# img: an Image object
# return: an ndarray num * h1 * w1 * 3
def get_batch_pics(img, height, width, h1, w1, num):
    batch_pics = np.zeros((num, h1, w1, 3))
    batch_num = 0
    for pic in get_random_pics(img, height, width, h1, w1, num):
        # pic: (h1, w1, 3)
        batch_pics[batch_num, :, :, :] = np.asarray(pic)
        batch_num += 1
    return batch_pics

# img: an Image object
def get_all_pics(img, height, width, h1, w1):
    for i in range(0, height, h1):
        for j in range(0, width, w1):
            cropped_img = img.crop((j, i, j + w1, i + h1))
            yield (i, j, cropped_img)

# yuv: a n*3 matrix
def save_img(filename, yuv, height, width):
    rgb_frame = yuv_to_rgb(yuv).reshape(height, width, 3)
    img = Image.fromarray(rgb_frame)
    img.save(filename)
    
