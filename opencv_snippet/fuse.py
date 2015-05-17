#!/bin/sh
# -*- coding: utf-8 -*-
''''which python2 >/dev/null && exec python2 "$0" "$@" # '''
''''which python  >/dev/null && exec python  "$0" "$@" # '''

import cv2, cv
import numpy as np


def fuse(file_path):
    img = cv2.imread(file_path, 1)
    cv.ShowImage('origin', cv.fromarray(img))
    cv.WaitKey(0)

    for i in xrange(1):
        kernel = np.ones((20,20), np.float32)/2500
        img = cv2.filter2D(img, -1, kernel)

    cv.ShowImage('origin', cv.fromarray(img))
    cv.WaitKey(0)

if __name__ == '__main__':
    file_path = '/home/atupal/Pictures/login.jpg'
    file_path = '/home/atupal/Downloads/Photo_0516_1a.jpg'
    fuse(file_path)
