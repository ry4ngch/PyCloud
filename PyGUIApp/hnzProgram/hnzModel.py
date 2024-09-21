from tkinter.filedialog import askopenfilename
import cv2 # to manipulate image
from pubsub import pub
import PIL.ImageTk, PIL.Image # image transfer between openCV and tkinter
import numpy as np # to manipulate image


class Model:
    def __init__(self):
        # variable to check if image has been loaded
        # this variable is to avoid error before image is loaded
        self.flagLoadImage = False
        return

    def loadImg(self):
        path = askopenfilename(
            initialdir="./",
            filetypes=[("Image File", "*.jpg *.jpeg"), ("All Files", "*.*")],
            title="Choose a file"
        )

        if len(path) > 0:
            self.originalImg = cv2.imread(path)
            self.currentImg = self.originalImg.copy() #duplicate as current image
            pub.sendMessage("model_updated", data=self.toTkImg(self.currentImg))

        self.flagLoadImage = True
    # convert cv2 to tk image
    def toTkImg(self, img):
        # cv2 image is in bar format
        b, g, r = cv2.split(img)
        img = cv2.merge((r, g, b))

        # convert rgb array into 2 dimensional PIL image array
        im = PIL.Image.fromarray(img)

        # convert PIL array into tkinter image
        imgtk = PIL.ImageTk.PhotoImage(image=im)
        return imgtk

    def lineDetection(self, p, th, minlen, maxgap):
        if self.flagLoadImage:
            img = self.originalImg.copy()

            # Pre-processing image before line-detection
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert img to grayscale
            edges = cv2.Canny(gray, 50, 150, apertureSize=3) # detect edges use canny function

            # detect lines and put into a collection 'lines'
            lines = cv2.HoughLinesP(edges, p, np.pi/360, th, minlen, maxgap)

            # draw lines on to image
            for line in lines:
                x1, y1, x2, y2 = line[0] # get start and endpoint location
                cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2) # draw lines

            self.currentImg = img # put the work into current image
            pub.sendMessage("model_updated", data=self.toTkImg(self.currentImg)) # update the view