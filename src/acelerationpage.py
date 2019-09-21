class AcelerationPage(tk.Frame):

    def __init__(self, parent, controller):
        tempo = list()
        var_acc = list()
        tk.Frame.__init__(self, parent)
        currentValue = tk.StringVar(self, "0")
        interfaseframe = tk.Frame(self)
        interfaseframe.pack(side=tk.TOP, fill='both')
        label1 = ttk.Label(interfaseframe, text="File Name: ")
        label1.grid(row=0, column=0)
        doc_name = ttk.Entry(interfaseframe)
        doc_name.grid(row=0, column=1)
        button1 = ttk.Button(interfaseframe, text="Get data",
                            command=lambda: self.draw_graphic(doc_name.get(), tempo, var_acc))
        button1.grid(row=0, column=2)
        label2 = ttk.Label(interfaseframe, text="Sec to start the sum: ")
        label2.grid(row=1, column=0)
        sec = ttk.Entry(interfaseframe)
        sec.grid(row=1, column=1)
        button2 = ttk.Button(interfaseframe, text="SumUP 10sec of movement",
                            command=lambda: self.get_info(sec.get(), var_acc, currentValue))
        button2.grid(row=2, column=0)
        label3 = ttk.Label(interfaseframe, textvariable=currentValue)
        label3.grid(row=2, column=1)
        button3 = ttk.Button(self, text="Clear All",
                            command=lambda: self.clean_values(tempo, var_acc))
        button3.pack(side=tk.BOTTOM)
        canvas = FigureCanvasTkAgg(f, self)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def draw_graphic(self, str, tempo, var_acc):
        data = self.get_file(str)
        self.plot_graph(tempo, var_acc, data)
        a.clear()
        a.plot(tempo, var_acc, "#00A3E0", label="Variação da aceleração ao longo do tempo.")
        a.set_title('Variação da aceleração ao longo do tempo.')
        a.set_xlabel('sec')
        a.set_ylabel('variação aceleração')
        a.set_xlim(0, 60)
        a.set_ylim(0, 6)

    def clean_values(self, tempo, var_acc):
        a.clear()
        for k in range(len(var_acc)):
            var_acc.pop()
            tempo.pop()

    def plot_graph(self, tempo, var_acc, data):
    	for k in range(len(data[0])-1):
            soma = 0
            for index in (2,3,4):
                soma = soma + abs(data[index][k]-data[index][k+1])
            var_acc.append(soma)
    	for k in range(1,len(data[0])):
            tempo.append(data[0][k]/200)

    def get_info(self, point, var_acc, currentValue):
    	#point = input("Em que sec queres começar a contar: ")
        val = 0
        #print(int(point)*200, '+', int(point)*200+1200)
        for k in range(int(point)*200,int(point)*200+2000):#sums up 10 sec of the movement
            val = val + var_acc[k]
        val = float("{0:.2f}".format(val))
        currentValue.set(str(val))
        print(val)

    def get_file(self, str):
    	#doc = input("Escreva o nome do documento: ")
    	direc = '../files/' + str + '.txt'
    	print(direc)
    	data=pd.read_csv(direc, sep="\t", header=None, engine='python', skiprows=3)
    	return data

#
#    def on_key_press(self, event):
#        print("you pressed {}".format(event.key))
#        key_press_handler(event, canvas, toolbar)

#    canvas.mpl_connect("key_press_event", on_key_press)
