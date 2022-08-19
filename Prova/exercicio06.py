import cv2

image2 = cv2.imread('./DocsProva/mulher.png')
median = cv2.medianBlur(image2,3)

cv2.imshow("Original", image2)
cv2.imshow("Median", median)

cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()