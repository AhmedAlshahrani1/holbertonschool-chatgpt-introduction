#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
        Calculates the factorial of a non-negative integer using recursion.
    
    Parameters:
        n (int): The integer number for which the factorial is to be calculated.
    
    Returns:
        int: The factorial of the number `n`. If `n` is 0, it returns 1.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
