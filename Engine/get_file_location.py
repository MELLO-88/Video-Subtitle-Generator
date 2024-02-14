import tkinter as tk
from tkinter import filedialog

def get_file_location():
    # Initialize the Tkinter root
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Ask for the file location
    file_path = filedialog.askopenfilename()  # Opens dialog to select a file
    root.destroy()  # Close the Tkinter root
    return file_path