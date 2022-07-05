import unittest
from Kata import disemvowel

class Test__7thKyu_FriendOrFoeTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(disemvowel("This website is for losers LOL!"), "Ths wbst s fr lsrs LL!")
    def test_2(self):
        self.assertEqual(disemvowel("No offense but,\nYour writing is among the worst I've ever read"), "N ffns bt,\nYr wrtng s mng th wrst 'v vr rd")
    def test_3(self):
        self.assertEqual(disemvowel("What are you, a communist?"), "Wht r y,  cmmnst?")
    

if __name__ == '__main__':
    unittest.main()