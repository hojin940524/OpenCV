##이미지변환(팽창)
#이미지를 확장하여 작은 구멍을 채움
#흰색 영역의 외곽 픽셀 주변에 흰색을 추가

import cv2
import numpy as np

kernel = np.ones((3, 3), dtype=np.uint8)
# kernel

img = cv2.imread('dilate.png', cv2.IMREAD_GRAYSCALE)
dilate1 = cv2.dilate(img, kernel, iterations=1) # 반복 횟수
dilate2 = cv2.dilate(img, kernel, iterations=2)
dilate3 = cv2.dilate(img, kernel, iterations=3)

cv2.imshow('gray', img)
cv2.imshow('dilate1', dilate1)
cv2.imshow('dilate2', dilate2)
cv2.imshow('dilate3', dilate3)

cv2.waitKey(0)
cv2.destroyAllWindows()