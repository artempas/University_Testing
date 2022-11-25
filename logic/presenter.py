from tkinter import *
from tkinter import messagebox
from enum import Enum
from logic.calcLogic import CalcLogic


class Operation(Enum):
    PLUS = "+"
    MINUS = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
    NONE = "="


class Presenter(Tk):
    def __init__(self):
        super(Presenter, self).__init__()
        self.__memory: float = 0
        self.resizable(False, False)
        self.__operation: Operation = Operation.NONE
        self.title("Калькулятор")
        self.memory_field = Label(
            text="",
            foreground="#E5C079",
            background="#282C34",
            font=("Roboto", 17),
            width=16,
            anchor="w",
        )
        self.input_field = Entry(
            self,
            validate="key",
            validatecommand=(self.register(self.__validate_input), "%S", "%P"),
            background="#2C313C",
            foreground="#528BFF",
            justify="right",
            font=("Roboto", 17),
            width=16,
            highlightthickness=0,
            bd=0,
        )
        self.configure(background="#282C34")
        pixel = PhotoImage(width=1, height=1)
        self.plus_button = Button(
            self,
            text="+",
            command=self.on_plus,
            font=("Roboto", 25),
            background="#BBBBBA",
            activebackground="#528BFF",
            highlightbackground="#528BFF",
            width=4,
        )
        self.minus_button = Button(
            self,
            text="-",
            command=self.on_subtract,
            font=("Roboto", 25),
            background="#BBBBBA",
            activebackground="#528BFF",
            highlightbackground="#528BFF",
            width=4,
        )
        self.divide_button = Button(
            self,
            text="÷",
            command=self.on_divide,
            font=("Roboto", 25),
            background="#BBBBBA",
            activebackground="#528BFF",
            highlightbackground="#528BFF",
            width=4,
        )
        self.multiply_button = Button(
            self,
            text="✕",
            command=self.on_multiply,
            font=("Roboto", 25),
            background="#BBBBBA",
            activebackground="#528BFF",
            highlightbackground="#528BFF",
            width=4,
        )
        self.equals_button = Button(
            self,
            text="=",
            command=self.calculate,
            font=("Roboto", 25),
            background="#BBBBBA",
            activebackground="#528BFF",
            highlightbackground="#528BFF",
            width=9,
        )

        self.memory_field.grid(row=0, column=0, columnspan=2, sticky="W")
        self.input_field.grid(row=1, column=0, columnspan=2)
        self.plus_button.grid(row=2, column=0, sticky="E")
        self.minus_button.grid(row=2, column=1, sticky="W")
        self.divide_button.grid(row=3, column=0, sticky="E")
        self.multiply_button.grid(row=3, column=1, sticky="W")
        self.equals_button.grid(row=4, columnspan=2)

    @property
    def operation(self):
        return self.__operation

    @operation.setter
    def operation(self, value):
        match self.__operation:
            case Operation.PLUS:
                self.plus_button.config(relief=RAISED)
            case Operation.MINUS:
                self.minus_button.config(relief=RAISED)
            case Operation.DIVIDE:
                self.divide_button.config(relief=RAISED)
            case Operation.MULTIPLY:
                self.multiply_button.config(relief=RAISED)
        self.__operation = value
        match self.__operation:
            case Operation.PLUS:
                self.plus_button.config(relief=SUNKEN)
            case Operation.MINUS:
                self.minus_button.config(relief=SUNKEN)
            case Operation.DIVIDE:
                self.divide_button.config(relief=SUNKEN)
            case Operation.MULTIPLY:
                self.multiply_button.config(relief=SUNKEN)

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value
        if value is None:
            self.memory_field["text"] = "ОШИБКА"
        else:
            self.memory_field["text"] = str(
                self.memory if self.memory % 1 else round(self.memory)
            )[:16]

    def on_plus(self):
        if self.input_field.get():
            if self.memory and self.operation != Operation.NONE:
                try:
                    self.memory = self.__perform_operation()
                    self.input_field.delete(0, "end")
                except ZeroDivisionError:
                    self.memory = None
                    self.memory_field["text"] = "ОШИБКА"
            else:
                self.memory = float(self.input_field.get())
                self.input_field.delete(0, "end")
        self.operation = Operation.PLUS

    def on_multiply(self):
        if self.input_field.get():
            if self.memory and self.operation != Operation.NONE:
                try:
                    self.memory = self.__perform_operation()
                    self.input_field.delete(0, "end")
                except ZeroDivisionError:
                    self.memory = None
                    self.memory_field["text"] = "ОШИБКА"
            else:
                self.memory = float(self.input_field.get())
                self.input_field.delete(0, "end")
        self.operation = Operation.MULTIPLY

    def on_subtract(self):
        if self.input_field.get():
            if self.memory and self.operation != Operation.NONE:
                try:
                    self.memory = self.__perform_operation()
                    self.input_field.delete(0, "end")
                except ZeroDivisionError:
                    self.memory = None
                    self.memory_field["text"] = "ОШИБКА"
            else:
                self.memory = float(self.input_field.get())
                self.input_field.delete(0, "end")
        self.operation = Operation.MINUS

    def on_divide(self):
        if self.input_field.get():
            if self.memory and self.operation != Operation.NONE:
                try:
                    self.memory = self.__perform_operation()
                    self.input_field.delete(0, "end")
                except ZeroDivisionError:
                    self.memory = None
                    self.memory_field["text"] = "ОШИБКА"
            else:
                self.memory = float(self.input_field.get())
                self.input_field.delete(0, "end")
        self.operation = Operation.DIVIDE

    def calculate(self):
        print(f"{self.operation=}")
        if self.input_field.get():
            if self.operation == Operation.NONE:
                print("code needed")
                self.memory = float(self.input_field.get())
                self.input_field.delete(0, "end")
            else:
                try:
                    self.memory = self.__perform_operation()
                    self.input_field.delete(0, "end")
                except ZeroDivisionError:
                    self.memory = None
            self.operation = Operation.NONE

    def __perform_operation(self):
        logic = CalcLogic(self.memory, float(self.input_field.get()))
        result = None
        match self.operation:
            case Operation.PLUS:
                result = logic.sum()
                self.plus_button.config(relief=RAISED)
            case Operation.MINUS:
                result = logic.subtract()
                self.minus_button.config(relief=RAISED)
            case Operation.DIVIDE:
                result = logic.divide()
                self.divide_button.config(relief=RAISED)
            case Operation.MULTIPLY:
                result = logic.multiply()
                self.multiply_button.config(relief=RAISED)
        return result

    def __validate_input(self, char: str, new_val: str):
        print(f"{char=} {new_val=}")
        if new_val:
            match self.operation:
                case Operation.PLUS:
                    self.plus_button.config(relief=RAISED)
                case Operation.MINUS:
                    self.minus_button.config(relief=RAISED)
                case Operation.DIVIDE:
                    self.divide_button.config(relief=RAISED)
                case Operation.MULTIPLY:
                    self.multiply_button.config(relief=RAISED)
        else:
            match self.operation:
                case Operation.PLUS:
                    self.plus_button.config(relief=SUNKEN)
                case Operation.MINUS:
                    self.minus_button.config(relief=SUNKEN)
                case Operation.DIVIDE:
                    self.divide_button.config(relief=SUNKEN)
                case Operation.MULTIPLY:
                    self.multiply_button.config(relief=SUNKEN)
            return True

        return (
            char in "0123456789.-" and new_val.count(".") < 2 and new_val.find("-") < 1
        )
