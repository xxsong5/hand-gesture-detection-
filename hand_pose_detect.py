import cv2
import numpy as np






cap = cv2.VideoCapture(0)


hand_cascade = cv2.CascadeClassifier('fist.xml')
hand_cascade1 = cv2.CascadeClassifier('palm.xml')

while (1):

    # Take each frame
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)


  
    hands = hand_cascade.detectMultiScale(gray, 1.3, 5)
   # hands1 = hand_cascade1.detectMultiScale(gray, 1.3, 5)

    #get largest hand rect
    x_best=0
    y_best=0
    w_best=640
    h_best=480
    area_best=0
    succeed=0
    for (x,y,w,h) in hands:
        area=w*h
        if area > area_best:
           area_best = area
           x_best=x
           y_best=y
           w_best=w
           h_best=h
           succeed=1
    if succeed == 1:
        x_best -= w_best
        y_best -= int(h_best*1.3)
        w_best = w_best*3 + x_best
        h_best = h_best*3 + y_best
        cv2.rectangle(frame,(x_best,y_best),(w_best,h_best),(255,0,0),2)
        
        if x_best < 0:
           x_best =0
        if y_best <0:
           y_best =0
        if w_best >639:
           w_best =639
        if h_best >479:
           h_best=479
        print x_best, w_best, y_best, h_best
    roi_gray= gray[y_best:h_best,x_best:w_best]
    hands1 = hand_cascade1.detectMultiScale(roi_gray, 1.3, 5)
  
    for (x,y,w,h) in hands1:
       cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
       


  #  for (x,y,w,h) in hands1:
  #    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)


    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    cv2.waitKey(1)

cv2.destroyAllWindows()

    

