#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 18:09:53 2023

@author: bmiit202006100110040
"""

import cv2
import numpy as n
from matplotlib import pyplot as plt

img = cv2.imread("1.jpg")
cv2.imshow("Original", img)

hist = cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist, color='b')
plt.title('Image Histogram For Blue Channel GFG')
plt.show()

mini = n.min(img)
maxi = n.max(img)

new = ((img - mini) * (255 / (maxi- mini))).astype(n.uint8)

newHist = cv2.calcHist([new],[0],None,[256],[0,256])
plt.plot(newHist, color='b')
plt.show()

cv2.imshow("New", new)
cv2.imwrite("New1.jpg", new)

cv2.waitKey(0)
cv2.destroyAllWindows()