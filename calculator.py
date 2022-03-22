from tkinter import *
from calculator.model import CalculatorStack
from calculator.service import CalculatorService
from ui.window import *
from calculator import *

calculator_stack = CalculatorStack()
calculator_service = CalculatorService()

def main():
    win = Window("Calculator", window_handler)
    win.start()

def window_handler(arg, expression):
    print(arg)
    print(expression)

if __name__ == "__main__":
    main()
