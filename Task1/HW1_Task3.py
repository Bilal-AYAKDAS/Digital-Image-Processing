#Bilal Ayakdas 220316002
from matplotlib import pyplot as plt
import cv2 as cv

#Read Image
img = cv.imread('images/lighthouse.png')
cv.namedWindow('colored',cv.WINDOW_AUTOSIZE)
cv.imshow('colored',img)
cv.waitKey(0)

#Convert to gray scale image
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#Show grayscale image
cv.imshow('gray',gray)
cv.waitKey(0)

#Rotate  45 degree the image
rot_mat = cv.getRotationMatrix2D((img.shape[1] / 2, img.shape[0] / 2), 45, 1)
rotated_img = cv.warpAffine(img, rot_mat, (img.shape[1], img.shape[0]), flags=cv.INTER_CUBIC)

#Show rotated image
cv.imshow('rotated', rotated_img)
cv.waitKey(0)

#Draw the grayscale images's histogram
plt.figure()
plt.hist(gray)
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")
plt.title("Histogram of Grayscale Image")
plt.show()





