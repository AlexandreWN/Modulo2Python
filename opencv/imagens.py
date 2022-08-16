''' 

RODAR VIDEO


import cv2

cap = cv2.VideoCapture('./Docs/img/video_car.mp4')
ret, frame = cap.read()

while(True):
    ret, frame = cap.read()
    if(cv2.waitKey(50) == ord('q') or ret == False):
        break
    cv2.imshow('frame', frame)
cap.release()
cv2.destroyAllWindows()
'''

'''

DEIXA O VIDEO DE PONTA CABEÇA

import cv2
cap = cv2.VideoCapture('./Docs/img/video_car.mp4')
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("novo_video.avi", fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame, 0)
        output.write(frame)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
output.release()
cv2.destroyAllWindows()
'''

'''
import cv2
import numpy as np
import random as rnd

fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("novo_video2.avi", fourcc, 30.0, (640,480))

x = 10

while(x > 0):
    cardX = rnd.randint(0, 512)
    cardY = rnd.randint(0, 512)

    img = np.full((512,512,3),(0,0,0),np.uint8)
    frame = cv2.circle(img,(cardX,cardY),50,(0,0,255),-1)
    output.write(frame)

    cv2.imshow('frame', frame)
    if cv2.waitKey(int(1000/2)) & 0xFF == ord('q'):
        break
    x -= 0.5
cap.release()
output.release()
cv2.destroyAllWindows()
'''

import cv2
cap = cv2.VideoCapture('./Docs/img/video_car.mp4')
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("carro_psicodelico.avi", fourcc, 20.0, (300,300))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        frame=cv2.resize(frame,(300,300))
        output.write(frame)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
output.release()
cv2.destroyAllWindows()


