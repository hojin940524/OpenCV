##이미지검출(윤곽선)
#윤곽선: 경계선을 연결한 선

import cv2
img = cv2.imread('card.png')
target_img = img.copy() # 사본 이미지

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

### 윤곽선 찾기 모드
# 1) cv2.RETR_EXTERNAL : 가장 외곽의 윤곽선만 찾음
# 2) cv2.RETR_LIST : 모든 윤곽선 찾음 (계층 정보 없음)
# 3) cv2.RETR_TREE : 모든 윤곽선 찾음 (계층 정보를 트리 구조로 생성)

### 3번

contours, hierarchy = cv2.findContours(otsu, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print(hierarchy)
print(f'총 발견 갯수 : {len(contours)}')

COLOR = (0, 200, 0) # 녹색
cv2.drawContours(target_img, contours, -1, COLOR, 2)

cv2.imshow('img', img)
cv2.imshow('gray', gray)
cv2.imshow('otsu', otsu)
cv2.imshow('contour', target_img)

cv2.waitKey(0)
cv2.destroyAllWindows()