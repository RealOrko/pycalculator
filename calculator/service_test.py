import unittest

from model import *
from service import *

class TestCalculatorService(unittest.TestCase): 

    def test_get_total_with_simple_values(self):

        model: CalculatorStack = CalculatorStack()
        model.push_number(CalculatorValue(1.1))
        model.push_operation(CalculatorOperation.ADD)
        model.push_number(CalculatorValue(1.6))
        
        service: CalculatorService = CalculatorService()
        self.assertEqual(2.7, service.get_total(model))

if __name__ == '__main__':
    unittest.main()
