#!/python3
from tkinter import *
from amov import *
#from mpl_toolkits.mplot3d import axes3d
#import time
def pass_doc(data):
    doc = doc_name.get()
    data = get_file(doc)

root = Tk()
# Code to add widgets will go here...
L1 = Label(root, text="Doc Name: ")
L1.pack(side = LEFT)
doc_name = Entry(root, bd =5)
doc_name.pack(side = LEFT)
B1 = Button(root, text='Get File', command=lambda: pass_doc(data))
B1.pack(side = LEFT)

root.mainloop()
