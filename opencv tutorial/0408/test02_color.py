import os
import cv2

base_path = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(base_path, "opencv_logo.jpg")

image = cv2.imread(image_path)

if image is None:
    print("图片读取失败，请检查路径是否正确")
else:
    cv2.imshow("blue", image[:, :, 0])
    cv2.imshow("green", image[:, :, 1])
    cv2.imshow("red", image[:, :, 2])
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray", gray)
    
    cv2.waitKey()

    