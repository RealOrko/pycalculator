from calculator.model import *

class CalculatorService:
    
    def get_total(self, model: CalculatorStack) -> float:

        result: float = 0.0

        leftValue: CalculatorValue = None
        rightValue: CalculatorValue = None
        operation: CalculatorOperation = None

        for x in model.values:
            
            if isinstance(x, CalculatorValue) and leftValue is None:
                leftValue = x 
                continue
            
            if isinstance(x, CalculatorOperation) and operation is None:
                operation = x
                continue

            if isinstance(x, CalculatorValue) and rightValue is None:
                rightValue = x 
            
            if (leftValue is not None) and (rightValue is not None) and (operation is not None): 

                if operation == CalculatorOperation.ADD:
                    result += leftValue.value + rightValue.value
                
                if operation == CalculatorOperation.SUBTRACT:
                    result += leftValue.value - rightValue.value
                
                if operation == CalculatorOperation.MULTIPLY:
                    result += leftValue.value * rightValue.value
                
                if operation == CalculatorOperation.DIVIDE:
                    result += leftValue.value / rightValue.value

        return result
