from tkinter import BOTH, filedialog, Entry
from tkinter.ttk import Frame, Button, Label
import datetime
from main import main


class Window(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def openInputFile(self):
        self.inputFile = filedialog.askopenfilename()
        self.btnInputFile.config(text=self.inputFile[self.inputFile.rfind('/')+1:])

    def openEditFile(self):
        self.editFile = filedialog.askopenfilename()
        self.btnEditFile.config(text=self.editFile[self.editFile.rfind('/')+1:])

    def upload(self):
        main.main(self.inputFile, self.editFile, self.dateChange.get(), self.maxPriceEntry.get())

    def initUI(self):
        self.master.title("Острые предметы")
        self.pack(fill=BOTH, expand=True)

        source_text = Label(self, text="Исходный план")
        source_text.grid(row=1, column=0)

        self.btnInputFile = Button(self, text="Выберите файл", command=self.openInputFile)
        self.btnInputFile.grid(row=2, column=0)

        source_text1 = Label(self, text="Измененный план")
        source_text1.grid(row=1, column=1)

        self.btnEditFile = Button(self, text="Выберите файл", command=self.openEditFile)
        self.btnEditFile.grid(row=2, column=1)

        source_text2 = Label(self, text="Дата изменений")
        source_text2.grid(row=1, column=2)

        self.dateChange = Entry(self)
        self.dateChange.grid(row=2, column=2)
        date = str(datetime.datetime.now())
        self.dateChange.insert(0, date[:date.find(' ')])

        max_price_label = Label(self, text="Максимальная стоимость изменений")
        max_price_label.grid(row=3, column=0, columnspan=2)

        self.maxPriceEntry = Entry(self)
        self.maxPriceEntry.grid(row=4, column=0, columnspan=2)
        self.maxPriceEntry.insert(0, "0")

        upload = Button(self, text="ЗАГРУЗИТЬ", command=self.upload)
        upload.grid(row=3, column=2, rowspan=2, columnspan=2)
