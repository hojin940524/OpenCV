##이미지변형(이진화)

##그림판에서 제작한 이미지로 확인
import cv2

def empty(pos):
    # print(pos)
    pass

img = cv2.imread('threshold.png', cv2.IMREAD_GRAYSCALE)

name = 'Trackbar'
cv2.namedWindow(name)

cv2.createTrackbar('threshold', name, 127, 255, empty)  # bar 이름, 창의 이름, 초기값, 최대값, 이벤트 처리

while True:
    thresh = cv2.getTrackbarPos('threshold', name)  # bar 이름, 창의 이름
    ret, binary = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)

    if not ret:
        break

    cv2.imshow('img', img)
    cv2.imshow(name, binary)
    if cv2.waitKey(1) == ord('q'):
        break

#
img2 = cv2.imread('threshold.png', cv2.IMREAD_GRAYSCALE)

ret, binary1 = cv2.threshold(img2, 0, 255, cv2.THRESH_BINARY) # 진한 회색, 밝은 회색, 흰색
ret, binary2 = cv2.threshold(img2, 127, 255, cv2.THRESH_BINARY) # 밝은 회색, 흰색
ret, binary3 = cv2.threshold(img2, 195, 255, cv2.THRESH_BINARY) # 흰색

cv2.imshow('img2', img2)
cv2.imshow('binary1', binary1)
cv2.imshow('binary2', binary2)
cv2.imshow('binary3', binary3)
cv2.waitKey(0)


cv2.destroyAllWindows()