"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

<<<<<<< HEAD
def square_root(a):
    try:
        if a < 0:
            raise ValueError("Cannot take square root of a negative number.")
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
=======
>>>>>>> f756465d641028aa4b64df8c27e683c3eec4912e
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0: raise(ZeroDivisionError)
    return b / a

def log(a, b):
    return math.log(b, a)

def exp(a, b):
    return a ** b


