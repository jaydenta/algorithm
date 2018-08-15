import pytest
from operate_file import *
def sum_element_squares(l):
	x = 0
	for i in l:
		x = x + ((i)**2)
	return x


print(sum_element_squares([1,2,3]))