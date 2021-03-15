#Generating Test Cases
import sys
sys.path.append("..")
from src.app import *
# MR1
# the result of searching name should be the same as
# the result of searching its co-ressponding id
class MR1:
	def __init__(self, input): 
		self.input = input
		self.output = sql_queryname(input)
		if self.output:
			self.test_input = self.output[0][0]
			self.test_output = sql_queryid(self.test_input)
		else:
			self.test_input = 0
			self.test_output = sql_queryid(self.test_input)

		


		
