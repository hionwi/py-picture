import cv2
foreground=cv2.imread('a.png')
alpha=cv2.imread('alpha.jpg')
p2=cv2.imread('2.png')
background=cv2.resize(p2,(foreground.shape[1],foreground.shape[0]))
foreground = foreground.astype(float)
background = background.astype(float)
alpha = alpha.astype(float)/255
foreground = cv2.multiply(alpha, foreground)
background = cv2.multiply(1-alpha, background)
outImage = cv2.add(foreground, background)
cv2.imshow("outImg",outImage/255)
cv2.waitKey()
