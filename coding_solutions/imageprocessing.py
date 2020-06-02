# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg',-1)
%matplotlib auto
cv2.imshow('image',img)