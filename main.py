# Text Encoding Program

"""
This program is to take a string of text and then make it all different so it can't be read
Then there will a decoding section to ensure that it can be reversed and read as per normal again

This program was made out of me seeing if I could implement it successfully
"""


import tkinter as tk
from frameMain import *
from functions import *


class Window:
    def __init__(self, root, title, geometry):
        # This will set all the base info for the main window
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)

        FrameMain(root)  # To make the main frame

        self.root.mainloop()  # To actually run the program loop


def main():
    window = Window(tk.Tk(), 'Text Cryptographer', '800x250')  # Main window defined here


main()


# Future Improvements
# Change the text inputs from lines into boxes for more text options
