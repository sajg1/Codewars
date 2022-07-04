import unittest
import Kata

class Test__7thKyu_FriendOrFoeTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Kata.friend(["Ryan", "Kieran", "Mark",]), ["Ryan", "Mark"])
    def test_2(self):
        self.assertEqual(Kata.friend(["Ryan", "Jimmy", "123", "4", "Cool Man"]), ["Ryan"])
    def test_3(self):
        self.assertEqual(Kata.friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]), ["Jimm", "Cari", "aret"])
    def test_4(self):
        self.assertEqual(Kata.friend(["Love", "Your", "Face", "1"]), ["Love", "Your", "Face"])
    def test_5(self):
        self.assertEqual(Kata.friend(["Hell", "Is", "a", "badd", "word"]), ["Hell", "badd", "word"])
    def test_5(self):
        self.assertEqual(Kata.friend(["Issa", "Issac", "Issacs", "ISISS"]), ["Issa"])
    def test_6(self):
        self.assertEqual(Kata.friend(["Robot", "Your", "MOMOMOMO"]), ["Your"])
    def test_7(self):
        self.assertEqual(Kata.friend(["Your", "BUTT"]), ["Your", "BUTT"])
    def test_8(self):
        self.assertEqual(Kata.friend(["Hello", "I", "AM", "Sanjay", "Gupt"]), ["Gupt"])
    def test_9(self):
        self.assertEqual(Kata.friend(["This", "IS", "enough", "TEst", "CaSe"]), ["This", "TEst", "CaSe"])
    def test_10(self):
        self.assertEqual(Kata.friend([]), [])

if __name__ == '__main__':
    unittest.main()