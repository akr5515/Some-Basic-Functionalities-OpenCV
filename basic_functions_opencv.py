import cv2 as cv

img = cv.imread('images/1a.jpg')
img = cv.resize(img,(700,500))

cv.imshow('image',img)
#gray
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#blur
blur = cv.blur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

#edge detection
canny = cv.Canny(blur,125,175)
cv.imshow('Canny',canny)

cv.waitKey(0)