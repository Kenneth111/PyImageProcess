# PyImageProcess
A Python library to process images and YUV files.

## get_a_frame(filename, height, width, frameId)
get_a_frame is used to extract an frame from a YUV file. This function returns an n by 3 matrix containing Y, U and V components.

**filename**: a string, like "capture.yuv"

**height**: the frame's height

**width**: the frame's width

**frameId**: the frame number to be extracted, starting from 1

## get_all_frames(filename, height, width, num_frames)
get_all_frames is used to extract all the frames and their corrsponding frame ID in a YUV file. This function is a generator and therefore can be used in a for loop.

**filename**: a string, like "capture.yuv"

**height**: the frame's height

**width**: the frame's width

**num_frames**: how many frames in the YUV file
