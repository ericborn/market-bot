# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 14:55:56 2020

@author: Eric
"""

import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys import PressKey, ESC, Y, ONE, TWO, THREE,FOUR,\
                       FIVE, SIX, SEVEN, EIGHT, NINE, ZERO

def process_img(image):
    original_image = image
    # convert to gray
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # edge detection
    processed_img =  cv2.Canny(processed_img, threshold1 = 200, threshold2=300)
    return processed_img

def main():
    last_time = time.time()
    while True:
        screen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
        #print('Frame took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        new_screen = process_img(screen)
        cv2.imshow('window', new_screen)
        #cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break