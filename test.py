import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

img1 = cv2.imread('1.jpg')
edgs = cv2.Canny(img1,180,300)
cv2.imshow('result',edgs)
cv2.waitKey(0)
cv2.destroyAllWindows()