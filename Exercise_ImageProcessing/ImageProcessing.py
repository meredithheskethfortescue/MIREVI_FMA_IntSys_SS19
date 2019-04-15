#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract elements in an image from background
@author: Raphael Stascheit at MIREVI
"""

import os
import argparse

import numpy as np
from skimage import io
from scipy import ndimage

FLAG_VERBOSE = True


def expose(path, flag_dark_background=False, flag_clip=False, flag_edge=False):
    # laod image
    # Note: return value is a numpy array with float values between 0..1
    img_gray = io.imread(path, as_gray=True)

    # Background color must be zero. Hence to remove a light background the image must be inverted.
    if not flag_dark_background:
        img_gray = 1 - img_gray

    if flag_edge:
        img_gray = convolve_edge(img_gray)

    if flag_clip:
        img_gray = clip(img_gray)

    # create empty image with the same shape as the input but with four channels
    height, width = np.shape(img_gray)
    img_rgba = np.empty([height, width, 4], dtype=np.float64)

    # grayscale to alpha
    img_rgba[..., 3] = img_gray

    # set target color tone to the r, g and b channel
    color_target = np.array([38, 139, 210], dtype=np.float64) / 255
    img_rgba[..., :3] = color_target

    return img_rgba


def clip(img):
    print("Clipped 3% of the highest and lowest values.")

    # normalize
    img_clipped = img / np.max(img)

    # symmetric stretch 3%
    quantile = 0.03
    img_clipped *= (1 + 2 * quantile)
    img_clipped -= quantile

    # clip
    img_clipped[img_clipped < 0] = 0.
    img_clipped[img_clipped > 1] = 1.

    return img_clipped


def convolve_edge(img):
    # blur image to smooth background with a boxblur
    kernel_blur = np.array([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]]) / 9

    img_blurred = ndimage.convolve(img, kernel_blur, mode='reflect')

    # simple edge detection (gradients)
    kernel_edge = np.array([[-1, -1, -1],
                            [-1, 8, -1],
                            [-1, -1, -1]])

    img_convolved = ndimage.convolve(img_blurred, kernel_edge, mode='reflect')

    # get absolute value (edge detection gives gradients. Gradients can be negative)
    img_convolved = np.abs(img_convolved)
    # normalize
    img_convolved /= np.max(img_convolved)

    return img_convolved


def save_result(image, path_input):
    """Append designator to filename and save image as *.png file"""
    dir_input = os.path.dirname(os.path.abspath(path_input))

    filename_prefix = str(os.path.basename(path_input).split('.')[0])
    filename_out = filename_prefix + '_exposed.png'

    path_out = os.path.join(dir_input, filename_out)

    print("Image saved to", path_out)
    io.imsave(path_out, image)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Extract elements in an image from background")

    # positional arguments
    parser.add_argument('-i', '--input',
                        help="Path to inputfile (*.jpg, or *.png)")

    parser.add_argument('--darkbackground',
                        action='store_true',
                        help="Set this flag if the background in the image is dark.")

    parser.add_argument('--clip',
                        action='store_true',
                        help="Stretch contrast by clipping min and max values")

    parser.add_argument('--edgedetection',
                        action='store_true',
                        help="Apply canny edge detection to exposed image")

    args = parser.parse_args()

    # image processing
    img_out = expose(args.input,
                     flag_dark_background=args.darkbackground,
                     flag_clip=args.clip,
                     flag_edge=args.edgedetection)

    # save image
    save_result(img_out, args.input)

    # show result
    if FLAG_VERBOSE:
        # only import if necessary
        from matplotlib import pyplot as plt

        plt.imshow(img_out)
        plt.show()
