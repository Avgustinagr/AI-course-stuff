import cv2
import numpy as np

img = cv2.imread('book2.jpg')
img_coords = np.array([
[173,  428],
[403,  435],
[146,  569],
[402,  576]
])

img_dst = cv2.imread('book1.jpg')
img_dst_coords = np.array([
[179,  429],
[407,  432],
[170,  583],
[407,  586]])

h, status = cv2.findHomography(img_coords, img_dst_coords)
img_out = cv2.warpPerspective(img, h, (img_dst.shape[1],img_dst.shape[0]))

cv2.imshow("Source Image", img)
cv2.imshow("Destination Image", img_dst)
cv2.imshow("Warped Source Image", img_out)
 
 #press esc to exit. (or kill -9 <pid> like i did 10 times before i figured out which key '0' is)
cv2.waitKey(0);