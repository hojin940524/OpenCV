##이미지 자르기
import cv2

##이미지 영역을 잘라 새로운 윈도우(창)에 표시
img = cv2.imread('carrot.jpg')
crop1 = img[100:200, 200:400] # 세로 기준 100 : 200 까지, 가로 기준 200 : 400 까지 자름

cv2.imshow('img', img) # 원본 이미지
cv2.imshow('crop', crop1) # 잘린 이미지

##이미지 영역을 잘라 기존 윈도우(창)에 표시
img2 = cv2.imread('carrot.jpg')
crop2 = img2[100:200, 200:400] # 세로 기준 100 : 200 까지, 가로 기준 200 : 400 까지 자름
img2[100:200, 400:600] = crop2
cv2.imshow('img2', img2) # 원본 이미지


cv2.waitKey(0)
cv2.destroyAllWindows()