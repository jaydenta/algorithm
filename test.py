import pytest
from operate_file import *

def test_sum_elements_squares():
	actual = sum_element_squares([1,2,3])
	expect = 14
	assert actual == expect

def test_factorial():
	actual = factorial([1,2,3])
	expect = 6
	assert actual == expect

def test_find_letters():
	actual = find_letters(['a',1,'b',2,'c',3])
	expect = 3
	assert actual == expect