def perform_operation(num1: float, num2: float, operation: str):
    operation = operation.lower()
    
    if operation == 'add':
        addation = num1 + num2
        return addation
    elif operation == 'subtract':
        subtraction = num1 - num2
        return subtraction
    elif operation == 'multiply':
        multiplication = num1 * num2
        return multiplication
    elif operation == 'divide':
        if num2 == 0:
            return "Error: You can NOT divide by zero"
        division = num1 / num2
        return division
        return "Error: Invalid operation"
    
    