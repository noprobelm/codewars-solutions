"""
A pangram is a sentence that contains every single letter of the alphabet at
least once. For example, the sentence "The quick brown fox jumps over the lazy
dog" is a pangram, because it uses the letters A-Z at least once (case is
irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is,
False if not. Ignore numbers and punctuation.

"""

import re

def is_pangram(s):
    alphabet = [chr(uni) for uni in range(97, 123)] 
    pangram_test = sorted([char for char in list(re.sub('\W', '', s.lower()))])
    for letter in alphabet:
        if letter not in pangram_test:
            return False
    return True

def main():
    helper = (
        f"Input a string. Function will determine if the string is a pangram "
        f"(each letter of the alphabet exists one or more times). Returns "
        f"True or False"
    )

    print("Input a string:")
    s = input()
    print(is_pangram(s))

if __name__ == "__main__":
    main()
