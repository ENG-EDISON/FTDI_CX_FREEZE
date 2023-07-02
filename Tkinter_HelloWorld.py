#Python Script to create a label with hello World

from tkinter import *                  #imports the Tkinter library into the global namespace
from tkinter.ttk import *              #This imports the ttk or themed Tk widget library
root=Tk()                              #Creates root or master application object
label=Label(root,text="Hello Wolrd!")  #This creates a new Label object.
label.pack()                           #places the new label widget onto its parent widget
root.mainloop()                        #This final line starts our main event loop