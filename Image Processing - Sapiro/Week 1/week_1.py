#!/usr/bin/env python2.7

"""
    Author: Jason Johns
    Date:   1/29/2014
    Desc:   Week 1 Assignment for Coursera class.

            For the project, its been suggested to use Octave or Matlab, but making heads or
            tails out of those programs has been tricky.

            Given the functionality of Python packages NumPy, SciPy and OpenCV bindings,
            I decided to do the course assignments in Python where possible

"""

import os, sys 
import numpy as np, cv2 as cv
from scipy import ndimage

class Week1:

    def __init__(self):
        self.filename = None

    def parseArgs(self, args):
        
        if len(args) == 1:
            print "Invalid Arguments or flags.\n\n\
Proper flags are:\n\
    -r [rotation angle number] Change the image rotation\n\
    -i [num] change intensity level.  Valid num values are [2, 4, 8, 16, 32, 64, 128, 256]\n\
    -s [neighborhood] Calculate the spatial average of the nxn neighborhood and replace\n"

            sys.exit(2)

        else:
            self.filename = args[1]
            self.fileSplit = args[1].split(".")

            if args[2] == "-r":
                self.rotateImage(float(args[3]))

            elif args[2] == "-i":
                intensity = int(args[3])
                if intensity != 0 and ((intensity & (intensity- 1)) == 0):
                    self.adjustIntensity(intensity)

                else:
                    print "Acceptable intensity values are [2, 4, 8, 16, 32, 64, 128, 256]."

            elif args[2] == "-s":
                self.replaceSpatialAverage(int(args[3]))


    """
        Rotates the image about the center point by the angle specified.  Saves the resulting
        file with _rotate_ANGLE inserted in filename
    """
    def rotateImage(self, angle):
        print "Rotating image to angle: %s" % (angle)

        image = cv.imread(self.filename, -1)
        rotate = ndimage.rotate(image, angle)

        newFile = "%s_rotate_%s.%s" % (self.fileSplit[0], int(angle), self.fileSplit[1])

        print "Saving to %s" % (newFile)
        cv.imwrite(newFile, rotate)


    def adjustIntensity(self, intensity):


        #open image as ndarray and convert to YCrCb
        image = cv.imread(self.filename, -1)

        #use masking to use vectorization to implement threshold
        idx = image[ :, :, 0] > intensity
        image[idx] = intensity

        #create new file string and save adjusted image
        newFile = "%s_intensity_%s.%s" % (self.fileSplit[0], intensity, self.fileSplit[1])
        cv.imwrite(newFile, image)

    def replaceSpatialAverage(self, neighborhood):
        print  "Replacing %dx%d blocks with average" % (neighborhood, neighborhood)

        image = cv.imread(self.filename, -1)

        img = cv.medianBlur(image, int(neighborhood))

        newFile = "%s_medianblur_%sx%s.%s" % (self.fileSplit[0], neighborhood, neighborhood, self.fileSplit[1])
        cv.imwrite(newFile, img)



init = Week1()
init.parseArgs(sys.argv)