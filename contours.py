import cv2 as cv
import numpy as np


img = cv.imread('images/cats.jpg')
cv.imshow('cats',img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

#gray
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY);
cv.imshow('Gray', gray)

#blur
blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#canny
canny =cv.Canny(blur,125,175)
cv.imshow('Canny', canny)

#threshold
ret, thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

#contours
contours, hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours found')

#draw contours
cv.drawContours(blank,contours,-1,(0,255,0),1);
cv.imshow('Draw contours', blank)

cv.waitKey(0)