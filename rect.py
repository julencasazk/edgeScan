import cv2

# Load iamge, grayscale, adaptive threshold
cap = cv2.VideoCapture(0 + cv2.CAP_V4L2)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

def nothing(a):
    pass

cv2.namedWindow('thresh', cv2.WINDOW_FREERATIO)
cv2.namedWindow('opening', cv2.WINDOW_FREERATIO)
cv2.namedWindow('image', cv2.WINDOW_FREERATIO)
cv2.createTrackbar("thresh1", "image", 100, 500, nothing)
cv2.createTrackbar("thresh2", "image", 200, 500, nothing)
if cap.isOpened():
    # Window 
    while cv2.getWindowProperty('image',0) >= 0:
        _, image = cap.read()
        gray = image
        # gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        thresh = cv2.Canny(gray,cv2.getTrackbarPos("thresh1", "image"), cv2.getTrackbarPos("thresh2", "image"))
        # # Fill rectangular contours
        cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        for c in cnts:
            cv2.drawContours(image, [c], -1, (0,255,0), 3)

        # Morph open
        # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9,9))
        # opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=4)
        opening = thresh

        # Draw rectangles
        cnts = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        c = max(cnts, key=cv2.contourArea)
        # for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(image, (x, y), (x + w, y + h), (255,0,0), 3)

        cv2.imshow('thresh', thresh)
        cv2.imshow('opening', opening)
        cv2.imshow('image', image)
        cv2.waitKey(1)
