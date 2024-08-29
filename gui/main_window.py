from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

class MainWindow(Tk):
    def __init__(self, summarize_callback, read_docx_callback):
        super().__init__()
        self.show = True
        self.result = True
        self.chosenFile = 'No chosen file'
        self.filename = ''
        self.fileContent = ''
        self.xstAlgoContent = 'Placeholder for existing algorithm results.'
        self.newAlgoContent = 'Placeholder for new algorithm results.'
        self.summarize_callback = summarize_callback
        self.read_docx_callback = read_docx_callback
        self.create_widgets()

    def create_widgets(self):
        self.setup_window()
        self.create_header()
        self.create_columns()
        self.create_results_window()

    def setup_window(self):
        self.screenWidth = self.winfo_screenwidth()
        self.screenHeight = self.winfo_screenheight()
        self.geometry('%dx%d' % (self.screenWidth * 0.95, self.screenHeight * 0.9))
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=2)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        Frame(self, background='antiquewhite').grid(row=0, column=0, columnspan=3, sticky='nsew')

    def create_header(self):
        try:
            self.tenioPic = self.load_image('./player-spaceship.png', 15, 14)
            self.bajePic = self.load_image('./player-spaceship.png', 15, 14)
            self.caladiaoPic = self.load_image('./player-spaceship.png', 15, 14)
        except Exception as e:
            print("Error loading image:", e)
            self.tenioPic = self.bajePic = self.caladiaoPic = None

        header_frame = Frame(self, background='antiquewhite')
        header_frame.grid(row=0, column=0, columnspan=3, sticky='ew')

        Label(header_frame, text="Designing An Adaptive Dynamic Approach Applied in Text Summarization",
              font=('Slussen Mono Black', 15), background='antiquewhite', wraplength=self.screenWidth * 0.45).pack(pady=10)

        self.summarizer = Button(header_frame, text='Summarize', borderwidth=2, state='disabled', background='antiquewhite',
                width=12, height=2, activebackground='antiquewhite4', activeforeground="white",
                disabledforeground='bisque2', font=('Calibri Bold', 9), cursor='X_cursor', command=self.summarize_text)
        self.summarizer.pack(side=RIGHT, padx=5)

        Button(header_frame, text='Results', borderwidth=2, state='disabled', background='antiquewhite',
                width=12, height=2, activebackground='antiquewhite4', activeforeground="white",
                disabledforeground='bisque2', font=('Calibri Bold', 9), cursor='X_cursor').pack(side=RIGHT, padx=5)

        Button(header_frame, text='About', borderwidth=2, state='normal', background='antiquewhite',
                width=12, height=2, activebackground='antiquewhite4', activeforeground="white",
                font=('Calibri Bold', 9), cursor='hand2', command=self.toggle_about).pack(side=RIGHT, padx=5)

        self.aboutWindow = Frame(self, background='whitesmoke', bd=5, relief='ridge', pady=15, padx=15)
        Label(self.aboutWindow, background='whitesmoke', text="Designing An Adaptive Dynamic Approach Applied in Text Summarization",
              font=('Times New Roman Bold', 13), wraplength=self.screenWidth * 0.35).pack()
        Label(self.aboutWindow, background='whitesmoke', text="This is the abstract of the study...", font=('Times New Roman Normal', 11),
              wraplength=self.screenWidth * 0.35, justify='left', pady=30).pack()
        self.setup_researchers()

    def setup_researchers(self):
        group_Members = Frame(self.aboutWindow, background='whitesmoke', height=125, width=self.screenWidth * 0.35)
        Label(group_Members, text="Tenio", background='whitesmoke', font=('Times New Roman Bold', 8)).place(relx=0.95, anchor=NE)
        Label(group_Members, image=self.tenioPic).place(relx=1.05, rely=0.99, anchor=SE)

        Label(group_Members, text="Baje", background='whitesmoke', font=('Times New Roman Bold', 8)).place(relx=0.7, anchor=N)
        Label(group_Members, image=self.bajePic).place(relx=0.7, rely=0.99, anchor=S)

        Label(group_Members, text="Caladiao", background='whitesmoke', font=('Times New Roman Bold', 8)).place(relx=0.43, anchor=NW)
        Label(group_Members, image=self.caladiaoPic).place(relx=0.35, rely=0.99, anchor=SW)

        group_Members.pack()

    def create_columns(self):
        self.create_column1()
        self.create_column2()
        self.create_column3()

    def create_column1(self):
        column1 = Frame(self, padx=15, pady=2, borderwidth=2, relief='groove', background='whitesmoke')
        column1.grid(row=1, column=0, sticky='nsew')

        runningFile = Canvas(column1, borderwidth=2, relief='sunken')
        runningFileFrame = Frame(runningFile)
        self.runningFileLabel = Label(runningFileFrame, text=self.fileContent, wraplength=self.screenWidth * 0.2, justify='left')
        self.runningFileLabel.pack()
        runningFileFrame.place(anchor=NW, relx=0.05, rely=0.025)
        runningFile.pack(side='bottom', fill=BOTH, expand=True)

        insertFile = Button(column1, text="Insert File", width=15, height=2, borderwidth=2, relief='ridge', cursor='hand2', command=self.open_file_dialog)
        insertFile.pack(side='left', padx=5, pady=5)
        self.fileLabel = Label(column1, text=self.filename, padx=5, background='whitesmoke')
        self.fileLabel.pack(side='right', padx=5, pady=5)

    def create_column2(self):
        column2 = Frame(self, padx=15, pady=2, borderwidth=2, relief='groove', background='whitesmoke')
        column2.grid(row=1, column=1, sticky='nsew')

        xstAlgoCanvas = Canvas(column2, borderwidth=2, relief='sunken')
        xstAlgoFrame = Frame(xstAlgoCanvas)
        Label(xstAlgoFrame, text=self.xstAlgoContent, wraplength=self.screenWidth * 0.25, justify='left').pack()
        xstAlgoFrame.place(anchor=NW, relx=0.05, rely=0.025)
        xstAlgoCanvas.pack(side='bottom', fill=BOTH, expand=True)
        Label(column2, text='Existing Algorithm', pady=6, font=('Calibri Bold', 15), background='whitesmoke').pack(side='top')

    def create_column3(self):
        column3 = Frame(self, padx=15, pady=2, borderwidth=2, relief='groove', background='whitesmoke')
        column3.grid(row=1, column=2, sticky='nsew')

        newAlgoCanvas = Canvas(column3, borderwidth=2, relief='sunken')
        newAlgoFrame = Frame(newAlgoCanvas)
        Label(newAlgoFrame, text=self.newAlgoContent, wraplength=self.screenWidth * 0.25, justify='left').pack()
        newAlgoFrame.place(anchor=NW, relx=0.05, rely=0.025)
        newAlgoCanvas.pack(side='bottom', fill=BOTH, expand=True)
        Label(column3, text='New Algorithm', pady=6, font=('Calibri Bold', 15), background='whitesmoke').pack(side='top')

    def create_results_window(self):
        self.resultsWindow = Frame(self, padx=15, pady=2, borderwidth=2, relief='groove', background='whitesmoke')
        self.resultsWindow.grid(row=1, column=2, sticky='nsew')

        self.resultsText = Text(self.resultsWindow, wrap='word')
        self.resultsText.pack(expand=True, fill=BOTH)

    def summarize_text(self):
        if self.fileContent:
            summary = self.summarize_callback(self.fileContent)
            self.resultsText.delete(1.0, END)
            self.resultsText.insert(END, summary)

    def open_file_dialog(self):
        file_path = filedialog.askopenfilename(filetypes=[("Word Documents", "*.docx")])
        if file_path:
            self.filename = file_path
            self.fileLabel.config(text=self.filename)
            self.fileContent = self.read_docx_callback(file_path)
            self.runningFileLabel.config(text=self.fileContent)
            self.summarizer.config(state='normal')  # Enable summarize button
            print("File loaded and summarize button enabled.")

    def toggle_about(self):
        if self.show:
            self.aboutWindow.grid(row=1, column=1, sticky='nsew')
        else:
            self.aboutWindow.grid_forget()
        self.show = not self.show

    @staticmethod
    def load_image(path, subsample_x, subsample_y):
        image = Image.open(path)
        photo = ImageTk.PhotoImage(image)
        return photo.subsample(subsample_x, subsample_y)