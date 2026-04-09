import os
import cv2

base_path = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(base_path, "opencv_logo.jpg")

# print(cv2.__version__)

image = cv2.imread(image_path)

if image is None:
    print("图片读取失败，请检查路径是否正确")
else:
    print(image.shape)  # 输出格式：(高, 宽, 通道数)，例如 (400, 600, 3)

cv2.imshow("image", image)
cv2.waitKey()












