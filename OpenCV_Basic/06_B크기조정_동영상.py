##크키 조정 - 동영상

import cv2

##고정 크기로 설정
cap = cv2.VideoCapture('cat.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_resized_fix = cv2.resize(frame, (400, 500)) # 고정크기
    cv2.imshow('video_fix', frame_resized_fix)
    if cv2.waitKey(1) == ord('q'):
        break

## 비율 설정
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_resized_ratio = cv2.resize(frame, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC) # 비율
    cv2.imshow('video_ratio', frame_resized_ratio)
    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()