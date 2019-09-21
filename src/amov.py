class AMov(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        #tk.Tk.iconbitmap(self,'icon.ico')
        tk.Tk.wm_title(self, "Movement Analysis")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save settings", command = lambda: popupmsg("Not supported just yet!"))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=lambda: quit())
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
