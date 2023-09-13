##이미지변환(열림&닫힘)
import cv2
import numpy as np
kernel = np.ones((3, 3), dtype=np.uint8)

##열림(Opening): 침식 후 팽창. 깎아서 노이즈 제거 후 살찌움
img_opening = cv2.imread('erode.png', cv2.IMREAD_GRAYSCALE)

erode_opening = cv2.erode(img_opening, kernel, iterations=3)
dilate_opening = cv2.dilate(erode_opening, kernel, iterations=3)

cv2.imshow('img_opening', img_opening)
cv2.imshow('erode_opening', erode_opening)
cv2.imshow('dilate_opening', dilate_opening)

##닫힘(Closing) : 팽창 후 침식. 구멍을 메운 후 다시 깎음
img_closing = cv2.imread('dilate.png', cv2.IMREAD_GRAYSCALE)

dilate_closing = cv2.dilate(img_closing, kernel, iterations=3)
erode_closing = cv2.erode(dilate_closing, kernel, iterations=3)

cv2.imshow('img_closing', img_closing)
cv2.imshow('dilate_closing', dilate_closing)
cv2.imshow('erode_closing', erode_closing)


cv2.waitKey(0)
cv2.destroyAllWindows()