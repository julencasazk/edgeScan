'''
A simple Program for grabing video from basler camera and converting it to opencv img.
Tested on Basler acA1300-200uc (USB3, linux 64bit , python 3.5)
'''
from pypylon import pylon
import cv2
import numpy
from pyzbar.pyzbar import decode

# conecting to the first available camera
camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
camera.Open()
# camera.ExposureAuto.SetValue(0)
pylon.FeaturePersistence.Load('settings.pfs', camera.GetNodeMap(), True)
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


while camera.IsGrabbing():
    grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

    if grabResult.GrabSucceeded():
        frame_count += 1
        # Access the image data
        image = converter.Convert(grabResult)
        img = image.GetArray()
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        if frame_count<15:
            print(f"Capturando Fondo: {frame_count}")
            mask = bckgrnd.apply(img, learningRate= -1)
        else:
            mask = bckgrnd.apply(img, learningRate= 0)
            _, mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY) # Las sombras tienen valor 127
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # No hace falta
        cv2.imshow('title', img)
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
            c = max(contours, key=cv2.contourArea)
            if cv2.contourArea(c)>(100*100): 
                rect = cv2.minAreaRect(c)
                _, size, _ = rect
                height, width = size
                print(f"Box Heigth and Width: {height} {width}")
                box = cv2.boxPoints(rect)
                box = numpy.int0(box)
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