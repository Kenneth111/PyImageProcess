from PIL import Image
import numpy as np
from utils import get_batch_pics
from utils_rgb import rgb_to_yuv, save_rgb, show_img_diff
from utils_yuv import yuv_to_rgb, get_a_frame, save_yuv, save_a_patch, convertYUV2Img, yuv_draw_box
from jpeg import quantization, in_quantization
from transform import dct2, idct2

def demo_get_batch_pics():
    img = Image.open("172.png")
    pics = get_batch_pics(img, 15, 15, 15)

def demo_yuv_rgb():
    yuv_frame = get_a_frame("../capture.yuv", 1080, 1920, 1)
    rgb_frame = yuv_to_rgb(yuv_frame)
    save_rgb("test.bmp", rgb_frame, 1080, 1920)
    yuv_frame1 = rgb_to_yuv(rgb_frame)
    save_yuv("test1.yuv", yuv_frame1)
    
def demo_save_rgb_diff():
    file1 = r'1080.bmp'
    file2 = r'20x1080.bmp'
    diff_file = r'diff.bmp'
    show_img_diff(file1, file2, diff_file)

def demo_save_a_patch():
    yuv_frame = get_a_frame("../capture.yuv", 1080, 1920, 1)
    save_a_patch("test_patch.yuv", 0, 0, 16, 16, yuv_frame.reshape(1080, 1920, 3))

def demo_jpeg():
    yuv_frame = get_a_frame("../capture.yuv", 1080, 1920, 1).reshape(1080, 1920, 3)
    tmp_frame = np.zeros((1080, 1920), dtype="uint8")
    for i in range(0, 1080, 8):
        for j in range(0, 1920, 8):
            tmp_frame[i: i + 8, j: j+ 8] = idct2(in_quantization(np.int8(quantization(dct2(yuv_frame[i: i+8, j: j+8, 0]), 0)), 0))
    img = Image.fromarray(tmp_frame)
    img.save("ddd.bmp")

def demo_yuv_draw_box():
    yuv_frame = get_a_frame("../capture.yuv", 1080, 1920, 1).reshape(1080, 1920, 3)
    yuv_frame = yuv_draw_box(yuv_frame, 1080, 1920, 100, 120, 220, 250, "r")
    yuv_frame = yuv_frame.reshape(-1, 3)
    save_yuv("draw.yuv", yuv_frame)

def main():
    # demo_get_batch_pics()
    # demo_yuv_rgb()
    # demo_save_rgb_diff()
    # demo_save_a_patch()
    # demo_jpeg()
    # convertYUV2Img('d:/capture1.yuv', 1080, 1920, 20, 'bmp', 'dcgan')
    demo_yuv_draw_box()

if __name__ == "__main__":
    main()