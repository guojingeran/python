import cv2
import math
import numpy as np

def rotate_about_center(src, angle, scale=1.):
    w = src.shape[1]
    h = src.shape[0]
    rangle = np.deg2rad(angle)  # angle in radians
    # now calculate new image width and height
    nw = (abs(np.sin(rangle)*h) + abs(np.cos(rangle)*w))*scale
    nh = (abs(np.cos(rangle)*h) + abs(np.sin(rangle)*w))*scale
    # ask OpenCV for the rotation matrix
    rot_mat = cv2.getRotationMatrix2D((nw*0.5, nh*0.5), angle, scale)
    # calculate the move from the old center to the new center combined
    # with the rotation
    rot_move = np.dot(rot_mat, np.array([(nw-w)*0.5, (nh-h)*0.5,0]))
    # the move only affects the translation, so update the translation
    # part of the transform
    rot_mat[0,2] += rot_move[0]
    rot_mat[1,2] += rot_move[1]
    return cv2.warpAffine(src, rot_mat, (int(math.ceil(nw)), int(math.ceil(nh))), flags=cv2.INTER_LANCZOS4, borderValue=(255, 255, 255))

#加载图片
image = cv2.imread('C:\\python\\opencv\\meizi.jpg')
glasses = cv2.imread('C:\\python\\opencv\\glasses.png')
height, width = image.shape[:2]

# 转换成灰度，提高计算速度
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# 加载Haar特征分类器
left_eye_cascade = cv2.CascadeClassifier('C:\\python\\opencv\\haarcascade_lefteye_2splits.xml')
right_eye_cascade = cv2.CascadeClassifier('C:\\python\\opencv\\haarcascade_righteye_2splits.xml')

# 探检测图片中的眼睛
left_eye = left_eye_cascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 5, minSize = (5,5))
right_eye = right_eye_cascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 5, minSize = (5,5))

# 双眼中心点的距离
d1 = right_eye[0][1] - left_eye[0][1]
d2 = right_eye[0][0] - left_eye[0][0]
distance = int(math.sqrt(d1*d1 + d2*d2))

# 眼睛缩放比例
scale = int(width/2*distance)
print(scale)

# 计算双眼连线与水平的角度,并对眼镜进行相同角度的旋转
r = (right_eye[0][1] - left_eye[0][1])/(right_eye[0][0] - left_eye[0][0])
degree = math.degrees(math.atan(-r))
glasses = rotate_about_center(glasses, degree, 1/11)

glasses_gray = cv2.cvtColor(glasses, cv2.COLOR_BGR2GRAY)
#print(glass.shape)

ret, _mask= cv2.threshold(glasses_gray, 200, 255, cv2.THRESH_BINARY) 
h, w = glasses.shape[:2]
rows = left_eye[0][1]
cols = left_eye[0][0]
# 双眼中心，也是ROI中心
eye_center_x = int((left_eye[0][0] + right_eye[0][0] + left_eye[0][2])/2)
eye_center_y = int((left_eye[0][1] + right_eye[0][1] + left_eye[0][3])/2)

# ROI区域
r_1 = eye_center_y - int(h/2) + 10
c_1 = eye_center_x - int(w/2)
roi = image[r_1:r_1 + h, c_1:c_1 + w]
_mask_inv = cv2.bitwise_not(_mask)

glasses_fg = cv2.bitwise_and(roi, roi, mask=_mask)
img_bg = cv2.bitwise_and(glasses, glasses, mask=_mask_inv)
dst = cv2.add(img_bg, glasses_fg)

image[r_1:r_1 + h, c_1:c_1 + w] = dst
cv2.imwrite('C:\\python\\opencv\\meizi_glasses.jpg', image)
cv2.imshow('rotate', image)
cv2.waitKey(0)
cv2.destroyAllWindows()