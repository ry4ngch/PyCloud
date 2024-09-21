import tkinter as tk
from tkinter import *
from pubsub import pub #important for parsing information between MVC

class View:
    def __init__(self, parent):
        # Initialized variable
        self.container = parent
        return

    def setup(self):
        # call methods to setup the user interface
        self.create_widget()
        self.setup_layout()

    def create_widget(self):
        # Create various widgets in the tkinter main window
        # Setup frames
        self.topFrame = Frame(
            self.container,
            borderwidth=2,
            highlightbackground="white",
            highlightcolor="red",
            highlightthickness=1,
            width=300,
            height=600
        )

        self.bottomFrame = Frame(
            self.container,
            borderwidth=2,
            highlightbackground="white",
            highlightcolor="red",
            highlightthickness=1,
            width=300,
            height=600
        )

        self.topFrame2 = Frame(self.topFrame)

        # Create Buttons
        self.b1LoadImg = tk.Button(
            self.topFrame2,
            text="Load Image",
            command=self.loadImg
        )

        self.b2LineDetect = tk.Button(
            self.topFrame2,
            text="Line Detection",
            command=self.lineDetect
        )

        # Create Scale Bar
        self.scale1 = tk.Scale(
            self.topFrame,
            from_=1,
            to=20,
            orient=HORIZONTAL,
            length=500,
            label="pixel",
            command=self.scalarChange
        )
        self.scale1.set(1)

        self.scale2 = tk.Scale(
            self.topFrame,
            from_=1,
            to=130,
            orient=HORIZONTAL,
            length=500,
            label="threshold",
            command=self.scalarChange
        )
        self.scale2.set(50)

        self.scale3 = tk.Scale(
            self.topFrame,
            from_=1,
            to=500,
            orient=HORIZONTAL,
            length=500,
            label="mini line length",
            command=self.scalarChange
        )
        self.scale3.set(10)

        self.scale4 = tk.Scale(
            self.topFrame,
            from_=1,
            to=100,
            orient=HORIZONTAL,
            length=500,
            label="max line gap",
            command=self.scalarChange
        )
        self.scale4.set(50)


        # image panel
        self.panelA = tk.Label(self.bottomFrame, text="image here")


    def loadImg(self):
        print("View - Load Image")
        pub.sendMessage("OpenFile_Button_Pressed")

    def lineDetect(self):
        print("View - Line Detect")
        pub.sendMessage("LineDetect_Button_Pressed")

    # put image into panel A
    def updateImg(self, img):
        print("Update Image")
        self.panelA.configure(image=img)
        self.panelA.image = img

    def scalarChange(self, val):
        print("View - Scalar Change")
        pub.sendMessage("ScalarChange_Button_Pressed")

    def setup_layout(self):
        self.topFrame.pack(side=TOP)
        self.bottomFrame.pack(side=BOTTOM)

        # Pack top2 inside top frame
        self.topFrame2.pack(side=TOP)

        # Pack 2 button to topframe2
        self.b1LoadImg.pack(side=LEFT)
        self.b2LineDetect.pack(side=RIGHT)

        # Pack 4 scale bar
        self.scale4.pack(side=BOTTOM) # Max Line Gap
        self.scale3.pack(side=BOTTOM) # Min Line Length
        self.scale2.pack(side=BOTTOM) # Threshold
        self.scale1.pack(side=BOTTOM) # Pixel

        # Pack PanelA in Bottom Frame
        self.panelA.pack()


# testing
if __name__ == "__main__":
    mainwin = Tk()
    WIDTH = 800
    HEIGHT = 800
    mainwin.geometry("%sx%s" %(WIDTH, HEIGHT))
    mainwin.title("Open CV")

    view = View(mainwin) # Top View as Application Window
    view.setup()
    mainwin.mainloop()