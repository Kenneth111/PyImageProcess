# PyImageProcess
A Python library to process images and YUV files.

Dependencies:

* numpy
* PIL
* scipy

## utils.py
### get_random_pics(img, h, w, num)
This function is developed for training a deep neural network. It can extract a number of patches from a picture. In addtion, this function is a generator and can be used in a for loop.

**img**: an Image object (PIL.Image)

**h**: the height of a patch

**w** : the width of a patch

**num**: how many patches to extract

### get_batch_pics(img, h, w, num)
This function is developed for training a deep neural network. It extracts a number of patches from a picture and pack the patches into a ndarray object. This function calls get_random_pics to get random patches.

**img**: an Image object

**h**: the height of a patch

**w**: the width of a patch

**num**: how many patches to extract

**return**: a 4 dimension ndarray object: [num, w, h, 3]

### get_all_pics(img, h, w)
This function is developed for training a deep neural network. It extracts (height / h) * (width / w) patches from a picture and these patches are not overlapped. In addtion, this function is a generator and can be used in a for loop.

**img**: an Image object (PIL.Image)

**h**: the height of a patch

**w** : the width of a patch

## utils_yuv.py
### get_a_frame(filename, height, width, frameId)
Extract an frame from a YUV file. This function returns an n by 3 matrix containing Y, U and V components.

**filename**: a string, like "capture.yuv"

**height**: the frame's height

**width**: the frame's width

**frameId**: the frame number to be extracted, starting from 1

### get_all_frames(filename, height, width, num_frames)
Extract all the frames and their corrsponding frame ID in a YUV file. This function is a generator and therefore can be used in a for loop.

**filename**: a string, like "capture.yuv"

**height**: the frame's height

**width**: the frame's width

**num_frames**: how many frames in the YUV file

### yuv_to_rgb(yuv_frame)
Convert YUV to RGB . The conversion formula can be found [here](https://www.vocal.com/video/rgb-and-yuv-color-space-conversion/).

**yuv_frame**: an n by 3 matrix containing Y, U and V seperately.

**return**: an n by 3 matrix containing R, G and B seperately.

### def convertYUV2Img(yuv_filename, height, width, num_frames, format, img_filename)
Read frames from a yuv file and save the frame to image files

**yuv_filename**: the yuv file to convert

**height, width**: the height and the width of the yuv file

**num_frames**: how many frames of the yuv file to convert

**format**: such as "jpg", "bmp"

**img_filename**: a string used in image files

### yuv_draw_box(yuv_frame, height, width, startx, starty, endx, endy, color)
Draw a box on a YUV frame.

**yuv_frame**: a n by 3 matrix containing Y, U and V, seperately, or a (height, width, 3) matrix

**color**: "r", "g" or "b"  

## utils_rgb.py
### show_img_diff(file1, file2, diff_file)
Compare two images and save the difference between these images into a new image file.

**file1**: the first image file to compare (string)

**file2**: the second image file to compare (string)

**diff_file**: where to save the difference (string)

### rgb_to_yuv(rgb_frame)
Convert RGB to YUV. The conversion formula can be found [here](https://www.vocal.com/video/rgb-and-yuv-color-space-conversion/).

**rgb_frame**: an n by 3 matrix containing R, G, and B seperately.

**return**: an n by 3 matrix containing Y, U and V seperately.

### save_rgb(filename, rgb, height, width)
Save a RGB frame to a file.

**filename**: The file name, like "test.bmp".

**rgb**: a n by 3 matrix containing R, G and B seperately.

## transform.py
### dct2(a)
2-d discrete cosine transform. This function can be found [here](https://inst.eecs.berkeley.edu/~ee123/sp16/Sections/JPEG_DCT_Demo.html).

**a**: 2-d ndarray object

### idct2(a)
2-d inverse discrete cosine transform. This function can be found [here](https://inst.eecs.berkeley.edu/~ee123/sp16/Sections/JPEG_DCT_Demo.html).

**a**: 2-d ndarray object