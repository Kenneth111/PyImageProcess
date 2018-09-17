from PIL import Image
import numpy as np
from utils import get_batch_pics
from utils_rgb import rgb_to_yuv, save_rgb, show_img_diff
from utils_yuv import yuv_to_rgb, get_a_frame, save_yuv

def demo_get_batch_pics():
    img = Image.open("172.png")
    pics = get_batch_pics(img, 15, 15, 15)

def demo_yuv_rgb():
    yuv_frame = get_a_frame("../capture.yuv", 1080, 1920, 1)
    rgb_frame = yuv_to_rgb(yuv_frame)
    save_rgb("test.bmp", rgb_frame, 1080, 1920)
    yuv_frame1 = rgb_to_yuv(rgb_frame)
    save_yuv("test1.yuv", yuv_frame1)
    
def save_rgb_diff():
    file1 = r'1080.bmp'
    file2 = r'20x1080.bmp'
    diff_file = r'diff.bmp'
    show_img_diff(file1, file2, diff_file)

def main():
    demo_get_batch_pics()
    demo_yuv_rgb()
    save_rgb_diff()

if __name__ == "__main__":
    main()