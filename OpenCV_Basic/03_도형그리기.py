##도형그리기
import cv2
import numpy as np

##01 빈 스케치북 만들기
img1 = np.zeros((480, 640, 3), dtype=np.uint8) #세로 480 x 가로 640, 3 Channel (RGB) 에 해당하는 스케치북 만들기
img1[:] = (255, 255, 255) # 전체 공간을 흰 색으로 채우기
#print(img)
cv2.imshow('img1', img1)

##02 일부 영역 색칠
img2 = np.zeros((480, 640, 3), dtype=np.uint8)
img2[100:200, 200:300] = (255, 255, 255) #[세로영역, 가로영역]
#print(img)
cv2.imshow('img2', img2)

##03 직선
img3 = np.zeros((480, 640, 3), dtype=np.uint8)

COLOR3 = (0, 255, 255) # BGR : Yellow, 색깔
THICKNESS3 = 3 # 두께

cv2.line(img3, (50, 100), (400, 50), COLOR3, THICKNESS3, cv2.LINE_8) # 그릴 위치, 시작 점, 끝 점, 색깔, 두께, 선 종류
cv2.line(img3, (50, 200), (400, 150), COLOR3, THICKNESS3, cv2.LINE_4)
cv2.line(img3, (50, 300), (400, 250), COLOR3, THICKNESS3, cv2.LINE_AA)

cv2.imshow('img3', img3)

##04 원
img4 = np.zeros((480, 640, 3), dtype=np.uint8)

COLOR4 = (255, 255, 0) # BGR 옥색
RADIUS4 = 50 # 반지름
THICKNESS4 = 10 # 두께

cv2.circle(img4, (200, 100), RADIUS4, COLOR4, THICKNESS4, cv2.LINE_AA) # 속이 빈 원 # 그릴 위치, 원의 중심점, 반지름, 색깔, 두께, 선 종류
cv2.circle(img4, (400, 100), RADIUS4, COLOR4, cv2.FILLED, cv2.LINE_AA) # 꽉 찬 원

cv2.imshow('img4', img4)

##05 사각형
img5 = np.zeros((480, 640, 3), dtype=np.uint8)

COLOR5 = (0, 255, 0) # BGR 초록색
THICKNESS5 = 3 # 두께

cv2.rectangle(img5, (100, 100), (200, 200), COLOR5, THICKNESS5) # 속이 빈 사각형 # 그릴 위치, 왼쪽 위 좌표, 오른쪽 아래 좌표, 색깔, 두께
cv2.rectangle(img5, (300, 100), (400, 300), COLOR5, cv2.FILLED) # 꽉 찬 사각형

cv2.imshow('img5', img5)

##06 다각형
img6 = np.zeros((480, 640, 3), dtype=np.uint8)

COLOR6 = (0, 0, 255) # BGR 빨간색
THICKNESS6 = 3 # 두께

pts1 = np.array([[100, 100], [200, 100], [100, 200]])
pts2 = np.array([[200, 100], [300, 100], [300, 200]])

# cv2.polylines(img, [pts1], True, COLOR, THICKNESS, cv2.LINE_AA)
# cv2.polylines(img, [pts2], True, COLOR, THICKNESS, cv2.LINE_AA)
cv2.polylines(img6, [pts1, pts2], True, COLOR6, THICKNESS6, cv2.LINE_AA) # 속이 빈 다각형 # 그릴 위치, 그릴 좌표들, 닫힘 여부, 색깔, 두께, 선 종류

pts3 = np.array([[[100, 300], [200, 300], [100, 400]], [[200, 300], [300, 300], [300, 400]]])
cv2.fillPoly(img6, pts3, COLOR6, cv2.LINE_AA) # 꽉 찬 다각형 # 그릴 위치, 그릴 좌표들, 색깔, 선 종류

cv2.imshow('img6', img6)



cv2.waitKey(0)
cv2.destroyAllWindows()