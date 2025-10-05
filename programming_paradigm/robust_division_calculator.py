def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
        ans = num/den
        return  f'The result of the division is {ans}'
    
    except ValueError:
        return f'Error: Please enter numeric values only.'
    
    except ZeroDivisionError:
        return f'Error: Cannot divide by zero.'
