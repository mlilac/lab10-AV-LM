#https://github.com/mlilac/lab10-AV-LM.git
#Partner 1: Aniruth Venkedesh
#Partner 2: Lucas Moraes
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number.")
    try:
        return math.sqrt(a)
    except Exception as e:
        print(f"Error in square_root: {e}")
        return

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except Exception as e:
        print(f"Error in hypotenuse: {e}")
        return

# First example
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0: raise(ZeroDivisionError)
    return b / a

def logarithm(a, b):
    return math.log(b, a)

def exp(a, b):
    return a ** b


