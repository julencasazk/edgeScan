import cv2 

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    if not ret:
        print("No hay ret jajaj")
        break
    cv2.imshow("yoyo", frame)
    cv2.waitKey(0)