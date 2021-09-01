import numpy as np
from PIL import Image
from .utils_rgb import save_rgb

# yuv: an n by 3 matrix    
def save_yuv(filename, yuv):
    with open(filename, "wb") as f:
        f.write(bytearray(yuv[:, 0].tolist()))
        f.write(bytearray(yuv[:, 1].tolist()))
        f.write(bytearray(yuv[:, 2].tolist()))

def save_yuv_420(filename, y, u, v):
    with open(filename, "wb") as f:
        f.write(bytearray(y.tolist()))
        f.write(bytearray(u.tolist()))
        f.write(bytearray(v.tolist()))

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

def get_a_frame(filename: str, height: int, width: int, frame_id: int):
    """
    return a n * 3 matrix
    """
    with open(filename, "rb") as f_in:
        f_in.seek(height * width * 3 * (frame_id - 1))
        y = f_in.read(height * width)
        u = f_in.read(height * width)
        v = f_in.read(height * width)
    y = np.frombuffer(y, dtype="uint8")
    u = np.frombuffer(u, dtype="uint8")
    v = np.frombuffer(v, dtype="uint8")
    return np.vstack([y, u, v]).T

def get_a_frame_420(filename: str, height: int, width: int, frame_id: int):
    with open(filename, "rb") as f_in:
        f_in.seek( ((height * width * 3) >> 1) * (frame_id - 1))
        y = f_in.read(height * width)
        u = f_in.read( (height * width) >> 2)
        v = f_in.read( (height * width) >> 2)
    y = np.frombuffer(y, dtype="uint8")
    u = np.frombuffer(u, dtype="uint8")
    v = np.frombuffer(v, dtype="uint8")
    return (y, u, v)

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

# yuv: height * width * 3
def save_a_patch(filename, startX, startY,  height, width, yuv):
    c = len(yuv.shape)
    if c != 3:
        return -1
    (h, w, c) = yuv.shape
    if startX + width > w or startY + height > h or c != 3:
        return -2
    save_yuv(filename, yuv[startY: startY + height, startX: startX + width, :].reshape(-1, 3))
    return 0

# read frames from a yuv file and save the frame to image files
# yuv_filename: the yuv file to convert
# height, width: the height and the width of the yuv file
# num_frames: how many frames of the yuv file to convert
# format: such as "jpg", "bmp"
# img_filename: a string used in image files
def convertYUV2Img(yuv_filename, height, width, num_frames, format, img_filename):
    for yuv, i in get_all_frames(yuv_filename, height, width, num_frames):
        rgb = yuv_to_rgb(yuv)
        tmp_filename = img_filename + ("-%d.%s" % (i, format))
        save_rgb(tmp_filename, rgb, height, width)


"""
yuv_frame: (height * width, 3) 
color: "r", "g" or "b"
"""
def yuv_draw_box(yuv_frame, height, width, startx, starty, endx, endy, color):
    if startx < 0 or starty <0 or endx >= width or endy >= height:
        return -1
    if color == "r":
        yuv_color = (82, 90, 240)
    elif color == "g":
        yuv_color = (145, 54, 34)
    else:
        yuv_color = (41, 240, 110)
    dims = len(yuv_frame.shape)
    if dims == 2:
        yuv_frame = yuv_frame.reshape(height, width, 3)
    yuv_frame[starty, startx: endx, 0] = np.ones((1, endx - startx)) * yuv_color[0]
    yuv_frame[starty, startx: endx, 1] = np.ones((1, endx - startx)) * yuv_color[1]
    yuv_frame[starty, startx: endx, 2] = np.ones((1, endx - startx)) * yuv_color[2]
    yuv_frame[endy, startx: endx, 0] = np.ones((1, endx - startx)) * yuv_color[0]
    yuv_frame[endy, startx: endx, 1] = np.ones((1, endx - startx)) * yuv_color[1]
    yuv_frame[endy, startx: endx, 2] = np.ones((1, endx - startx)) * yuv_color[2]
    for h in range(starty, endy):
        yuv_frame[h, startx, 0] = yuv_color[0]
        yuv_frame[h, startx, 1] = yuv_color[1]
        yuv_frame[h, startx, 2] = yuv_color[2]
        yuv_frame[h, endx, 0] = yuv_color[0]
        yuv_frame[h, endx, 1] = yuv_color[1]
        yuv_frame[h, endx, 2] = yuv_color[2]
    if dims == 2:
        return yuv_frame.reshape(-1, 3)
    return yuv_frame