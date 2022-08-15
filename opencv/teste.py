import cv2
import numpy as np
'''
dog = cv2.imread('./Docs/img/dog.jpg', cv2.IMREAD_COLOR)
dog_cinza = cv2.imread('./Docs/img/dog.jpg', cv2.IMREAD_GRAYSCALE)
dog_trasp = cv2.imread('./Docs/img/dog.jpg', cv2.IMREAD_UNCHANGED)

cv2.imshow('dogão', dog)
cv2.waitKey(0)
cv2.imshow('dogão', dog_cinza)
cv2.waitKey(0)
cv2.imshow('dogão', dog_trasp)
cv2.waitKey(0)


cv2.destroyAllWindows()

cv2.imwrite('dog_cinza.jpg', dog_cinza)
'''
img = np.zeros((512,512,3), np.uint8)

cv2.line(img, (150,0),(150,512),(255,255,255),5)
cv2.line(img, (350,0),(350,512),(255,255,255),5)

cv2.line(img, (0,150),(512,150),(255,255,255),5)
cv2.line(img, (0,350),(512,350),(255,255,255),5)

cv2.imshow("tic-tac-toe", img)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()

#Rettangullo(image)