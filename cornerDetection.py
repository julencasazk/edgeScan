'''
A simple Program for grabing video from basler camera and converting it to opencv img.
Tested on Basler acA1300-200uc (USB3, linux 64bit , python 3.5)
'''
from pypylon import pylon
import cv2
import numpy as np
from pyzbar.pyzbar import decode

def fourCornersSort(pts):
    """ Sort corners: top-left, bot-left, bot-right, top-right """
    # Difference and sum of x and y value
    # Inspired by http://www.pyimagesearch.com
    diff = np.diff(pts, axis=1)
    summ = pts.sum(axis=1)
    
    # Top-left point has smallest sum...
    # np.argmin() returns INDEX of min
    return np.array([pts[np.argmin(summ)],
                     pts[np.argmax(diff)],
                     pts[np.argmax(summ)],
                     pts[np.argmin(diff)]])

# conecting to the first available camera
camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
camera.Open()
# camera.ExposureAuto.SetValue(0)
# pylon.FeaturePersistence.Load('settings_lights_on.pfs', camera.GetNodeMap(), True)
# Grabing Continusely (video) with minimal delay
camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 
converter = pylon.ImageFormatConverter()

# converting to opencv bgr format
converter.OutputPixelFormat = pylon.PixelType_BGR8packed
converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

bckgrnd = cv2.createBackgroundSubtractorMOG2()
ref_img = None
frame_count = 0
cv2.namedWindow('mask', cv2.WINDOW_NORMAL)
cv2.namedWindow('contour', cv2.WINDOW_NORMAL)
cv2.namedWindow('real', cv2.WINDOW_NORMAL)
cv2.namedWindow('barcode', cv2.WINDOW_NORMAL)
cv2.namedWindow('thresholded barcode', cv2.WINDOW_NORMAL)


while camera.IsGrabbing():
    grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

    if grabResult.GrabSucceeded():
        frame_count += 1
        # Access the image data
        image = converter.Convert(grabResult)
        img = image.GetArray()
        img = cv2.rotate(img, cv2.ROTATE_180)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(img, 170, 255, cv2.THRESH_BINARY) # Las sombras tienen valor 127
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        rectContours = []
        for contour in contours:
            perimeter = cv2.arcLength(contour, True)
            aproximation = cv2.approxPolyDP(contour, perimeter*0.01, True)
            if len(aproximation) == 4:
                rectContours.append(contour)
        if rectContours:
            c = max(rectContours, key=cv2.contourArea)
            if cv2.contourArea(c)>(100*100): 
                cv2.drawContours(img,[c],0,(0,0,255),2)
                points = fourCornersSort(c[:,0])
                points = points.astype(np.float32)

                height = max(np.linalg.norm(points[0] - points[1]),
                np.linalg.norm(points[2] - points[3]))
                width = max(np.linalg.norm(points[1] - points[2]),
                np.linalg.norm(points[3] - points[0]))

                finalPoints = np.array([[0,0],[0, height],[width,height],[width,0]], np.float32)
                m = cv2.getPerspectiveTransform(points, finalPoints)
                dsp = cv2.warpPerspective(img, m, (int(width), int(height)))
                # 
                # HACER OTSU THRESHOLD A LA IMAGEN PREPROCESADA
                _, threshdsp = cv2.threshold(dsp, 200, 255, cv2.THRESH_OTSU+cv2.THRESH_BINARY) # Las sombras tienen valor 127
                # BARRIDO DE ENFOQUE PARA ENFOCARLO AUTOMATICAMENTE
                # 
                cv2.imshow('barcode', dsp)
                cv2.imshow('thresholded barcode', threshdsp)

        cv2.imshow('contour', img)
        cv2.imshow('mask', mask)
        cv2.imshow('real', img)


        k = cv2.waitKey(30)
        if k == ord('q'):
            break
        elif k == ord('b'):
            res = decode(dsp)
            print(str(res)+"\n")
        elif k == ord('v'):
            res = decode(threshdsp)
            print(str(res)+"\n")



    grabResult.Release()
    
# Releasing the resource    
camera.StopGrabbing()

cv2.destroyAllWindows()