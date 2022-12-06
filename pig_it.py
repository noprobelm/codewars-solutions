"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
Examples

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""

def pig_it(text):
    text = text.split(' ')
    for i, k in enumerate(text):
        if k.isalpha():
            text[i] = k[1:] + k[0] + 'ay'
    return ' '.join(text)

def main():
    helper = (
        f"Input a string. Function will convert the string to Pig Latin and "
        f"return it."
    )
    text = input()
    print(pig_it(text))

if __name__ == "__main__":
    main()
