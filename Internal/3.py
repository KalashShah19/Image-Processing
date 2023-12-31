#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 18:06:44 2023

@author: bmiit202006100110040
"""

import cv2
import numpy as n

img = cv2.imread("3.jpg")

mini = n.min(img)
maxi = n.max(img)

new = ((img - mini) * (255 / (maxi- mini))).astype(n.uint8)

cv2.imshow("New3", new)
cv2.imwrite("New3.jpg", new)
cv2.waitKey(0)
cv2.destroyAllWindows()