import numpy as np
import cv2
from matplotlib import pyplot as plt


# 图像处理，将logo图标叠加到一张图片的右下角，要求有颜色的区域为不透明

# 载入待处理图像和水印logo
img = cv2.imread('C:\\Users\\liu\\Documents\\python\\opencv\\girl.jpg')
logo = cv2.imread('C:\\Users\\liu\\Documents\\python\\opencv\\logo.jpg')
logo = cv2.resize(logo, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_NEAREST)
logo_rows, logo_cols = logo.shape[:2]
img_rows, img_cols = img.shape[:2]

# 对logo进行处理，生成遮罩mask
logo_gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(logo_gray, 200, 255, cv2.THRESH_BINARY)  # 二值化函数
mask_inv = cv2.bitwise_not(mask)

# 提取目标图片的ROI
r1 = img_rows - logo_rows - 20
c1 = img_cols - logo_cols - 20
r2 = r1 + logo_rows
c2 = c1 + logo_cols
roi = img[r1:r2, c1:c2]

# ROI和Logo图像融合
img_bg = cv2.bitwise_and(roi, roi, mask=mask)
logo_fg = cv2.bitwise_and(logo, logo, mask=mask_inv)
dst = cv2.add(img_bg, logo_fg)
img[r1:r2, c1:c2] = dst

cv2.imwrite('C:\\Users\\liu\\Documents\\python\\opencv\\logo_logo.jpg', img)
cv2.imshow("logo", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
# 显示图片，调用matplotlib展示
plt.figure()
titles = ["logo", "logo_gray", "mask", "mask_inv", "roi", "img_bg", "logo_fg", "dst"]
imgs = [logo, logo_gray, mask, mask_inv, roi, img_bg, logo_fg, dst]
for x in range(len(imgs)):
    plt.subplot(241 + x), plt.imshow(imgs[x]), plt.title(titles[x])
plt.show()
'''