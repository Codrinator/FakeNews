from tkinter import *
from tkinter.ttk import *
import tkinter as tk

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'Analyze', width = 25, command = self.close_windows)
        self.button1.pack()
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()

def main(): 
    root = tk.Tk()
    root.title("FakeNews")
    root.geometry("800x600")
    windowIcon = PhotoImage(file = 'Graphics\\fake-news.png')
    backgroundTexture = PhotoImage(file = 'Graphics\\paper_texture_05.png')
    root.iconphoto(False, windowIcon)
    root.configure(bg = 'yellow')   
    app = MainWindow(root)
    canvas1 = Canvas(root, width = 800, height = 600)
    canvas1.pack(fill = 'both', expand = True)
    canvas1.create_image(0, 0, image = backgroundTexture, anchor = 'nw')
    root.mainloop()

main()