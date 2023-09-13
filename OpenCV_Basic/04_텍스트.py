##텍스트

import cv2
import numpy as np

img = np.zeros((480, 640, 3), dtype=np.uint8)

SCALE = 1 # 크기
COLOR = (255, 255, 255) # 흰색
THICKNESS = 1 # 두께

#putText(그릴위치, 텍스트 내용, 시작 위치, 폰트 종류, 크기, 색깔, 두께)
cv2.putText(img, "Nado Simplex", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, SCALE, COLOR, THICKNESS)
cv2.putText(img, "Nado Plain", (20, 150), cv2.FONT_HERSHEY_PLAIN, SCALE, COLOR, THICKNESS)
cv2.putText(img, "Nado Script Simplex", (20, 250), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, SCALE, COLOR, THICKNESS)
cv2.putText(img, "Nado Triplex", (20, 350), cv2.FONT_HERSHEY_TRIPLEX, SCALE, COLOR, THICKNESS)
cv2.putText(img, "Nado Italic", (20, 450), cv2.FONT_HERSHEY_TRIPLEX | cv2.FONT_ITALIC, SCALE, COLOR, THICKNESS)

cv2.imshow('img', img)


##한글
img2 = np.zeros((480, 640, 3), dtype=np.uint8)

SCALE2 = 1 # 크기
COLOR2 = (255, 255, 255) # 흰색
THICKNESS2 = 1 # 두께

cv2.putText(img2, "호지니", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, SCALE2, COLOR2, THICKNESS2)
cv2.imshow('img2', img2)

##한글 우회 방법
from PIL import ImageFont, ImageDraw, Image #PIL - python image library
def myPutText(src, text, pos, font_size, font_color):
    img_pil = Image.fromarray(src)
    draw = ImageDraw.Draw(img_pil)
    font = ImageFont.truetype('fonts/gulim.ttc', font_size)
    draw.text(pos, text, font=font, fill=font_color)
    return np.array(img_pil)

img3 = np.zeros((480, 640, 3), dtype=np.uint8)

FONT_SIZE3 = 30
COLOR3 = (255, 255, 255) # 흰색

# cv2.putText(img, "호진", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, SCALE, COLOR, THICKNESS)
img3 = myPutText(img3, "호진", (20, 50), FONT_SIZE3, COLOR3)
cv2.imshow('img3', img3)


cv2.waitKey(0)
cv2.destroyAllWindows()
