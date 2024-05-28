import cv2 as cv

""" img = cv.imread('D:\\Screenshot 2022-11-20 235959.png')
    cv.vi('ll',img)
    cv.waitKey(0)
 """



def rescale ( frame , scale = 0.75) : 
    width = int(frame.shape[1] * scale)
    hieght = int(frame.shape[0] * scale)
    dimentions = (width , hieght)
    return cv.resize(frame , dimentions , interpolation = cv.INTER_AREA)

capture = cv.VideoCapture('D:\\WIN_20221115_21_12_01_Pro.mp4') 

while True  :

    is_true , frame = capture.read()
    resized = rescale(frame)
    cv.imshow('video' , frame)
    cv.imshow('video2' , resized)
    if cv.waitKey(20) & 0Xff==ord('c'):
            break

capture.release()
cv.destroyAllWindows()