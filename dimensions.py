'''
A simple Program for grabing video from basler camera and converting it to opencv img.
Tested on Basler acA1300-200uc (USB3, linux 64bit , python 3.5)
'''
from pypylon import pylon
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import matplotlib.pyplot as plt

# conecting to the first available camera
camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
camera.Open()
# camera.ExposureAuto.SetValue(0)
# pylon.FeaturePersistence.Load('settings.pfs', camera.GetNodeMap(), True)
# Grabing Continusely (video) with minimal delay
camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 
converter = pylon.ImageFormatConverter()

# converting to opencv bgr format
converter.OutputPixelFormat = pylon.PixelType_BGR8packed
converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

bckgrnd = cv2.createBackgroundSubtractorMOG2()
ref_img = None
frame_count = 0
cv2.namedWindow('title', cv2.WINDOW_NORMAL)
cv2.namedWindow('contour', cv2.WINDOW_NORMAL)
cv2.namedWindow('mask', cv2.WINDOW_NORMAL)

def order_points(pts):
	# initialzie a list of coordinates that will be ordered
	# such that the first entry in the list is the top-left,
	# the second entry is the top-right, the third is the
	# bottom-right, and the fourth is the bottom-left
	rect = np.zeros((4, 2), dtype = "float32")
	# the top-left point will have the smallest sum, whereas
	# the bottom-right point will have the largest sum
	s = pts.sum(axis = 1)
	rect[0] = pts[np.argmin(s)]
	rect[2] = pts[np.argmax(s)]
	# now, compute the difference between the points, the
	# top-right point will have the smallest difference,
	# whereas the bottom-left will have the largest difference
	diff = np.diff(pts, axis = 1)
	rect[1] = pts[np.argmin(diff)]
	rect[3] = pts[np.argmax(diff)]
	# return the ordered coordinates
	return rect


while camera.IsGrabbing():
    grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

    if grabResult.GrabSucceeded():
        frame_count += 1
        # Access the image data
        image = converter.Convert(grabResult)
        img2 = image.GetArray()
        matrix = np.load("cam_matrix.npz")
        mtx, dist, newcameramtx = matrix["mtx"],matrix["dist"], matrix["newcameramtx"]
        img2 = cv2.undistort(img2, mtx, dist, None, newcameramtx)
        img = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
        cv2.imshow('title', img2)
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            c = max(contours, key=cv2.contourArea)
            if cv2.contourArea(c)>(100*100): 
                rect = cv2.minAreaRect(c)
                _, size, _ = rect
                height, width = size
                print(f"Box Heigth and Width: {height/10.23} {width/10.23}")
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                cv2.drawContours(img,[box],0,(0,0,255),2)
        cv2.imshow('contour', img)
        cv2.imshow('mask', mask)
        k = cv2.waitKey(30)
        if k == ord('q'):
            break
        elif k == ord('b'):
            res = decode(img)
            print(res)

            # x = 460 mm height from camera to ground
            # fov = 48º of FOV
            # h: real horizontal viewing length
            # h = 2*x*tg(fov/2) = 409.61 mm
            # Resolution: 4192 x 3120
            # real width = 4192/409.61 = 10.23 px/mm

    grabResult.Release()
    
# Releasing the resource    
camera.StopGrabbing()

cv2.destroyAllWindows()