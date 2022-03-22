from threading import local
from tkinter import *

class Window:

    root: Tk = None
    event_handler = None
    output_entry: Entry = None

    def __init__(self, title, event_handler) -> None:

        self.event_handler = event_handler

        self.root = Tk()
        self.root.title(title)
        self.root.columnconfigure(0, weight=1)
        self.root.geometry('1000x1000')
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        top_frame = Frame(self.root)
        top_frame.rowconfigure(0, weight=1, minsize=150)
        top_frame.columnconfigure(0, weight=1)
        top_frame.grid(row=0, sticky='ew')
        self.output_entry = Entry(top_frame, font=('Arial', 28))
        self.output_entry.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)

        center = Frame(self.root, width=50, height=40, padx=3, pady=3)
        center.grid(row=1, sticky='nsew')
        center.grid_rowconfigure(0, weight=1)
        center.grid_columnconfigure(1, weight=1)

        center_mid = Frame(center, width=150, padx=3, pady=3)
        center_mid.grid(row=0, column=1, sticky='nsew')
        center_mid.grid_rowconfigure(0, weight=1)
        center_mid.grid_columnconfigure(0, weight=1)
        
        counter = 0
        for row_index in range(3):
            center_mid.rowconfigure(row_index, weight=1)
            for column_index in range(3):
                counter = counter + 1
                center_mid.columnconfigure(column_index, weight=1)
                digit_button = Button(center_mid, text=counter, font=('Arial', 22))
                digit_button.bind('<Button>', self.button_clicked)
                digit_button.grid(row=row_index, column=column_index, sticky="nsew")
        
        center_mid.rowconfigure(row_index+1, weight=1)
        digit_button = Button(center_mid, text=0, font=('Arial', 22))
        digit_button.bind('<Button>', self.button_clicked)
        digit_button.grid(row=row_index+1, columnspan=3, sticky="nsew")

        center_right = Frame(center, width=450, padx=5, pady=5)
        center_right.grid(row=0, column=2, sticky='nesw')

        center_right.rowconfigure(0, weight=1)
        center_right.columnconfigure(0, weight=1, minsize=250)
        clear_button = Button(center_right, text="C", font=('Arial', 22))
        clear_button.bind('<Button>', self.button_clicked)
        clear_button.grid(row=0, column=0, sticky='nesw')

        center_right.rowconfigure(1, weight=1)
        multiply_button = Button(center_right, text="x", font=('Arial', 22))
        multiply_button.bind('<Button>', self.button_clicked)
        multiply_button.grid(row=1, column=0, sticky='nesw')

        center_right.rowconfigure(2, weight=1)
        divide_button = Button(center_right, text="÷", font=('Arial', 22))
        divide_button.bind('<Button>', self.button_clicked)
        divide_button.grid(row=2, column=0, sticky='nesw')

        center_right.rowconfigure(3, weight=1)
        add_button = Button(center_right, text="+", font=('Arial', 22))
        add_button.bind('<Button>', self.button_clicked)
        add_button.grid(row=3, column=0, sticky='nesw')

        center_right.rowconfigure(4, weight=1)
        subtract_button = Button(center_right, text="-", font=('Arial', 22))
        subtract_button.bind('<Button>', self.button_clicked)
        subtract_button.grid(row=4, column=0, sticky='nesw')

        center_right.rowconfigure(5, weight=1)
        decimal_button = Button(center_right, text=".", font=('Arial', 22))
        decimal_button.bind('<Button>', self.button_clicked)
        decimal_button.grid(row=4, column=0, sticky='nesw')

        bottom = Frame(self.root, padx=3, pady=3)
        bottom.grid(row=3, sticky='ew')
        bottom.grid_rowconfigure(0, weight=1, minsize=150)
        bottom.grid_columnconfigure(0, weight=1)
        
        equals_button=Button(bottom, text="=", font=('Arial', 22))
        equals_button.bind('<Button>', self.button_clicked)
        equals_button.grid(row=0, column=0, sticky='nesw')

    def start(self):
        self.root.mainloop()
    
    def button_clicked(self, event):
        argument = event.widget['text']
        self.output_entry.insert(END, event.widget['text'])
        self.event_handler(argument, self.output_entry.get())

