import cv2
image = cv2.imread("./Docs/img/dog.jpg")
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow("Dog_HSV",image_hsv)
cv2.imshow("Original", image)

cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()