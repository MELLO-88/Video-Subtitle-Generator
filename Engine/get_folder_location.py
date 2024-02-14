import tkinter as tk
from tkinter import filedialog

def get_folder_location():

    root = tk.Tk()  # Create a temporary root window
    root.withdraw()  # Hide the root window

    folder_path = filedialog.askdirectory(
        title="Select Folder"
    )  # Open a dialog box to select a folder

    if folder_path:  # Check if a folder was selected
        print("Selected folder:", folder_path)
        return folder_path
    else:
        print("No folder selected.")
        return None