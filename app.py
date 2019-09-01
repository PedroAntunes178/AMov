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
from amov import *

LARGE_FONT= ("Verdana", 12)
style.use('ggplot')
f = plt.figure(2)
a = f.add_subplot(111)

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()


class AMov(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self,default='src/app_icon.ico')
        tk.Tk.wm_title(self, "Movement Analysis")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save settings", command = lambda: popupmsg("Not supported just yet!"))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)
        tk.Tk.config(self, menu=menubar)
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
        tempo = list()
        var_acc = list()
        val = 0
        tk.Frame.__init__(self, parent)
        labe1 = tk.Label(self, text="File Name: ")
        labe1.grid(row=0, column=0)
        doc_name = ttk.Entry(self)
        doc_name.grid(row=0, column=1)
        button1 = ttk.Button(self, text="Get data",
                            command=lambda: self.draw_graphic(doc_name.get(), tempo, var_acc))
        button1.grid(row=0, column=2)
        sec = ttk.Entry(self)
        sec.grid(row=1, column=0)
        button2 = ttk.Button(self, text="SumUP 1min of movement",
                            command=lambda: get_info(sec.get(), var_acc, val))
        button2.grid(row=1, column=1)
        labe2 = tk.Label(self, text=val)
        labe2.grid(row=1, column=2)
        button3 = ttk.Button(self, text="Clear All",
                            command=lambda: clean_values(tempo, var_acc))
        button3.pack(side=tk.BOTTOM)
        canvas = FigureCanvasTkAgg(f, self)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def draw_graphic(self, str, tempo, var_acc):
        data = get_file(str)
        plot_graph(tempo, var_acc, data)
        a.clear()
        a.plot(tempo, var_acc, "#00A3E0", label="Variação da aceleração ao longo do tempo.")
        a.set_title('Variação da aceleração ao longo do tempo.')
        a.set_xlabel('sec')
        a.set_ylabel('variação aceleração')
        a.set_xlim(0, 60)
        a.set_ylim(0, 6)
#
#    def on_key_press(self, event):
#        print("you pressed {}".format(event.key))
#        key_press_handler(event, canvas, toolbar)

#    canvas.mpl_connect("key_press_event", on_key_press)


app = AMov()
app.geometry("1280x720")
app.mainloop()
