import cv2
import numpy as np

# 提取感兴趣区域ROI
img = cv2.imread('C:\\python\\opencv\\xiaojiejie_logo.png')
roi = img[918:999, 455:681]
roi_hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

# 处理蓝色水印
# 设定蓝色HSV范围
lower_blue = np.array([100, 43, 46])
upper_blue = np.array([124, 255, 255])
# 创建蓝色水印蒙层
kernel = np.ones((3, 3), np.uint8)
mask_blue = cv2.inRange(roi_hsv, lower_blue, upper_blue)
# 对蓝色水印蒙层进行膨胀操作
dilate_blue = cv2.dilate(mask_blue, kernel, iterations=1)
# 修补蓝色水印
res_1 = cv2.inpaint(roi, dilate_blue, 5, flags=cv2.INPAINT_TELEA)

# 处理红色水印
lower_red = np.array([0, 43, 46])
upper_red = np.array([10, 255, 255])
res_1_hsv = cv2.cvtColor(res_1, cv2.COLOR_BGR2HSV)
mask_red = cv2.inRange(res_1_hsv, lower_red, upper_red)
dilate_red = cv2.dilate(mask_red, kernel, iterations=1)
res_2 = cv2.inpaint(res_1, dilate_red, 5, flags=cv2.INPAINT_TELEA)
img[918:999, 455:681] = res_2
cv2.imwrite('C:\\python\\opencv\\xiaojiejie_nologo.png', img)