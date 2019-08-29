import cv2
import numpy as np

# Read images : src image will be cloned into dst
img = cv2.imread('C:\\Users\\liu\\Documents\\python\\opencv\\beach.jpg')
obj= cv2.imread('C:\\Users\\liu\\Documents\\python\\opencv\\littlegirl.jpg')

#obj = cv2.resize(obj, None, fx=0.8, fy=0.8, interpolation=cv2.INTER_CUBIC)

gray = cv2.cvtColor(obj, cv2.COLOR_BGR2GRAY)

height_1, width_1 = img.shape[:2]
height_2, width_2 = obj.shape[:2]

# 设置ROI
r1 = height_1 - height_2
r2 = height_1
c1 = width_1 - width_2 -50
c2 = width_1 -50
#roi = img[r1:r2, c1:c2]


# Create an all white mask
mask = 255 * np.ones(obj.shape, obj.dtype)
center = (int(c1/2+c2/2), int(r1/2+r2/2))
# The location of the center of the src in the dst
#center = (1090, 700)
#center = (n + int(c2/2), m + int(r2/2))
#print(m,n)

# Seamlessly clone src into dst and put the results in output
normal_clone = cv2.seamlessClone(obj, img, mask, center, cv2.NORMAL_CLONE)
mixed_clone = cv2.seamlessClone(obj, img, mask, center, cv2.MIXED_CLONE)

# Write results
cv2.imwrite('C:\\Users\\liu\\Documents\\python\\opencv\\clone.jpg', normal_clone)
cv2.imwrite('C:\\Users\\liu\\Documents\\python\\opencv\\clone_mixed.jpg', mixed_clone)