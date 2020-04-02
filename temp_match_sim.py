import cv2
import numpy as np
import os
import time

#input images to be compared 
img1='img/ron1.jpg'
img2='img/ron2.jpg'

#orb oriented fast and rotated brief
orb = cv2.ORB_create()

img1 = cv2.imread(img1,0)
img2 = cv2.imread(img2,0)
	
img1 = cv2.resize(img1, (600,600), interpolation = cv2.INTER_AREA)
img2 = cv2.resize(img2, (600,600), interpolation = cv2.INTER_AREA)
		
#to find key points and descriptors for each image
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)  #crosscheck is true will give best matching

matches = bf.match(des1,des2)
matches = sorted(matches,key=lambda x:x.distance)
		
top=5
#to show the output image
matchimg = cv2.drawMatches(img1, kp1, img2, kp2, matches[:top], None)
#to find the distance between images 
sums=0
for m in matches:
	sums+=m.distance
img3 = cv2.resize(matchimg, (1200,600), interpolation = cv2.INTER_AREA)
cv2.imshow("img3",img3)
cv2.imwrite("op.png", img3)

print("average distance of first and second image is ",sums/top)
	
cv2.waitKey(0)
cv2.destroyAllWindows(0)





























































