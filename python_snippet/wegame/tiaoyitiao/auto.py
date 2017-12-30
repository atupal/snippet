#!/bin/sh
# -*- coding: utf-8 -*-
''''which python2 >/dev/null && exec python2 "$0" "$@" # '''
''''which python  >/dev/null && exec python  "$0" "$@" # '''

import ipdb
import os
import time as t
import numpy
import cv2

from PIL import Image

import jump


def sum_of_tuple(a, b):
    if len(a) > len(b):
        a, b = b, a
    return sum( abs(a[i] - b[i]) for i in xrange(len(a)) )

def dfs(colors, rgb, x, y, color):

    sizex = len(colors)
    sizey = len(colors[0])

    stack = [(x, y)]

    xx = [0, 0, 1, 1, 1, -1, -1, -1]
    yy = [-1, 1, 0, 1, -1, 0, 1, -1]
    xx_yy = zip(xx, yy)

    while len(stack) > 0:
        pos = stack.pop()
        colors[pos[0]][pos[1]] = color

        for i,j in xx_yy:
            nextx = pos[0] + i
            nexty = pos[1] + j
            if nextx >= 0 and nextx < sizex and nexty >= 0 and nexty < sizey and colors[nextx][nexty] == -1:
                if sum_of_tuple(rgb[nextx, nexty], rgb[pos[0], pos[1]]) < 30:
                    colors[nextx][nexty] = color
                    stack.append((nextx, nexty))

distance_sum = 0
time_sum = 0

iteration = 0
auto_mode = False
train_iterations = 3

cv2.namedWindow("img")

while 1:
#if __name__ == "__main__":

    os.system("/home/atupal/Software/Android/Sdk/platform-tools/adb shell screencap -p /sdcard/screen.png && /home/atupal/Software/Android/Sdk/platform-tools/adb pull /sdcard/screen.png && /home/atupal/Software/Android/Sdk/platform-tools/adb shell rm /sdcard/screen.png")

    img = Image.open("./screen.png")

    #rgb = img.convert("RGB")

    arr = img.load()

    size = img.size

    current_position = (0, 0)

    print "size:", size

    #ipdb.set_trace()

    for width in xrange(size[0]):
        for height in xrange(size[1]):

            v = arr[width, height]
            #print rgb.getpixel((width, height))

            if sum_of_tuple((54, 60, 102), v) < 7:
                if height > current_position[1]:
                    current_position = (width, height)

    print "current_position: ", current_position

    target_position = (0, 0)

    colors = [ [-1] * size[1] for _ in xrange(size[0]) ]

    color = 0
    #colors[0][0] = color

    #for x in xrange(size[0]):
    #    for y in xrange(size[1]):
    #        if sum_of_tuple(arr[x, y], arr[0, 0]) < 10:
    #            colors[x][y] = color

    #color += 1
    for x in xrange(size[0]):
        for y in xrange(size[1]):
            if colors[x][y] == -1:
                dfs(colors, arr, x, y, color)
                color += 1

    color_sum = [0] * color

    for x in xrange(size[0]):
        for y in xrange(size[1]):
            color_sum[colors[x][y]] += 1

    print "color count: ", color

    first_color = -1
    for y in xrange(150, size[1]):
        for x in xrange(size[0]):
            if first_color == -1 and colors[x][y] != colors[x][150] and color_sum[colors[x][y]] > 600:
                first_color = colors[x][y]

    xx = [0, 0, 0, 1, 1, 1, -1, -1, -1]
    yy = [0, 1, -1, 0, 1, -1, 0, 1, -1]
    for i,j in zip(xx, yy):
        arr[(current_position[0] + i, current_position[1] + j)] = (0, 255, 0, 255)

    target_position = [0, 0]

    cnt = 0
    for x in xrange(size[0]):
        for y in xrange(150, size[1]):
            if colors[x][y] == first_color:
                arr[x, y] = (255, 0, 0, 255)
                cnt += 1
                if target_position[0] == 0:
                    target_position = [x, y]
                else:
                    target_position[0] = target_position[0] * 1.0 * (cnt - 1) / cnt + x * 1.0 / cnt
                    target_position[1] = target_position[1] * 1.0 * (cnt - 1) / cnt + y * 1.0 / cnt

    target_position[0] = int(target_position[0])
    target_position[1] = int(target_position[1])

    xx = [0, 0, 0, 1, 1, 1, -1, -1, -1]
    yy = [0, 1, -1, 0, 1, -1, 0, 1, -1]
    for i,j in zip(xx, yy):
        arr[(target_position[0] + i, target_position[1] + j)] = (255, 0, 0, 255)

    bullseye = [0, 0]
    cnt = 0
    for x in xrange(target_position[0] - 25, target_position[0] + 25):
        for y in xrange(target_position[1] - 25, target_position[1] + 25):
            if x >= 0 and x < size[0] and y >= 0 and y < size[1] and sum_of_tuple(arr[x, y], (245, 245, 245, 255)) < 10:
                cnt += 1
                if bullseye[0] == 0:
                    bullseye= [x, y]
                else:
                    bullseye[0] = bullseye[0] * 1.0 * (cnt - 1) / cnt + x * 1.0 / cnt
                    bullseye[1] = bullseye[1] * 1.0 * (cnt - 1) / cnt + y * 1.0 / cnt

    if bullseye[0] != 0 and cnt < 100:
        target_position = bullseye

    xx = [0, 0, 0, 1, 1, 1, -1, -1, -1]
    yy = [0, 1, -1, 0, 1, -1, 0, 1, -1]
    for i,j in zip(xx, yy):
        arr[(target_position[0] + i, target_position[1] + j)] = (0, 0, 255, 255)
        pass

    #img.show()
    open_cv_img = numpy.array(img)
    cv2.imshow("img", open_cv_img)
    cv2.waitKey(10)

    distance = ((current_position[0] - target_position[0]) * (current_position[0] - target_position[0]) + \
               (current_position[1] - target_position[1]) * (current_position[1] - target_position[1])) ** 0.5

    print "distance", distance

    suggestion_time = 0

    if time_sum != 0:
        suggestion_time = time_sum * 1.0 / distance_sum * distance

    suggestion_time = 7 * 1.0 / 230* distance
    print "suggestion time: ", suggestion_time

    if suggestion_time > 0 and iteration > train_iterations:
        auto_mode = True
    else:
        auto_mode = False

    try:
        time = input("step length[1 - 10]: ")
    except Exception as ex:
        time = 0

    if not time:
        time = suggestion_time

    time = jump.jump(time)
    t.sleep(1)

    if time > 0 and not auto_mode:
        distance_sum += distance
        time_sum += time

    iteration += 1
