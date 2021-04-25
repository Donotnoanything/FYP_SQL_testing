import unittest
from test.testcase import MR1
from src.app import *



class TestStringMethods(unittest.TestCase):

    def __init__(self, input): 
        super(TestStringMethods, self).__init__()
        self.input = input
        self.output = sql_queryname(input)
        if self.output:
            self.test_input = self.output[0][0]
            self.test_output = sql_queryid(self.test_input)
        else:
            self.test_input = 0
            self.test_output = sql_queryid(self.test_input)


    def runTest(self):
#Test input:        
        test = MR1(self.input)
#        print(test.input, test.output, test.test_input, test.test_output)
        self.assertEqual(test.output, test.test_output)


def suite():
    suite = unittest.TestSuite()
    with open('sql') as f:
        allinput = f.read().splitlines()

    suite.addTests(TestStringMethods(input) for input in allinput)
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())


