# -*- coding: utf-8 -*-

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
    v1 = [1.000, 0.001, 1.574]
    v2 = [1.000, -0.187, -0.469]
    v3 = [1.000, 1.856, 0.001]    
    mat1 = np.array([v1, v2, v3])
    mat1 = mat1.T
    v4 = np.array([[16, 128, 128]], dtype="uint8")
    rgb_frame -= v4
    rgb_frame = np.clip(np.matmul(rgb_frame, mat1), 0, 255)
    return np.uint8(rgb_frame.reshape(yuv_frame.shape))

# return a n*3 matrix
def rgb_to_yuv(rgb_frame):
    yuv_frame = np.copy(rgb_frame)
    v1 = [0.213, 0.715, 0.072]
    v2 = [-0.115, -0.385, 0.500]
    v3 = [0.500, -0.454, -0.046]    
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

# yuv: a n*3 matrix
def save_rgb(filename, rgb, height, width):
    rgb_frame = rgb.reshape(height, width, 3)
    img = Image.fromarray(rgb_frame)
    img.save(filename)

# yuv: an n by 3 matrix    
def save_yuv(filename, yuv):
    with open(filename, "wb") as f:
        f.write(bytearray(yuv[:, 0].tolist()))
        f.write(bytearray(yuv[:, 1].tolist()))
        f.write(bytearray(yuv[:, 2].tolist()))

# file1: string
# file2: string
# diff_file: where to save the comparison result
def show_img_diff(file1, file2, diff_file):
    img1 = Image.open(file1)
    img2 = Image.open(file2)
    if img1.size != img2.size:
        print("the size of file1 is different from the size of file2")
        return
    rgb_img1 = np.array(img1)
    rgb_img2 = np.array(img2)
    diff_img = abs(rgb_img1 - rgb_img2)
    img3 = Image.fromarray(diff_img)
    img3.save(diff_file)