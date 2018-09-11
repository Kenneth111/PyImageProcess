# PyImageProcess
A Python library to process images and YUV files.

Dependencies:

* numpy
* PIL
* scipy

## utils.py
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

### rgb_to_yuv(rgb_frame)
Convert RGB to YUV. The conversion formula can be found [here](https://www.vocal.com/video/rgb-and-yuv-color-space-conversion/).

**rgb_frame**: an n by 3 matrix containing R, G, and B seperately.

**return**: an n by 3 matrix containing Y, U and V seperately.

### save_img(filename, yuv, height, width)
Save a YUV frame to a file. The YUV frame will be converted to a RGB frame and saved to a file.

**filename**: The file name, like "test.bmp".

**yuv**: a n by 3 matrix containing Y, U and V seperately.

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

## transform.py
### dct2(a)
2-d discrete cosine transform. This function can be found [here](https://inst.eecs.berkeley.edu/~ee123/sp16/Sections/JPEG_DCT_Demo.html).

**a**: 2-d ndarray object

### idct2(a)
2-d inverse discrete cosine transform. This function can be found [here](https://inst.eecs.berkeley.edu/~ee123/sp16/Sections/JPEG_DCT_Demo.html).

**a**: 2-d ndarray object