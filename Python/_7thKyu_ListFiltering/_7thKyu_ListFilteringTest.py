import unittest
import Kata

class Test__7thKyu_ListFilteringTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Kata.filter_list([1, 2, 'a', 'b']), [1, 2], 'For input [1, 2, "a", "b"]')
    def test_2(self):
        self.assertEqual(Kata.filter_list([1, 'a', 'b', 0, 15]), [1, 0, 15], 'Fot input [1, "a", "b", 0, 15]')
    def test_3(self):
        self.assertEqual(Kata.filter_list([1, 2, 'aasf', '1', '123', 123]), [1, 2, 123], 'For input [1, 2, "aasf", "1", "123", 123]')
    def test_4(self):
        self.assertEqual(Kata.filter_list(['a', 'b', '1']), [], 'For input ["a", "b", "1"]')
    def test_5(self):
        self.assertEqual(Kata.filter_list([1, 2, 'a', 'b']), [1, 2], 'For input ["1, 2, "a", "b"]')

if __name__ == '__main__':
    unittest.main()