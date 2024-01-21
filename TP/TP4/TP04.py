import tkinter as tk
from tkinter import messagebox

# Create the canvas for the barcode
class BarcodeCanvas(tk.Canvas):
    # Create the canvas configuration
    def __init__(self, master=None):
        super().__init__(master)
        self.config(width=300, height=350, bg="white")

    def checksum(self, barcode):
        """Calculate the checksum of the barcode.
        The odd digits are summed together are weighted 1, while the even digits are weighted 3.
        The total is then divided by 10.

        If the remainder is 0, the checksum is 0. Otherwise, the checksum is 10 - remainder."""

        odd_sum = sum(int(barcode[i]) for i in range(0, 12, 2))
        even_sum = sum(int(barcode[i]) for i in range(1, 12, 2))
        total = odd_sum + even_sum * 3
        remainder = total % 10
        if remainder == 0:
            return 0
        else:
            return 10 - remainder
    
    # EAN-13 Barcode Logic
    def ean13(self, barcode, filename):
        """Encode the barcode number into EAN-13 barcode format.
        The number is devided into 3 parts:
        - The first digit
        - The first 6 digits
        - The last 6 digits (the last 5 digits + the checksum)

        The encoding of the first 6 digits is based on the 1st digit, it is either L or G.
        The encoding of the last 6 digits is not based on anything, it is always R.
        
        Every encoding consists of 7 bit binary code, plus the start (3 bit), middle (5 bit), 
        and end separator (5 bit). The total length of the barcode is 95 bit."""

        # Split the barcode into 3 parts
        start = barcode[:1]
        middle = barcode[1:7]
        end = barcode[7:]

        # Define the separators
        separator_se = "101" # SE = Start and End
        separator_m = "01010" # M = Middle

        # L or G code determination for the first 6 digits
        start_patterns = ["LLLLLL", "LLGLGG", "LLGGLG", "LLGGGL", "LGLLGG", "LGGLLG", "LGGGLL", "LGLGLG", "LGLGGL", "LGGLGL"]

        # Define encoding patterns for L, G, R
        encoding_patterns = {'L': 
                            ['0001101', '0011001', '0010011', '0111101', '0100011',
                            '0110001', '0101111', '0111011', '0110111', '0001011'],
                            'G': 
                            ['0100111', '0110011', '0011011', '0100001', '0011101',
                            '0111001', '0000101', '0010001', '0001001', '0010111'],
                            'R': 
                            ['1110010', '1100110', '1101100', '1000010', '1011100',
                            '1001110', '1010000', '1000100', '1001000', '1110100']}
        
        # Get the checksum
        global chksum
        chksum = self.checksum(barcode)
        
        # Start creating the barcode string
        barcode_lst = []

        # Add the start separator
        barcode_lst.append(separator_se)

        # Determine the pattern for the first 6 digits
        start_pattern = start_patterns[int(start)]

        # Encode the first group of 6 digits
        for i in range(6):
            # If the pattern is L, encode the digit using L encoding patterns
            if start_pattern[i] == 'L':
                barcode_lst.append(encoding_patterns['L'][int(middle[i])])
            # If the pattern is G, encode the digit using G encoding patterns
            else:
                barcode_lst.append(encoding_patterns['G'][int(middle[i])])
        
        # Add the middle separator
        barcode_lst.append(separator_m)

        # Encode the last group of 6 digits
        for i in range(5):
            # Encode the digit using R encoding patterns
            barcode_lst.append(encoding_patterns['R'][int(end[i])])
        # Encode the last digit
        barcode_lst.append(encoding_patterns['R'][chksum])

        # Add the end separator
        barcode_lst.append(separator_se)

        # Draw the barcode
        self.draw_barcode(barcode_lst, barcode)

        # Save the barcode to PS file
        self.postscript(file=filename, colormode='color')
    
    def draw_barcode(self, barcode_lst, barcode_str):
        """Draw the barcode on the canvas.
        The barcode is drawn from left to right, starting from the center of the canvas.
        The barcode is drawn using rectangles, with the width of 2 pixels and the height of 150 pixels.
        The color of the rectangle is black if the bit is 1, and white if the bit is 0."""

        # Clear the canvas
        self.delete("all")

        # Calculate the starting position to center the barcode horizontally
        total_width = sum(len(code) for code in barcode_lst) # Calculate the total width of the barcode
        x = (self.winfo_reqwidth() - total_width * 2) // 2
        y = 80

        # Define the barcode's width and height
        bar_width = 2
        bar_height = 150

        # Print the barcode's label
        label_text = "EAN-13 Barcode:"
        label_x = self.winfo_reqwidth() // 2  # Adjust the factor based on the font size
        label_y = 35
        self.create_text(label_x, label_y, text=label_text, font=("Helvetica", 16, 'bold'), anchor="n")

        # Print the first part of barcode's number
        number_text = barcode_str[0]
        number_x = self.winfo_reqwidth() // 2 - 110  # Adjust the factor based on the font size
        number_y = 235
        self.create_text(number_x, number_y, text=number_text, font=("Helvetica", 16, 'bold'), anchor="n")

        # Print the second part of barcode's number
        number_text = barcode_str[1:7]
        number_x = self.winfo_reqwidth() // 2 - 45  # Adjust the factor based on the font size
        number_y = 235
        self.create_text(number_x, number_y, text=number_text, font=("Helvetica", 16, 'bold'), anchor="n")

        # Print the third part of barcode's number
        number_text = (barcode_str + str(chksum))[7:]
        number_x = self.winfo_reqwidth() // 2 + 45 # Adjust the factor based on the font size
        number_y = 235
        self.create_text(number_x, number_y, text=number_text, font=("Helvetica", 16, 'bold'), anchor="n")

        # Print the checksum at the bottom of the canvas
        chksum_text = "Check Digit: " + str(chksum)
        chksum_x = self.winfo_reqwidth() // 2
        chksum_y = 280
        self.create_text(chksum_x, chksum_y, text=chksum_text, font=("Helvetica", 16, 'bold'), fill='orange', anchor="n")

        # ['101', '101101', '1101101']
        
        # Draw the barcode
        for code in barcode_lst:
            for bit in code:
                # Create a taller bar for the start, mid, and end seperator, with the height of 170 pixels color blue
                if code == "101" or code == "01010":
                    if bit == '1':
                        self.create_rectangle(x, y, x + bar_width, y + bar_height + 20, fill="blue", outline="")
                    else:
                        self.create_rectangle(x, y, x + bar_width, y + bar_height + 20, fill="white", outline="")
                # Create a normal bar for the rest of the barcode, with the height of 150 pixels color black
                else:
                    if bit == '1':
                        self.create_rectangle(x, y, x + bar_width, y + bar_height, fill="black", outline="")
                    else:
                        self.create_rectangle(x, y, x + bar_width, y + bar_height, fill="white", outline="")
                x += bar_width # Move to the next position

# Create the main frame
class BarcodeApp:
    def __init__(self, master=None):
        self.master = master

        # Set the window title and size, and make the window size unchangeable
        self.master.title("EAN-13 [by Daffa Abhipraya]")
        self.master.geometry("420x500")
        self.master.resizable(False, False)

        # Create the label for the PS filename input
        self.label_ps = tk.Label(self.master, text="Save barcode to PS file [eg: EAN13.eps]:", font=("Helvetica", 16, "bold"))
        self.label_ps.pack(pady=(10, 0))

        # Create the entry for the PS filename input
        self.entry_ps = tk.Entry(self.master, font=("Helvetica", 16))
        self.entry_ps.pack()
        # Bind the entry to the barcode function
        self.entry_ps.bind("<Return>", self.barcode)

        # Create the label for the barcode input
        self.label_barcode = tk.Label(self.master, text="Enter code (first 12 decimal digits):", font=("Helvetica", 16, "bold"))
        self.label_barcode.pack()

        # Create the entry for the barcode input
        self.entry_barcode = tk.Entry(self.master, font=("Helvetica", 16))
        self.entry_barcode.pack()
        # Bind the entry to the barcode function
        self.entry_barcode.bind("<Return>", self.barcode)

        self.barcode_button = tk.Button(self.master, text="Create!", command=self.barcode)
        self.barcode_button.pack()

        # Create the custom canvas for the barcode
        self.canvas = BarcodeCanvas(self.master)
        self.canvas.pack(pady=10)

    def barcode(self, _event=None): # _event is a dummy parameter
        """Get the input and validate it."""
        # Get all the input
        filename = self.entry_ps.get()
        barcode = self.entry_barcode.get()

        # Conditions that make the PS filename input invalid
        # Blank input
        blank_error = filename == ""
        # Contains restricted symbols
        symbol_error = "\\" in filename or "/" in filename or ":" in filename or "*" in filename or "?" in filename or "\"" in filename or "<" in filename or ">" in filename or "|" in filename
        # Not in .eps format
        format_error = not filename[-4:] == ".eps"
        # Empty filename
        emptyname_error = filename[:-4] == ""

        # Validate PS filename input
        if symbol_error or format_error or blank_error or emptyname_error:
            tk.messagebox.showerror("PS Filename Input Error!",
                                    "Please enter correct PS filename.\n\n" +
                                    "Note:\n" +
                                    "- PS filename can't contain any of the following symbols:\n" +
                                    "\\ / : * ? \" < > |\n" +
                                    "- PS filename must be in .eps format.\n" +
                                    "- PS filename can't be empty.")
            # Let the user enter the PS filename again
            self.entry_ps.delete(0, tk.END)
            return

        # Conditions that make the barcode input invalid
        # Blank input
        blank_error = len(barcode) == 0
        # Not 12 digits
        length_error = len(barcode) != 12
        # Contains characters other than decimal digits (0 - 9)
        symbol_error = not barcode.isdecimal()

        # Validate barcode input
        if blank_error or length_error or symbol_error:
            tk.messagebox.showerror("Barcode Input Error!",
                                    "Please enter correct barcode input.\n\n" +
                                    "Note:\n" +
                                    "- Barcode input must be 12 decimal digits.\n" +
                                    "- Barcode can't be empty.")
            # Let the user enter the barcode again
            self.entry_barcode.delete(0, tk.END)
            return
        
        # Draw the barcode
        self.canvas.ean13(barcode, filename)

# Main program function
def main():
    root = tk.Tk()
    app = BarcodeApp(master=root)
    root.mainloop()

# Main program
if __name__ == "__main__":
    main()