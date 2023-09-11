#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 17:19:45 2023

@author: bmiit202006100110040
"""

import cv2
import numpy as np

# Open the image.
img = cv2.imread('Resized.jpg',0)

# Apply gamma correction.
gamma_corrected = np.array(255*(img / 255) ** 0.9, dtype = 'uint8')
 
#resize just to check
#gamma_corrected = cv2.resize(gamma_corrected, (900, 550)) 
 
# Save edited images.
cv2.imshow('new.jpg', gamma_corrected)

cv2.imwrite('new.jpg', gamma_corrected) 
    
cv2.waitKey(0)

cv2.destroyAllWindows()