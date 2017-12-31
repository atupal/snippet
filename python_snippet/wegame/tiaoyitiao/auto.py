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
                #if sum_of_tuple(rgb[nextx, nexty], rgb[pos[0], pos[1]]) < 30:
                if sum_of_tuple(rgb[nextx, nexty], rgb[pos[0], pos[1]]) < 20:
                    colors[nextx][nexty] = color
                    stack.append((nextx, nexty))

# Canot use distance as the function name since it will be overwrite by a global variable with same name later
def distance_of_two_point(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

def is_area_circle(points):
    # [left, right, top, bottom]
    corner_points = [points[0]] * 4
    for p in points:
        if p[0] < corner_points[0][0]:
            corner_points[0] = p
        if p[0] > corner_points[1][0]:
            corner_points[1] = p
        if p[1] < corner_points[2][1]:
            corner_points[2] = p
        if p[1] > corner_points[3][1]:
            corner_points[3] = p

    diameter1 = distance_of_two_point(corner_points[0], corner_points[1]) * 0.5
    diameter2 = distance_of_two_point(corner_points[2], corner_points[3]) * 0.5

    #print diameter1, diameter2, len(points)
    return abs(diameter1 - diameter2) < (diameter1 + diameter2) * 0.5 * 0.05

iteration = 0
auto_mode = True
train_iterations = 3
iteration_sleep_time = 1.3
step_one_distance = -1
step_one_time = -1
DEBUG = 0

cv2.namedWindow("img")

def main():
    global iteration, auto_mode, train_iterations, iteration_sleep_time, step_one_distance, step_one_time, DEBUG
    if not DEBUG:
        os.system("cp screen.png previous_screen.png")
        os.system("/home/atupal/Software/Android/Sdk/platform-tools/adb shell screencap -p /sdcard/screen.png && /home/atupal/Software/Android/Sdk/platform-tools/adb pull /sdcard/screen.png && /home/atupal/Software/Android/Sdk/platform-tools/adb shell rm /sdcard/screen.png")
    else:
        auto_mode = False

    img = Image.open("./screen.png")

    size = img.size

    ## Note: Some magic "integer" number as based on the screen size (480, 854), they should be replaced by ratio.
    #if size[1] > 1000:
    enlarge_ratio = 480. / size[0]
    img = img.resize((int(size[0] * enlarge_ratio), int(size[1] * enlarge_ratio)))
    size = img.size

    #rgb = img.convert("RGB")

    arr = img.load()


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
    color_pixels_map = {}

    for x in xrange(size[0]):
        for y in xrange(size[1]):
            color_sum[colors[x][y]] += 1
            if colors[x][y] not in color_pixels_map:
                color_pixels_map[colors[x][y]] = []
            color_pixels_map[colors[x][y]].append((x, y))

    print "color count: ", color

    black_bottom = colors[current_position[0]][current_position[1]]
    black_head = -1
    for color in color_pixels_map:
        color_area = color_pixels_map[color]
        if len(color_area) > 60 and sum_of_tuple(arr[color_area[0]], arr[current_position]) < 60 and is_area_circle(color_area):
            black_head = color
            break
    if black_head != -1:
        for p in color_pixels_map[black_head]:
            arr[p] = (0, 0, 0, 255)

    #initial_height = 150
    initial_height = int(size[1] * 0.2)
    first_color = -1
    for y in xrange(initial_height, size[1]):
        for x in xrange(size[0]):
            color = colors[x][y]
            ### In most cases the first condition works. If not, try the second one.
            ### TODO: combind next two conditions or use clever check
            #if first_color == -1 and colors[x][y] != colors[x][initial_height] and color_sum[colors[x][y]] > 600: #565:
            #if first_color == -1 and colors[x][y] != colors[x][initial_height] and sum_of_tuple(arr[x, y], arr[current_position]) > 300 and color_sum[colors[x][y]] > 100:
            if black_head != -1:
                if color != colors[x][initial_height] and color != black_head and color != black_bottom and color_sum[colors[x][y]] > 100:
                    first_color = colors[x][y]
                    break
            else:
                if first_color == -1 and colors[x][y] != colors[x][initial_height] and sum_of_tuple(arr[x, y], arr[current_position]) > 300 and color_sum[colors[x][y]] > 100:
                    first_color = colors[x][y]
                    break

        if first_color != -1:
            break

    # change the color after we found the black_head and target location
    for p in color_pixels_map[colors[current_position[0]][current_position[1]]]:
        arr[p] = (0, 0, 0, 255)
        pass

    xx = [0, 0, 0, 1, 1, 1, -1, -1, -1]
    yy = [0, 1, -1, 0, 1, -1, 0, 1, -1]
    for i,j in zip(xx, yy):
        arr[(current_position[0] + i, current_position[1] + j)] = (0, 255, 0, 255)

    target_position = [0, 0]

    cnt = 0
    for x in xrange(size[0]):
        for y in xrange(initial_height, size[1]):
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

    if bullseye[0] != 0 and cnt < 150:
        target_position = bullseye

    xx = [0, 0, 0, 1, 1, 1, -1, -1, -1]
    yy = [0, 1, -1, 0, 1, -1, 0, 1, -1]
    for i,j in zip(xx, yy):
        arr[(target_position[0] + i, target_position[1] + j)] = (0, 0, 255, 255)
        pass

    #img.show()
    open_cv_img = numpy.array(img)
    cv2.imshow("img", open_cv_img)
    cv2.waitKey(50)

    distance = ((current_position[0] - target_position[0]) * (current_position[0] - target_position[0]) + \
               (current_position[1] - target_position[1]) * (current_position[1] - target_position[1])) ** 0.5

    print "distance", distance

    suggestion_time = 0

    if step_one_distance == -1:
        step_one_distance = 230 # (480, 854)
        #step_one_distance = 268
    if step_one_time == -1:
        step_one_time = 7 # (480, 854)
        #step_one_time = 7.2
    suggestion_time = step_one_time * 1.0 / step_one_distance * distance

    ### TODO: if the direction is right-top, this suggestion time will be a little larger than actually correct value
    if target_position[0] > current_position[0]: #and suggestion_time > 9:
        correct_rator = 0.9782608695652175
        print "correct the right-top direction, error term: ", suggestion_time * (1 - correct_rator)
        suggestion_time *= correct_rator
    print "suggestion time: ", suggestion_time

    try:
        if not auto_mode:
            time = float(input("step length[1 - 10]: "))
        else:
            time = 0
    except Exception as ex:
        time = 0

    if not time:
        time = suggestion_time

    #t.sleep(iteration_sleep_time)
    time = jump.jump(time)
    t.sleep(iteration_sleep_time)

    print "current iteration: ", iteration
    iteration += 1

try:
    #if __name__ == "__main__":
    while 1:
        main()
except Exception as ex:
    print(ex)
    pass
