import cv2
p1=cv2.imread('1.jpg')
p2=cv2.imread('2.png')
p3=cv2.imread('3.bmp')
cv2.imshow('1.jpg',p1)
cv2.imshow('2.png',p2)
cv2.imshow('3.bmp',p3)
cv2.waitKey()