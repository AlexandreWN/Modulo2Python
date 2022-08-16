from calendar import c
from gettext import npgettext
from random import random
import cv2
import numpy as np
import random

def funcao(event,x,y,flags,param):
    global r,g,bl
    cv2.circle(img,(x,y),10,(bl,g,r),-1)
     

a = 0
b = 0
c = 0
r = 0
g = 0
bl = 0
font = cv2.FONT_HERSHEY_SIMPLEX
img = np.full((512,512,3),(a,b,c),np.uint8)
cv2.namedWindow('janela')
cv2.setMouseCallback('janela', funcao)
while(True):
    cv2.rectangle(img, (0,0),(200,100),(0,0,0),-1)
    cv2.putText(img,"red = " + str(r),(0,20), font, 1, (191,0,191), 1, cv2.LINE_AA)
    cv2.putText(img,"gren = " + str(g),(0,50), font, 1, (191,0,191), 1, cv2.LINE_AA)
    cv2.putText(img,"blue = " + str(bl),(0,90), font, 1, (191,0,191), 1, cv2.LINE_AA)

    cv2.imshow('janela',img)
    key = cv2.waitKey(10)

    if key& 0xFF == 27:
        break
    elif key & 0xFF == 114:
        if(r == 250):
            r = 0
        else:
            r += 10
    elif key & 0xFF == 103:
        if(g == 250):
            g = 0
        else:
            g += 10
    elif key & 0xFF == 98:
        if(bl == 250):
            bl = 0
        else:
            bl += 10
cv2.destroyAllWindows()