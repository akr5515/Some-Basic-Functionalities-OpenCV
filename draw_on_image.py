import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype = 'uint8')

cv.imshow('blank',blank);
blank[200:300, 300:400]=0,0,255

cv.putText(blank,'Alu Ala', (120,222),cv.FONT_HERSHEY_COMPLEX,2,(255,0,0),thickness=2)
cv.imshow('red', blank)
cv.waitKey(0)