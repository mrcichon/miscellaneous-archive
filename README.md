Bits and pieces of miscellaneous code that either are or could be useful.

Rotate.py used to be much more complex but has since become obsolete due to PIL introducing a very convenient way of doing basically the same, namely rotating the image based on metadata.

screen_capture_multithread.py is a dead useful way of capturing the live feed from the screen. I have been unable to find or think of a much more efficient way of doing this. mss allows for a pretty acceptable framerate.

ConvertRGBAtoRGB is a quick fix I have thrown together to get a proper shape of my numpy array without breaking anything. Tensorflow doesn't complain so it seems to be working

distance.py is a rather simplistic way of measuring distance, based on focal distance formula. I wouldn't dare to use it in any project where measurements need to be in any way, shape or form accurate.
