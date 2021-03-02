import cv2 as cv

img = cv.imread('images/1a.jpg')
cv.imshow('Pix', img)

cv.waitKey(0)