import cv2 as cv
import numpy as np 

blank = np.zeros((500 , 500 , 3) , dtype='uint8') 
cv.imshow("Black" , blank)

# paint the image acertian color
# blank[:] = 255, 255 ,255
#cv.imshow("white" , blank)

# drawing a recatangle 
#cv.rectangle(blank, (0,0) , (250 , 500) , (0,0,255), thickness= cv.FILLED)
#cv.rectangle(blank, (0,0) , (blank.shape[0] , blank.shape[0]//2) , (0,0,255), thickness= -1) #another way of doing the same thing
#cv.imshow("rectangle" , blank)

# drawing a circle 
#cv.circle(blank,(250,250) , 50 , (0,0,255) , thickness= 3)
#cv.imshow("circle" , blank)

# drawing a line
#cv.line(blank, (0,0) , (250 , 500) , (0,0,255), thickness= 3)
#cv.imshow("line" ,blank)

# writing text 
#cv.putText(blank, "wesam" , (255 ,255), cv.FONT_HERSHEY_TRIPLEX , 1.0 , (0,0,255) , 2)
#cv.imshow('text' , blank)
cv.waitKey(0) 