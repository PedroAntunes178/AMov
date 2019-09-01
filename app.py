import matplotlib
matplotlib.use("TkAgg")
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from matplotlib import style
import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
from amov import *

LARGE_FONT= ("Verdana", 12)
style.use('ggplot')
f = plt.figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)

def animate(i):
    tempo = list()
    var_acc = list()
    data = get_file()
    plot_graph(tempo, var_acc, data)
    a.clear()
    a.plot(tempo, var_acc)


class AMov(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self,default='src/app_icon.ico')
        tk.Tk.wm_title(self, "Movement Analysis")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (AcelerationPage,):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(AcelerationPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class AcelerationPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        doc_name = ttk.Entry(self)
        doc_name.pack(side=tk.LEFT)
        button1 = ttk.Button(self, text="Get data",
                            command=lambda: self.draw_graphic(doc_name.get()))
        button1.pack(side=tk.LEFT)
        canvas = FigureCanvasTkAgg(f, self)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def draw_graphic(self, str):
        tempo = list()
        var_acc = list()
        data = get_file(str)
        plot_graph(tempo, var_acc, data)
        a.clear()
        a.plot(tempo, var_acc, "#00A3E0", label="Variação da aceleração ao longo do tempo.")
        a.set_title('Variação da aceleração ao longo do tempo.')
#
#    def on_key_press(self, event):
#        print("you pressed {}".format(event.key))
#        key_press_handler(event, canvas, toolbar)

#    canvas.mpl_connect("key_press_event", on_key_press)


app = AMov()
app.mainloop()
