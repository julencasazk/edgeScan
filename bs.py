# (Autofocus (https://docs.opencv.org/3.4/dd/d53/tutorial_py_depthmap.html))
# (Calibrate camera)
# (Convert to grayscale)
# (Filter noise)
# Background subtraction (OR EDGE DETECTION OR THRESHOLDING)
# (Filter noise)
# For each connected component or find contours
# Rotated bounding box

# If side cameras are perpendicular to top camera there is no need for features (https://docs.opencv.org/4.x/db/d27/tutorial_py_table_of_contents_feature2d.html)
# We can use pose (https://docs.opencv.org/4.x/d7/d53/tutorial_py_pose.html)
# Else homography (https://docs.opencv.org/4.x/d9/dab/tutorial_homography.html)

# threshold (not good): Otsu or Triangle (maybe) vs adaptive
# (OR GLOBAL THRESHOLD) by taking the highest background value in histogram
# Canny (very bad)

import sys

import cv2 as cv
import numpy as np

def main():
    cap = cv.VideoCapture(0)

    if not cap.isOpened():
        return 1

    bgfg = cv.createBackgroundSubtractorMOG2()
    learningRate = -1

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        match cv.waitKey(delay=1):
            case 27:
                break

            case 13 | 32:
                learningRate = -1 if learningRate == 0 else 0

        # fgmask = bgfg.apply(frame, learningRate=learningRate)
        fgmask = cv.Canny(frame, 100, 200)
        print(np.unique(fgmask))
        cv.imshow("", fgmask)


if __name__ == "__main__":
    sys.exit(main())
