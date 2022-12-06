"""
ROT13 is a simple letter substitution cipher that replaces a letter with the
letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar
cipher.

Create a function that takes a string and returns the string ciphered with
Rot13. If there are numbers or special characters included in the string, they
should be returned as they are. Only letters from the latin/english alphabet
should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
"""

import re
def rot13(message):
    alphabet = [chr(uni) for uni in range(97, 123)]
    def encode_char(char):
        if re.search('[a-z]', char):
            if 25 - alphabet.index(char) < 13:
                return alphabet[abs(13 - alphabet.index(char))]
            else:
                return alphabet[alphabet.index(char) + 13]
        else:
            return char

    return ''.join([encode_char(char.lower()).upper() if char.isupper() else
                    encode_char(char) for char in message])

def main():
    helper = (
        f"Input a string. Function will return the rot13 equivalent. spaces,"
        f"special characters, and digits are acceptable."
        )

    message = input()
    print(rot13(message))

if __name__ == "__main__":
    main()
