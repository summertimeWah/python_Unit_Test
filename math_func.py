# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 13:27:09 2024

@author: meifrank38
"""

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("除數不能為0")
    return a / b