from gui import MainApp
from logic import Summarizer

if __name__ == "__main__":
    summarizer = Summarizer()
    app = MainApp(summarizer)
    app.mainloop()