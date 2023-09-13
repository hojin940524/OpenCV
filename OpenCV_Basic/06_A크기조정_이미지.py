##크키 조정 - 이미지

import cv2

##고정 크키로 설정
img = cv2.imread('carrot.jpg')
cv2.imshow('img_fix', img)

dst_fix = cv2.resize(img, (400, 500)) # width, height 고정 크기
cv2.imshow('resize_fix', dst_fix)

##비율로 설정
dst_ratio = cv2.resize(img, None, fx=0.5, fy=0.5) # x, y 비율 정의 (0.5 배로 축소)
cv2.imshow('resize_ratio', dst_ratio)

##보간법
# cv2.INTER_AREA : 크기 줄일 때 사용
dst_reduction = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA) # x, y 비율 정의 (0.5 배로 축소)
cv2.imshow('resize_reduction', dst_reduction)

# cv2.INTER_CUBIC : 크기 늘릴 때 사용 (속도 느림, 퀄리티 좋음)
# cv2.INTER_LINEAR : 크기 늘릴 때 사용 (기본값)
dst_plus = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC) # x, y 비율 정의 (1.5 배로 확대)
cv2.imshow('resize_plus', dst_plus)


cv2.waitKey(0)
cv2.destroyAllWindows()