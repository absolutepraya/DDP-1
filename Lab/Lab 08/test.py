from tkinter import *

class ProcessButton:
    def __init__(self):
        window = Tk()
        label = Label(master = window, text="Welcome")
        btOK = Button(master = window, text="OK", command=self.processOK, bg="red", fg="white")
        btCancel = Button(master = window, text="Cancel", command=self.processCancel, bg="blue", fg="white")
        
        label.pack()
        btOK.pack()
        btCancel.pack()

        window.mainloop()

    def processOK(self):
        print("OK button is clicked")
    def processCancel(self):
        print("Cancel button is clicked")


ob = ProcessButton()
