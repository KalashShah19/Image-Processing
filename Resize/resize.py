#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 17:18:14 2023

@author: bmiit202006100110040
"""

import cv2

img = img = cv2.imread("img4.jpg", 0)

color = cv2.imread("img4.jpg")

img = cv2.resize(img, (444, 333))

cv2.imshow("Resized Image", img)

cv2.imwrite("Resized.jpg",img)

cv2.waitKey(0)

cv2.destroyAllWindows()