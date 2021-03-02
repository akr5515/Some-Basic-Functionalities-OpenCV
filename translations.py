import cv2 as cv
import numpy as np

img = cv.imread('images/1a.jpg')
cv.imshow('image',img)

#translate
def translate(image,x,y):
    translateMat= np.float32([[1,0,x],[0,1,y]])
    dimension = (image.shape[1], image.shape[0])
    return cv.warpAffine(image,translateMat,dimension)

img = translate(img,100,100)
cv.imshow('Translated', img)

#rotation
def rotate(image,angle,rotPoint=None):
    (height,width)=image.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimension = (width,height)
    return cv.warpAffine(image,rotMat,dimension)

img = rotate(img,45)
cv.imshow('Rotated', img)

#flipping
flip = cv.flip(img,-1) #0,1,-1
cv.imshow('Flipped', flip)

#cropped
crop = img[200:400,300:400]
cv.imshow('Cropped', crop)
cv.waitKey(0)