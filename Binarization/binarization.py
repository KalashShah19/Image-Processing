#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 17:12:48 2023

@author: bmiit202006100110040
"""

import cv2
from matplotlib import pyplot as plt

img = cv2.imread("Orange.jpg",0)

hist = cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist, color='b')
plt.show()

cv2.imshow("Original", img)

thresh, new = cv2.threshold(img, 230, 255, cv2.THRESH_BINARY)
cv2.imshow("Histogram", new)
cv2.imwrite("Histogram.jpg", new)

thresh, new = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("127", new)
cv2.imwrite("127.jpg", new)

avg = img.mean()
thresh, new = cv2.threshold(img, avg, 255, cv2.THRESH_BINARY)
cv2.imshow("Average = " + str(avg), new)
cv2.imwrite("Average.jpg", new)

thresh, otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) 
cv2.imshow("OTSU = " + str(thresh), otsu)
cv2.imwrite("OTSU.jpg", otsu)

cv2.waitKey(0)

cv2.destroyAllWindows()