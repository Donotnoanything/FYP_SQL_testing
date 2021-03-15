import unittest
from test.testcase import MR1

class TestStringMethods(unittest.TestCase):

    def test_MR1(self):
#Test input:        
        test = MR1("Dave")
#        print(test.input, test.output, test.test_input, test.test_output)
        self.assertEqual(test.output, test.test_output)

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()