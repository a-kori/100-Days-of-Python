def add(n1, n2):
    """Adds n1 to n2"""
    return n1 + n2

def subtract(minuend, subtrahend):
    """Subtracts subtrahend from minuend"""
    return minuend - subtrahend

def multiply(n1, n2):
    """Multiplies n1 by n2"""
    return n1 * n2

def divide(dividend, divisor):
    """Divides dividend by divisor, unless divisor is equal to 0"""
    if divisor != 0:
        return dividend / divisor
    else:
        return "You cannot divide a number by zero! Try again."
