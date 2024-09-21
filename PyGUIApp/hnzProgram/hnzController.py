from hnzView import View
from hnzModel import Model
from tkinter import *
from pubsub import pub

class Controller:
    def __init__(self, parent):
        self.parent = parent
        self.model = Model()
        self.view = View(parent)
        self.view.setup()

        pub.subscribe(self.openfile_btn_pressed, "OpenFile_Button_Pressed")
        pub.subscribe(self.line_detection, "LineDetect_Button_Pressed")
        pub.subscribe(self.model_change_handler, "model_updated")

    def openfile_btn_pressed(self):
        # print("controller - open file btn pressed")
        self.model.loadImg()

    def line_detection(self):
        print("controller - control line detection")
        self.model.lineDetection(
            self.view.scale1.get(),
            self.view.scale2.get(),
            self.view.scale3.get(),
            self.view.scale4.get()
        )

    # define model change method, pass current image
    # from model to view for updating in GUI
    def model_change_handler(self, data):
        print("controller - model change")
        self.view.updateImg(data)

# application entry point main method
    # create instance of tk
if __name__ == "__main__":
    mainwin = Tk()
    WIDTH = 800
    HEIGHT = 800
    mainwin.geometry("%sx%s" %(WIDTH, HEIGHT))
    mainwin.title("Image Line Detection")

    app = Controller(mainwin)
    mainwin.mainloop()



