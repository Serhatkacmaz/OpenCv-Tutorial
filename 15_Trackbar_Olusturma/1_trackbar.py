import numpy as np
import cv2 as cv


def nothing(x):
    pass


# siyah pencere
img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow("image")
# trackbar oluşturma
# son parametre izleme çubuğu her değiştiğinde (callback function)
cv.createTrackbar('R', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('B', 'image', 0, 255, nothing)

# switch trackbar
switch = '0 : OFF \n 1 : ON'
cv.createTrackbar(switch, 'image', 0, 1, nothing)


while True:
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    # trackbar mevcut kounmlarını alma

    r = cv.getTrackbarPos('R', 'image')
    g = cv.getTrackbarPos('G', 'image')
    b = cv.getTrackbarPos('B', 'image')
    s = cv.getTrackbarPos(switch, 'image')

    # switch is off
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]


cv.destroyAllWindows()
