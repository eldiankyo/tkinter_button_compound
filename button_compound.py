import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry('800x600')
root.resizable(False, False)
root.title('Tkinter button compound demo')

def download_clicked():
    showinfo(title='Information', message='Download button clicked!')

download_icon = tk.PhotoImage(file='./download.png')
download_button = ttk.Button(root, image=download_icon, text='Download', compound=tk.LEFT, command=download_clicked).pack()


root.mainloop()