import cv2

img = cv2.imread('C:/Users/Administrator/Documents/python/opencv/meizi.jpg')
# 读取图像信息
height, width, colors = img.shape

# 水印信息设置
water_mark = 'Hello,郭靖愕然'
font = cv2.FONT_HERSHEY_COMPLEX
x = width - 120
y = height - 25

#各参数依次是：照片/添加的文字/左下角坐标/字体/字体大小/颜色/字体粗细
new_img = cv2.putText(img, water_mark, (x, y), font, 0.5, (0, 0, 255), 1)

cv2.imshow('image', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()