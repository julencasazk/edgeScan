import sys

import cv2 as cv

thresh = 0
blockSize = 0
value = 0
thresh1 = 0
thresh2 = 0


def onChange(pos):
    global thresh

    thresh = cv.getTrackbarPos("thresh", "threshold")
    _, mat = cv.threshold(img, thresh, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
    cv.imshow("threshold", mat)


def onChange1(pos):
    global blockSize
    global value

    blockSize = cv.getTrackbarPos("blockSize", "threshold")
    mat = cv.adaptiveThreshold(
        img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, blockSize, value)
    cv.imshow("threshold", mat)


def onChange2(pos):
    global blockSize
    global value

    value = pos - 255
    mat = cv.adaptiveThreshold(
        img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, blockSize, value)
    cv.imshow("threshold", mat)


def onChange3(pos):
    global thresh1
    global thresh2

    thresh1 = pos
    mat = cv.Canny(img, thresh1, thresh2)
    cv.imshow("threshold", mat)


def onChange4(pos):
    global thresh1
    global thresh2

    thresh2 = pos
    mat = cv.Canny(img, thresh1, thresh2)
    cv.imshow("threshold", mat)

# DOWNLOAD IMAGES BEFOREHAND
    
# img = cv.imread("Image__2021-10-29__17-57-17_dim.png")
img = cv.imread("6_S_3.png")
# img = cv.imread("6_S_6.png")

if img is None:
    sys.exit(1)

img = cv.resize(img, (960, 540))
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img = cv.GaussianBlur(img, (7, 7), 0)

cv.namedWindow("threshold", cv.WINDOW_FREERATIO)
# cv.createTrackbar("thresh", "threshold", 0, 1000, onChange)
# cv.createTrackbar("blockSize", "threshold", 0, 1000, onChange1)
# cv.createTrackbar("C", "threshold", 0, 255*2, onChange2)
cv.createTrackbar("thresh1", "threshold", 0, 255, onChange3)
cv.createTrackbar("thresh2", "threshold", 0, 255, onChange4)
# img = cv.adaptiveThreshold(
#     img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 101, 20)
cv.imshow("threshold", img)
cv.waitKey()
cv.destroyAllWindows()
