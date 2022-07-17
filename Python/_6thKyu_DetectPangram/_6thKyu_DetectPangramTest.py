import unittest
from Kata import is_pangram

class Test__6thKyu_DetectPangramTest(unittest.TestCase):
    #Positive tests
    def test_1(self):
        pangram = "The quick brown fox jumps over the lazy dog."
        self.assertEquals(is_pangram(pangram), True)
    def test_2(self):
        pangram1 = "Cwm fjord bank glyphs vext quiz"
        self.assertEquals(is_pangram(pangram1), True, pangram1 + " is a pangram")
    def test_3(self):
        pangram2 = "Pack my box with five dozen liquor jugs."
        self.assertEquals(is_pangram(pangram2), True, pangram2 + " is a pangram")
    def test_4(self):
        pangram3 = "How quickly daft jumping zebras vex."
        self.assertEquals(is_pangram(pangram3), True, pangram3 + " is a pangram")
    def test_5(self):
        pangram4 = "ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ"
        self.assertEquals(is_pangram(pangram4), True, pangram4 + " is a pangram")
    #Negative tests
    def test_6(self):
        not_pangram1 = "This isn't a pangram!"
        self.assertEquals(is_pangram(not_pangram1), False, not_pangram1 + " is not a pangram.")
    def test_7(self):
        not_pangram2 = "abcdefghijklmopqrstuvwxyz"
        self.assertEquals(is_pangram(not_pangram2), False, not_pangram2 + " is not a pangram.")
    def test_8(self):
        not_pangram3 = "Aacdefghijklmnopqrstuvwxyz"
        self.assertEquals(is_pangram(not_pangram3), False, not_pangram3 + " is not a pangram.")

if __name__ == '__main__':
    unittest.main()
