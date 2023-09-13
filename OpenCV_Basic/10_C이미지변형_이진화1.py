##이미지변형(이진화)
import cv2
img = cv2.imread('carrot.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('img', img)

##Threshold
ret, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('binary', binary)

##Trackbar (값 변화에 따른 변형 확인)

def empty(pos):
    # print(pos)
    pass

name = 'Trackbar'
cv2.namedWindow(name)

cv2.createTrackbar('threshold', name, 127, 255, empty)  # bar 이름, 창의 이름, 초기값, 최대값, 이벤트 처리

while True:
    thresh = cv2.getTrackbarPos('threshold', name)  # bar 이름, 창의 이름
    ret, binary = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)

    if not ret:
        break

    cv2.imshow(name, binary)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()