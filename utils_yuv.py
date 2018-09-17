import numpy as np

# yuv: an n by 3 matrix    
def save_yuv(filename, yuv):
    with open(filename, "wb") as f:
        f.write(bytearray(yuv[:, 0].tolist()))
        f.write(bytearray(yuv[:, 1].tolist()))
        f.write(bytearray(yuv[:, 2].tolist()))

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