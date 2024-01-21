from tkinter import *
from tkinter import colorchooser

def choose_color():
    color = colorchooser.askcolor()
    if color:
        color_hex = color[1]
        label.config(text="Change the foreground color", fg=color_hex, font=("Helvetica", 20))

root = Tk()
root.title("Color Picker")
root.geometry("400x150")

label = Label(root, text="Change the foreground color", font=("Helvetica", 20))
label.pack(pady=20)

button = Button(root, text="Pick a Color", command=choose_color)
button.pack()

root.mainloop()
