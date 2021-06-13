import cv2
import numpy as np
from PIL import Image, ImageFont, ImageDraw


def image_in(img, text):
    PATH = 'C:\Windows\Fonts\meiryo.ttc'
    SIZE = 64
    font = ImageFont.truetype(PATH, SIZE)
    img = Image.fromarray(img)
    draw = ImageDraw.Draw(img)

    draw.text((100,100), text, font=font, fill=(0,0,255,0))
    img = np.array(img)
    return img


image = cv2.imread('arai11.jpg')
print(image.shape)
#b = image[:,:,0]
#g = image[:,:,1]
#r = image[:,:,2]

#cv2.namedWindow("arai", cv2.WINDOW_NORMAL)
image = cv2.resize(image, dsize=(500,800))
#cv2.putText(image, 'sexy',(100,100), cv2.FONT_HERSHEY_COMPLEX, 4,(0,0,255), 4, cv2.LINE_AA )
text = 'かわいい'
image = image_in(image, text)

cv2.imshow('arai', image)

#cv2.imshow('blue', b)
#cv2.imshow('green', g)
#cv2.imshow('red', r)

cv2.waitKey(0)
cv2.destroyAllWindows()

