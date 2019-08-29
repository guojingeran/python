import cv2
import numpy as np

def getBGR(img, meitu_map, i, j):
    # 读取原图中像素点的BGR值
    b, g, r = img[i][j]
    # 计算标准颜色表中颜色的位置坐标
    x = int(g/4 + int(b/32)*64)
    y = int(r/4 + int((b%32)/4)*64)
    # 返回滤镜颜色表中对应位置的颜色，完成映射
    return meitu_map[x][y]

# 依次载入原图、标准颜色图和滤镜颜色图
img = cv2.imread('C:\\python\\opencv\\meizi.jpg')
color_map = cv2.imread('C:\\python\\opencv\\lookup-table.png')
meitu_map = cv2.imread('C:\\python\\opencv\\meitu-table.png')

# 双层for循环替换原图每个像素点的颜色
for i in range(len(img)):
    for j in range(len(img[1])):
        img[i][j] = getBGR(img, meitu_map, i, j)

cv2.imwrite('C:\\python\\opencv\\meitu.jpg', img)
cv2.imshow('meitu', img)
cv2.waitKey(0)
cv2.destroyAllWindows()