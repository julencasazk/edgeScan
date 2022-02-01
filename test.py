'''
A simple Program for grabing video from basler camera and converting it to opencv img.
Tested on Basler acA1300-200uc (USB3, linux 64bit , python 3.5)
'''
from pypylon import pylon
import cv2

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

background = None

cv2.namedWindow('title', cv2.WINDOW_NORMAL)


while camera.IsGrabbing():
    grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

    if grabResult.GrabSucceeded():
        # Access the image data
        image = converter.Convert(grabResult)
        img = image.GetArray()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        if background is None:
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.imshow('title', img)
        else:
            img_blur = cv2.GaussianBlur(img, (5, 5), 0)
            background_blur = cv2.GaussianBlur(background, (5, 5), 0)
            difference = cv2.absdiff(img_blur, background_blur)
            _, thresh_result = cv2.threshold(difference, 64, 255, cv2.THRESH_BINARY)
            result = cv2.dilate(thresh_result, None, iterations=2)

            cv2.imshow('title', result)
        k = cv2.waitKey(30)
        if k == ord('q'):
            break
        elif k == ord('p'):
            print("Image captured!")
            background = img
    grabResult.Release()
    
# Releasing the resource    
camera.StopGrabbing()

cv2.destroyAllWindows()