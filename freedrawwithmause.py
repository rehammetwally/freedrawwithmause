# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 11:16:57 2022

@author: DevRehamMetwally
"""

import cv2
import numpy as np


################################
#####       VARIABLES       ####
################################
windowname="Drawing"
draw = False



################################
#####       FUNCTION        ####
################################
def drawing(event,x,y,flags,param):
    global ix,iy,draw
    if event == cv2.EVENT_LBUTTONDOWN:
        draw = True
        cv2.circle(img,(x,y),4,(0,0,255),-1)
    elif event == cv2.EVENT_MOUSEMOVE:
        if draw:
            cv2.circle(img,(x,y),4,(0,0,255),-1)
    elif event == cv2.EVENT_LBUTTONUP:
        draw = False
        cv2.circle(img,(x,y),4,(0,0,255),-1)




################################
#####       SHOW IMAGE      ####
################################


img = np.zeros((512,512,3))
cv2.namedWindow(windowname)
cv2.setMouseCallback(windowname,drawing)

while True:
    cv2.imshow(windowname,img)
    if cv2.waitKey(1) & 0xFF ==27:
        break
    
  
cv2.destroyAllWindows()
