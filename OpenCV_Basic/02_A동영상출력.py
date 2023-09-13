import cv2

##동영상 파일 출력
cap = cv2.VideoCapture('cat.mp4') #동영상 불러오기

while cap.isOpened(): #동영상 파일이 올바르게 열였는지 확인
    ret, frame = cap.read() #ret: 성공여부, frame: 받아온 이미지(프레임)
    if not ret:
        print("동영상을 불러오지 못하였습니다.")
        break

    cv2.imshow('cat_video', frame)

    if cv2.waitKey(1) == ord('q'): #q를 입력하였을때 종료
        print("사용자 입력에 의해 종료합니다.")
        break

cap.relase() #자원 해제
cv2.destroyAllWindows() #모든 창 닫기