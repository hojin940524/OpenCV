##이미지변형(흑백)
import cv2

##이미지를 흑백으로 읽음
img1 = cv2.imread('carrot.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('img1', img1)

##불러온 이미지를 흑백으로 변경
img2 = cv2.imread('carrot.jpg')
dst = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

cv2.imshow('img', img2)
cv2.imshow('gray', dst)


cv2.waitKey(0)
cv2.destroyAllWindows()