# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 13:32:39 2024

@author: meifrank38
"""

import math_func
import pytest

def test_add():
    assert math_func.add(1, 2) == 3, "應該返回兩個數字的和"
    assert math_func.add(-1, 1) == 0, "正負數相加應該為0"
    assert math_func.add(-1, -1) == -2, "兩個負數相加的結果檢查"
    #assert math_func.add(-1, -1) == 2, "test add assert failure"
    
def test_sub():
    assert math_func.sub(1, 2) == -1
    assert math_func.sub(2, 1) == 1 
    assert math_func.sub(1, 1) == 0
    assert math_func.sub(-1, -1) == 0
    #assert math_func.sub(1, 3) == 2
    
@pytest.mark.parametrize("test_input,expected", [(2, 6), (3, 9), ]) #(5, 6)
def test_multi(test_input, expected):
    assert math_func.multiply(test_input, 3) == expected
    
def test_divide():
    assert math_func.divide(6, 3) == 2
    assert math_func.divide(10, 2) == 5
    try:
        math_func.divide(5, 0)
    except ValueError as e:
        assert str(e) == "除數不能為0"
    else:
        assert False
        
#@pytest.mark.string
def test_add_strings():
    result = math_func.add('Hello', ' World')
    assert result == 'Hello World'
    assert type(result) is str
    assert 'Hello' in result