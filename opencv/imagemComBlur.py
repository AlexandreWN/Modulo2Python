import cv2
image = cv2.imread('./Docs/img/ruido.jpg')
image2 = cv2.imread('./Docs/img/mulher.png')
image3 = cv2.imread('./Docs/img/Flor.png')
blur = cv2.blur(image2,(9,9))
gausian = cv2.GaussianBlur(image2,(11,11),0)
median = cv2.medianBlur(image3,7) #Sal e pimenta

cv2.imshow("Filtrada", blur)
cv2.imshow("Original", image2)
cv2.imshow("Gaussian", gausian)
cv2.imshow("Median", median)

cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()