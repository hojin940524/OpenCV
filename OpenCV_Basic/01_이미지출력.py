import cv2
print("opencv_version : ", cv2.__version__) #opencv 버전 확인

##이미지 출력
img = cv2.imread('carrot.jpg') #해당 경로의 파일 읽어오기
cv2.imshow('carrot img', img)

##shape - 이미지의 height, width, channel 정보
print("shape: ", img.shape) #세로, 가로, channel

##읽기 옵션
img_color = cv2.imread('carrot.jpg', cv2.IMREAD_COLOR) #cv2.IMREAD_COLOR : 컬러 이미지. 투명 영역은 무시 (기본값)
img_gray = cv2.imread('carrot.jpg', cv2.IMREAD_GRAYSCALE) #cv2.IMREAD_GRAYSCALE : 흑백 이미지
img_unchanged = cv2.imread('carrot.jpg', cv2.IMREAD_UNCHANGED) #cv2.IMREAD_UNCHANGED : 투명 영역까지 포함

cv2.imshow('img_color', img_color)
cv2.imshow('img_gray', img_gray)
cv2.imshow('img_unchanged', img_unchanged)


cv2.waitKey(0) #지정된 시간(ms) 동안 사용자 키 입력 대기
cv2.destroyAllWindows() #모든 창 닫기