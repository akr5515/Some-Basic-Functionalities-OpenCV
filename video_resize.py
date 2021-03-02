import cv2 as cv

capture = cv.VideoCapture('videos/dog.mp4')

def resize_image(frame, scale=.75):
    height = int(frame.shape[0]*scale)
    width = int(frame.shape[1]*scale)

    dimension = (width,height)

    return cv.resize(frame,dimension, interpolation=cv.INTER_AREA)

while True:
    isTrue, frame = capture.read()
    resized_frame = resize_image(frame)
    cv.imshow('Video', frame)
    cv.imshow('Resized video', resized_frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()