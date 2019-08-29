import numpy as np
import cv2

img1 = cv2.imread('C:\\Users\\liu\\Documents\\python\\opencv\\image\\test1.jpg')
img2 = cv2.imread('C:\\Users\\liu\\Documents\\python\\opencv\\image\\test2.jpg')

srcImg = cv2.copyMakeBorder(img1, 0, 0, 0, 200, cv2.BORDER_CONSTANT, value=(0, 0, 0))
testImg = cv2.copyMakeBorder(img2, 0, 0, 200, 0, cv2.BORDER_CONSTANT, value=(0, 0, 0))
img1gray = cv2.cvtColor(srcImg, cv2.COLOR_BGR2GRAY)
img2gray = cv2.cvtColor(testImg, cv2.COLOR_BGR2GRAY)
# 将Hessian Threshold设置为400,阈值越大能检测的特征就越少
hessian = 400
surf = cv2.xfeatures2d.SURF_create(hessian)

# 查找关键点和描述符
kp1, des1 = surf.detectAndCompute(img1gray, None)
kp2, des2 = surf.detectAndCompute(img2gray, None)

# 绘制特征点
feature1 = cv2.drawKeypoints(img1, kp1, None, (255, 0, 0))
feature2 = cv2.drawKeypoints(img2, kp2, None, (255, 0, 0))

# 建立FLANN匹配器的参数
FLANN_INDEX_KDTREE = 1
# 配置索引，密度树的数量为5
indexParams = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
# 指定递归次数
searchParams = dict(checks=50)
# 建立匹配器
flann = cv2.FlannBasedMatcher(indexParams, searchParams)
# 得出匹配的特征点
matches = flann.knnMatch(des1, des2, k=2)
matchesMask = [[0, 0] for i in range(len(matches))]

good = []
pts1 = []
pts2 = []
# ratio test as per Lowe's paper
for i, (m, n) in enumerate(matches):
    if m.distance < 0.7*n.distance:
        good.append(m)
        pts2.append(kp2[m.trainIdx].pt)
        pts1.append(kp1[m.queryIdx].pt)
        matchesMask[i] = [1, 0]

draw_params = dict(matchColor=(0, 255, 0),
                    singlePointColor=(255, 0, 0),
                    matchesMask=matchesMask,
                    flags=0)
img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, matches, None, **draw_params)

rows, cols = srcImg.shape[:2]
# 查询图像的特征描述子索引
src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
# 训练(模板)图像的特征描述子索引
dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
warpImg = cv2.warpPerspective(testImg, np.array(M), (testImg.shape[1], testImg.shape[0]), flags=cv2.WARP_INVERSE_MAP)

for col in range(0, cols):
    if srcImg[:, col].any() and warpImg[:, col].any():
        left = col
        break
for col in range(cols-1, 0, -1):
    if srcImg[:, col].any() and warpImg[:, col].any():
        right = col
        break

res = np.zeros([rows, cols, 3], np.uint8)
for row in range(0, rows):
    for col in range(0, cols):
        if not srcImg[row, col].any():
            res[row, col] = warpImg[row, col]
        elif not warpImg[row, col].any():
            res[row, col] = srcImg[row, col]
        else:
            srcImgLen = float(abs(col - left))
            testImgLen = float(abs(col - right))
            alpha = srcImgLen / (srcImgLen + testImgLen)
            res[row, col] = np.clip(srcImg[row, col] * (1-alpha) + warpImg[row, col] * alpha, 0, 255)
            
cv2.imshow('connect', img3)
cv2.imshow('result', res)
cv2.waitKey()
cv2.destroyAllWindows()