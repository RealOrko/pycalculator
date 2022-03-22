from enum import Enum

class CalculatorValue:

    value: float = 0.0

    def __init__(self, value: float) -> None:
        self.value = value

class CalculatorOperation(Enum):
    
    ADD = 1
    SUBTRACT = 2
    DIVIDE = 3
    MULTIPLY = 4

class CalculatorStack:

    values = []

    def __init__(self) -> None:
        pass

    def clear(self):
        self.values = []

    def push_number(self, value: CalculatorValue) -> None:
        self.values.append(value)

    def push_operation(self, operation: CalculatorOperation) -> None:
        self.values.append(operation)
