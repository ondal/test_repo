import cv2

print('Hello world')

img = cv2.imread('tiger.jpg')
cv2.imshow("window", img)
cv2.waitKey(0)
