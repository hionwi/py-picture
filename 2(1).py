import cv2
p1=cv2.imread('a.png',-1)
a=p1[:,:,3]
cv2.imshow('a',a)
cv2.waitKey()
