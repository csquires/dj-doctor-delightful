import cv2

img = cv2.imread('messi.jpg')
cv2.imshow("img",img)
k = cv2.waitKey(0)
cv2.destroyAllWindows()
for i in range(5):
	cv2.waitKey(1)