import operator

#Dictionary mapping operator symbols to corresponding functions
OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

def calculate(expression):
    """Evaluate the arithmetic expression and return the result."""
    try:
        operand1, operator, operand2 = expression.split()
        operand1 = float(operand1)
        operand2 = float(operand2)
        
        if operator in OPERATORS:
            return OPERATORS[operator](operand1, operand2)
        else:
            return None  # Invalid operator
    except (ValueError, ZeroDivisionError):
        return None  # Invalid expression or division by zero

def main():
    while True:
        expression = input("Enter an arithmetic expression (operand1 operator operand2,'quit' to exit): ")
        if expression.lower() == 'quit':
            break
        
        result = calculate(expression)
        if result is not None:
            print("Result:", result)
        else:
            print("Invalid expression or operator.")
    
    print("Calculator closed.")

if __name__ == '__main__':
    main()

