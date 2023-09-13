##이미지 회전
import cv2
img = cv2.imread('carrot.jpg')
cv2.imshow('img', img)

##시계방향/90도
rotate_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) # 시계 방향으로 90도 회전
cv2.imshow('rotate_90', rotate_90)

##180도 회전
ROTATE_180 = cv2.rotate(img, cv2.ROTATE_180) # 시계 방향으로 90도 회전
cv2.imshow('ROTATE_180', ROTATE_180)

##반시계방향/90도 (=시계방향/270도)
rotate_270 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE) # 시계 반대 방향으로 90도
cv2.imshow('rotate_270', rotate_270)


cv2.waitKey(0)
cv2.destroyAllWindows()