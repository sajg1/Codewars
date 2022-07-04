import unittest
import Kata

class Test__6thKyu_CreatePhoneNumber(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Kata.create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
    def test_2(self):
        self.assertEqual(Kata.create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")
    def test_3(self):
        self.assertEqual(Kata.create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
    def test_4(self):
        self.assertEqual(Kata.create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890")
    def test_5(self):
        self.assertEqual(Kata.create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")
    

if __name__ == '__main__':
    unittest.main()
