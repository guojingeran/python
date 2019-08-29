import cv2
import numpy as np


# 梯形图片的矫正
'''
SrcImg = cv2.imread('C:\\python\\opencv\\image\\newspaper.jpg')
SrcCanvas = np.zeros(SrcImg.shape, dtype=np.uint8)

SrcPoints = np.float32([[ 327.,  66.], [ 410.,  66.], [ 328.,  162.], [ 421.,  162.]])
CanvasPoints = np.float32([[0,0],[400,0],[0,600],[400,600]])
PerspectiveMatrix = cv2.getPerspectiveTransform(np.array(SrcPoints), np.array(CanvasPoints))
PerspectiveImg = cv2.warpPerspective(SrcImg, PerspectiveMatrix, (400, 600))

cv2.imshow('PerspectiveImg', PerspectiveImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# 广告牌的合成
srcImg = cv2.imread('C:\\python\\opencv\\image\\baby.jpg')
canvasImg = cv2.imread('C:\\python\\opencv\\image\\billboard.jpg')

# 图片透视变换
srcPoints = np.float32([[0,0],[800,0],[0,500],[800,500]])
canvasPoints = np.float32([[ 140., 52.], [ 335., 118.], [ 138., 218.], [ 336., 242.]])

perspectiveMatrix = cv2.getPerspectiveTransform(np.array(srcPoints), np.array(canvasPoints))
perspectiveImg = cv2.warpPerspective(srcImg, perspectiveMatrix, (800, 529))
cv2.imshow('PerspectiveImg', perspectiveImg)

# 制作mask
gray = cv2.cvtColor(perspectiveImg, cv2.COLOR_BGR2GRAY)
h, w = gray.shape
for i in range(h):
    for j in range(w):
        if not gray[i][j] == 0:
            gray[i][j] = 255

mask = cv2.bitwise_not(gray)

# 像素运算，图片合成
img_bg = cv2.bitwise_and(canvasImg, canvasImg, mask=mask)
img = cv2.add(img_bg, perspectiveImg)

#cv2.imshow('img_bg', img_bg)
#cv2.imshow('PerspectiveImg', perspectiveImg)
cv2.imshow('result', img)
#cv2.imwrite('C:\\python\\opencv\\image\\result.jpg', img)

cv2.waitKey(0)
cv2.destroyAllWindows()