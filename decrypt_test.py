import os
import shutil # for moving files
import pyAesCrypt # for decryption
from pathlib import Path
import tkinter as tk
from tkinter import messagebox
import tkinter.simpledialog

folders_path = [
    str(os.path.join(Path.home(), "Downloads")),
    str(os.path.join(Path.home(), "Documents"))
]
# Get the key
root = tk.Tk()
root.withdraw()
key = tkinter.simpledialog.askstring("Decryption Key", "Enter the decryption key:", parent=root)

# Decrypt every file in each folder
for folder_path in folders_path:
    for file in os.listdir(folder_path):
        bufferSize = 64*1024
        # Get the path for the current file
        file_path = os.path.join(folder_path, file)
        if file.endswith(".aes"):
            # Decrypt the file
            pyAesCrypt.decryptFile(file_path, file_path[:-4], key, bufferSize)
            # Move the decrypted file
            destination_path = os.path.join(folder_path,"decrypted_"+file[:-4])
            shutil.move(file_path[:-4], destination_path)
            # Delete the encrypted file
            os.remove(file_path)

# Use tkinter to display a message that the decryption is complete
messagebox.showinfo("Decryption Complete", "All files in the folders have been decrypted.")
root.mainloop()