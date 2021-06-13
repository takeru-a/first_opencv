import cv2
import numpy as np

fimg = cv2.imread('woman.jpg')
bimg = cv2.imread('apex.jpeg')
bimg = cv2.resize(bimg,dsize=(1080, 800))

hsv = cv2.cvtColor(fimg,cv2.COLOR_BGR2HSV)

#２値化
bin_img = cv2.inRange(hsv, (0, 8, 0), (255, 255, 255))
#cv2.imshow('g', bin_img)

contours, _ = cv2.findContours(bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

contour = max(contours, key=lambda x: cv2.contourArea(x))

mask = np.zeros_like(bin_img)
cv2.drawContours(mask, [contour], -1, color=255, thickness=-1)
#cv2.imshow('m', mask)

x, y = 100, 50  # 貼り付け位置

# 幅、高さは前景画像と背景画像の共通部分をとる
w = min(fimg.shape[1], bimg.shape[1] - x)
h = min(fimg.shape[0], bimg.shape[0] - y)

# 合成する領域
fg_roi = fimg[:h, :w]  # 前傾画像のうち、合成する領域
bg_roi = bimg[y : y + h, x : x + w]  # 背景画像のうち、合成する領域

# 合成する。
bg_roi[:] = np.where(mask[:h, :w, np.newaxis] == 0, bg_roi, fg_roi)
#cv2.imshow('f', fimg)
cv2.imshow('b', bimg)
cv2.waitKey(0)
cv2.destroyAllWindows
