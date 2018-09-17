import numpy as np
from PIL import Image
# yuv: a n*3 matrix
def save_rgb(filename, rgb, height, width):
    rgb_frame = rgb.reshape(height, width, 3)
    img = Image.fromarray(rgb_frame)
    img.save(filename)

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