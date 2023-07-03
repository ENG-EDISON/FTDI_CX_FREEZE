from tkinter import Tk,Button

count=0;
def increment_fun():
    global count,B1
    count+=10
    B1.configure(text="Text counter = "+str(count))
    print("Updating..........")
root=Tk()
B1=Button(root)
B1.configure(background="yellow", text="Click Count = 0", command=increment_fun)
B1.pack()
root.mainloop()