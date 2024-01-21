import tkinter as tk

def convert():
    fahrenheit = float(entry.get())
    celsius = (fahrenheit - 32) * 5/9
    result_label.config(text=f"{celsius:.2f}")

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("250x50")

entry = tk.Entry(root, width=10)
entry.grid(row=0, column=0, padx=(10, 0), pady=10)

fahrenheit_label = tk.Label(root, text="°F")
fahrenheit_label.grid(row=0, column=1)

convert_button = tk.Button(root, text="➜", command=convert)
convert_button.grid(row=0, column=2, padx=10)

result_label = tk.Label(root, text="______")
result_label.grid(row=0, column=3)

celcius_label = tk.Label(root, text="°C")
celcius_label.grid(row=0, column=4)

root.mainloop()