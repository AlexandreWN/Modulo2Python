from calendar import c
from gettext import npgettext
from random import random
import cv2
import numpy as np
import random

def funcao(event,x,y,flags,param):
    global a,b,c
    if event == cv2.EVENT_MOUSEWHEEL:
       cv2.circle(img,(x,y),100,(255,0,0),-1)
       print("Circulo")
    elif event == cv2.EVENT_LBUTTONDBLCLK:
       cv2.ellipse(img,(x,y),(60,20),0,0,360,(0,255,0),-1)
       print("Ellipse")

a = 0
b = 0
c = 0
img = np.full((512,512,3),(a,b,c),np.uint8)
cv2.namedWindow('janela')
cv2.setMouseCallback('janela', funcao)
while(True):
    cv2.imshow('janela',img)
    if cv2.waitKey(10) & 0xFF == 27:
        break
cv2.destroyAllWindows()