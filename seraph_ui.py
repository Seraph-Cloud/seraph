# Seraph UI
# Author: @diveyez
# we are using tkinter because it is built
# into python and maskes a very quick way to
# dockerize this as a web application
from tkinter import *
# Constructing the UI
root = Tk()
UIVersion = Label (root, text="Seraph 0.1.0")
UIVersion.pack()
root.mainloop()
quit()