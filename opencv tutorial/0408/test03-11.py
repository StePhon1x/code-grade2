import os
import cv2

base_path = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(base_path, "opencv_logo.jpg")

image = cv2.imread(image_path)

# 3. crop
# if image is None:
#     print("图片读取失败，请检查路径是否正确")
# else:
#     crop = image[10:170, 40:200]
#     cv2.imshow("crop", crop)
#     cv2.waitKey()

# 4. draw
# import numpy as np

# image = np.zeros([300, 300, 3], dtype=np.uint8)

# cv2.line(image, (100,200), (250,250), (250,0,0), 2) #起点 终点 颜色
# cv2.rectangle(image, (30,100), (60,150), (0,255,0),2) #第一个顶点 对角顶点 颜色
# cv2.circle(image, (150, 100), 20, (0, 0, 255), 3) #圆心 半径 颜色

# cv2.putText(image, "hello", (100,50), 0, 1, (255,255,255), 2, 1)
# # 起点 字体类型 缩放系数 颜色 粗细 线条类型

# cv2.imshow("image", image)
# cv2.waitKey()

# 5. blur
# gauss = cv2.GaussianBlur(image, (5, 5), 0) #内核像素
# median = cv2.medianBlur(image, 5)
# cv2.imshow("image", image)
# cv2.imshow("gauss", gauss)
# cv2.imshow("median", median)

# cv2.waitKey()

# 6. corner
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# corners = cv2.goodFeaturesToTrack(gray, 500, 0.1, 10)
# for corner in corners:
#     x, y  = corner.ravel()
#     cv2.circle(image, (int(x), int(y)), 3, (255, 0, 255), -1)
#     # 图像、圆心、半径 3、颜色品红色 (255, 0, 255)、-1 表示填充

# cv2.imshow("corners", image)
# cv2.waitKey()

# 7. match
# import numpy as np

# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# template = gray[75:105, 235:265]
# # 从灰度图中裁出一小块区域作为"模板"（就是那个菱形），格式是 [y1:y2, x1:x2]，这里裁出了一个 30×30 的小图。

# match = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
# locations = np.where(match >= 0.9)
# # 用 TM_CCOEFF_NORMED（标准相关系数）算法，在整张图上滑动模板，逐像素计算相似度，结果是一个二维数组，每个值在 -1~1 之间，越接近 1 越相似。

# w, h = template.shape[0:2]
# for p in zip(*locations[::-1]): #locations[::-1] — 把 (行, 列) 翻转成 (列, 行)，即 (x, y), zip(*) — 将两个数组打包成坐标对
#     x1, y1 = p[0], p[1]
#     x2, y2 = x1 + w, y1 + h
#     cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

# cv2.imshow("image", image)
# cv2.waitKey()

# 8. gradient
# gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# # 1. 使用拉普拉斯算子（检测边缘——梯度剧烈变化处）
# laplacian = cv2.Laplacian(gray, cv2.CV_64F)

# # 2. canny边缘检测（定义边缘为梯度区间）
# # 梯度大于200 -> 变化足够强烈，确定是边缘
# # 梯度小于100 -> 变化较为平缓，确定非边缘
# # 梯度介于二者之间 -> 待定，看其是否与已知的边缘像素相邻
# canny = cv2.Canny(gray, 100, 200)

# cv2.imshow("gray", gray)
# cv2.imshow("laplacian", laplacian)
# cv2.imshow("canny", canny)

# cv2.waitKey()

# 9. threshold

# 1. 图片灰度二值化
# gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
# ret, binary = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY) 
# #全局固定阈值二值化：遍历每个像素，像素值 > 10 则设为 255（白），否则设为 0（黑）。阈值 10 是手动指定的，返回值 ret 就等于 10。

# # 2. 图片自适应二值化（划分区块二值化，效果更好）
# binary_adaptive = cv2.adaptiveThreshold(
#     gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
# # 255：像素超过阈值时赋的最大值
# # cv2.ADAPTIVE_THRESH_GAUSSIAN_C：用区块内像素的高斯加权平均作为阈值基准（中心像素权重更高）
# # 115：区块大小（必须为奇数），即 115×115 像素的邻域
# # 1：从计算出的均值中减去的常数，用于微调阈值

# # 3. 大津算法（基于图片灰度聚类分析，自定义阈值）
# ret1, binary_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# 大津（Otsu）算法：自动分析图像灰度直方图，找到一个最优阈值，使二值化后前景与背景的类间方差最大（即分得最开）。
# gray, 0 中的 0 只是占位，真正的阈值由算法计算后存入 ret1。

# cv2.imshow("gray", gray)
# cv2.imshow("binary", binary)
# cv2.imshow("adaptive", binary_adaptive)
# cv2.imshow("otsu", binary_otsu)

# cv2.waitKey()


# 10. morphology 图像的形态学算法（腐蚀和膨胀）
# import numpy as np

# gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# # 腐蚀和膨胀前先将图片二值化
# ret, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV) # 反向二值

# kernel = np.ones((5, 5), np.uint8)

# # 腐蚀和膨胀操作
# erosions = cv2.erode(binary, kernel)
# dilations = cv2.dilate(binary, kernel)

# cv2.imshow("erosions", erosions)
# cv2.imshow("dilations", dilations)
# cv2.imshow("binary", binary)

# cv2.waitKey()



# 11. camera

# capture = cv2.VideoCapture(0)

# ret = True

# while ret:
#     ret, frame = capture.read()
#     cv2.imshow("camera", frame)

#     # ret：这是一个布尔值，表示读取操作是否成功。
#     # 如果 ret 为 True，表示成功读取了一帧图像；如果为 False，则表示读取失败，可能是因为视频流结束或者其他错误。
#     # 在处理视频流时，这个返回值通常用于控制循环，直到视频流结束。

#     # frame：这是一个NumPy数组，代表了从视频捕获对象读取的当前帧。
#     # 这个数组通常是一个三维的，其形状为 (高度, 宽度, 通道数)，其中通道数可以是1（灰度图像）或3（彩色图像，分别对应红、绿、蓝通道）。

#     key = cv2.waitKey(1)
#     if key != -1:
#         break

# capture.release()












