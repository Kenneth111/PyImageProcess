from PIL import Image
import numpy as np
from utils import rgb_to_yuv, yuv_to_rgb, get_a_frame, get_batch_pics, save_img, save_yuv

def demo_get_batch_pics():
    img = Image.open("172.png")
    pics = get_batch_pics(img, 15, 15, 15)

def demo_yuv_rgb():
    yuv_frame = get_a_frame("../capture.yuv", 1080, 1920, 1)
    save_img("test.bmp", yuv_frame, 1080, 1920)
    rgb_frame = yuv_to_rgb(yuv_frame)
    yuv_frame1 = rgb_to_yuv(rgb_frame)
    save_yuv("test1.yuv", yuv_frame1)

def main():
    demo_get_batch_pics()
    demo_yuv_rgb()

if __name__ == "__main__":
    main()