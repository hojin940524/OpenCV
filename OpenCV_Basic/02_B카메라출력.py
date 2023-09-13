import cv2

cap = cv2.VideoCapture(0)  # 0번째 카메라 장치 (Device ID)

if not cap.isOpened():  # 카메라가 잘 열리지 않은 경우
    exit()  # 프로그램 종료

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('camera', frame)
    if cv2.waitKey(1) == ord('q'):  # 사용자가 q 를 입력하면 종료
        break

cap.release()
cv2.destroyAllWindows()