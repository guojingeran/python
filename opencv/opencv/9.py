import numpy as np
import cv2

# 载入背景图像和人物图像
img = cv2.imread('C:\\python\\opencv\\beach.jpg')
obj = cv2.imread('C:\\python\\opencv\\littlegirl.jpg')
height_1, width_1 = img.shape[:2]
height_2, width_2 = obj.shape[:2]

# 设置ROI
r1 = height_1 - height_2
r2 = height_1
c1 = width_1 - width_2 -50
c2 = width_1 -50
roi = img[r1:r2, c1:c2]

# 对人物图进行处理，生成蒙层mask
hsv = cv2.cvtColor(obj, cv2.COLOR_BGR2HSV)
lower_blue = np.array([90, 43, 46])
upper_blue = np.array([124, 255, 255])
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
mask_inv = cv2.bitwise_not(mask_blue)

# ROI和人物图像的融合
img_bg = cv2.bitwise_and(roi, roi, mask=mask_blue)
obj_fg = cv2.bitwise_and(obj, obj, mask=mask_inv)
dst = cv2.add(img_bg, obj_fg)
mask = 255 * np.ones(obj.shape, obj.dtype)

center = (int(c1/2+c2/2), int(r1/2+r2/2))

img = cv2.seamlessClone(dst, img, mask, center, cv2.NORMAL_CLONE)

cv2.imwrite('C:\\python\\opencv\\clone.png', img)
cv2.waitKey(0)
cv2.destroyAllWindows()