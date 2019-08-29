import cv2

# 加载图片
image = cv2.imread('C:/Users/Administrator/Documents/script/NeuralNetwork/opencv/girl.png')

# 转换成灰度，提高计算速度
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# 加载Haar特征分类器
face_cascade = cv2.CascadeClassifier('C:/Users/Administrator/Documents/script/NeuralNetwork/opencv/haarcascade_frontalface_default.xml')

# 探检测图片中的人脸
faces = face_cascade.detectMultiScale(
    gray,                # 要检测的图像
    scaleFactor = 1.15,  # 图像尺寸每次缩小的比例
    minNeighbors = 3,    # 一个目标至少要被检测到3次才会被标记为人脸
    minSize = (5,5)      # 目标的最小尺寸
)

# 为每个人脸绘制矩形框
for(x,y,w,h) in faces:
   cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('image',image)
cv2.waitKey(0)
