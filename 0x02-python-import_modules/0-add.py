#!/usr/bin/python3
import sys
from add_0 import add

"""Importing and using a module

    Args:
        a : first integer
        b : second integer

    Returns:
        a print of the operations variables and unswears

"""
if __name__ == "__main__":
    a = 1
    b = 2

    print(f"{a} + {b} = {add(a,b)}")

    sys.exit(0)
