from tkinter import *
from tkinter import filedialog
from logic.global_var import show, result, chosenFile
from logic.other_funcs import open_file_dialog

class ThesisSimulationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Thesis Simulation")
        self.initialize_gui()

    def initialize_gui(self):
        # Initialize and place the buttons and other widgets here
        self.create_buttons()

    def create_buttons(self):
        self.summarizer = Button(self.root, text='Summarize', borderwidth=2, state='normal', background='antiquewhite', width=12, height=2, activebackground='antiquewhite4', activeforeground="white", font=('Calibri Bold', 9), cursor='hand2', command=self.toggle_summarizer)
        self.summarizer.place(relx=0.78, rely=0.05, anchor=NE)

        self.results = Button(self.root, text='Results', borderwidth=2, state='normal', background='antiquewhite', width=12, height=2, activebackground='antiquewhite4', activeforeground="white", font=('Calibri Bold', 9), cursor='hand2', command=self.toggle_tab_results)
        self.results.place(relx=0.88, rely=0.05, anchor=NE)

    def toggle_about(self, e):
        global show
        if show:
            self.aboutWindow.place(relx=0.99, rely=0.15, anchor=NE)
        else:
            self.aboutWindow.place_forget()
        show = not show

    def toggle_summarizer(self):
        self.summarizer.after(500, self.toggle_results)

    def toggle_results(self):
        global result
        if result:
            self.resultsWindow.place(anchor=SE, relx=0.98, rely=0.9)
        else:
            self.resultsWindow.place_forget()
        result = not result

def main():
    root = Tk()
    app = ThesisSimulationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
