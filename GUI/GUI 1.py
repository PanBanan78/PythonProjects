__author__ = 'Oskar'

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()


    def create_widgets(self):
       # self.hi_there = tk.Button(self, text="Hello World", command=self.say_hi())
        self.seven = tk.Button(self, text="7", command=self.seven)
        self.seven.pack(side="left")
        self.eight = tk.Button(self, text="8", command=self.eight)
        self.eight.pack(side="right")

        self.quit = tk.Button(self, text="QUIT", fg="pink",command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

    def seven(self):
        print("7")

    def eight(self):
        print("8")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
