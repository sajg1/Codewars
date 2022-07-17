import string

def is_pangram(s):
    test_str = s.lower()
    alphabet = list(string.ascii_lowercase)
    
    for letter in test_str:
        if letter in alphabet:
            alphabet.remove(letter)
    
    return len(alphabet) == 0
