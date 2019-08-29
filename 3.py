import cv2
import numpy
from PIL import Image, ImageDraw, ImageFont

img_OpenCV = cv2.imread('C:/Users/Administrator/Documents/python/opencv/meizi.jpg')

# 读取图像信息
height, width, colors = img_OpenCV.shape

# 图像从OpenCV格式转换成PIL格式
img_PIL = Image.fromarray(cv2.cvtColor(img_OpenCV, cv2.COLOR_BGR2RGB))

# 水印属性设置
font = ImageFont.truetype('C:/Windows/Fonts/simsun.ttc', 20)
x = width - 150
y = height - 40
position = (x, y)
fillColor = (255,255,255)
water_mark = 'Hello,郭靖愕然'

# PIL添加文字
draw = ImageDraw.Draw(img_PIL)
draw.text(position, water_mark, font=font, fill=fillColor)

# 重新转换为OpenCV格式
img_OpenCV = cv2.cvtColor(numpy.asarray(img_PIL),cv2.COLOR_RGB2BGR)
cv2.imshow('water_mark',img_OpenCV)
cv2.waitKey(0)
cv2.destroyAllWindows()