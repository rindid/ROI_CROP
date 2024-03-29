import cv2
import numpy as np
import os

path = os.getcwd()
large = cv2.imread(path+'\image\\test.png')
#rgb = cv2.pyrDown(large)
rgb=large
small = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
grad = cv2.morphologyEx(small, cv2.MORPH_GRADIENT, kernel)
_, bw = cv2.threshold(grad, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 1))
connected = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, kernel)
#cv2.imshow('connected', connected)
# using RETR_EXTERNAL instead of RETR_CCOMP
contours, hierarchy = cv2.findContours(connected.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
mask = np.zeros(bw.shape, dtype=np.uint8)
morph = np.zeros(bw.shape, dtype=np.uint8)
for idx in range(len(contours)):
    x, y, w, h = cv2.boundingRect(contours[idx])
    mask[y:y+h, x:x+w] = 0
    cv2.drawContours(mask, contours, idx, (255, 255, 255), -1)
    r = float(cv2.countNonZero(mask[y:y+h, x:x+w])) / (w * h)
    if r > 0.20 and w > 1 and h > 1:

        copy_box = np.zeros(bw.shape, dtype=np.uint8)
        copy_box[y:y+h, x:x+w]=connected[y:y+h, x:x+w]
        #cv2.imshow('copy', copy_box)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (int(h/3)+2, int(h/3)+1))
        morph_small = cv2.dilate(copy_box, kernel, iterations=1)
        #morph_small = cv2.morphologyEx(copy_box, cv2.MORPH_OPEN, kernel)
        morph=cv2.add(morph, morph_small)

        #cv2.rectangle(rgb, (x, y), (x+w-1, y+h-1), (0, 255, 0), 2)
#cv2.imshow('mor', morph)
contours2, hierarchy = cv2.findContours(morph.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
mask = np.zeros(bw.shape, dtype=np.uint8)
for idx in range(len(contours2)):
    x, y, w, h = cv2.boundingRect(contours2[idx])
    mask[y:y+h, x:x+w] = 0
    cv2.drawContours(mask, contours2, idx, (255, 255, 255), -1)
    r = float(cv2.countNonZero(mask[y:y+h, x:x+w])) / (w * h)
    if r > 0.20 and w > 10 and h > 10 and w*h>200:
        cv2.rectangle(rgb, (x, y), (x+w-1, y+h-1), (0, 255, 0), 2)


# show image with contours rect
cv2.imshow('rects', cv2.pyrDown(rgb))
cv2.imwrite(path+'\image\\result.png',rgb)
cv2.waitKey()
