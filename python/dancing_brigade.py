"""
Mothers arranged a dance party for the children in school. At that party, there
are only mothers and their children. All are having great fun on the dance floor
 when suddenly all the lights went out. It's a dark night and no one can see
each other. But you were flying nearby and you can see in the dark and have
 ability to teleport people anywhere you want.

Legend:

-Uppercase letters stands for mothers, lowercase stand for their children, i.e.
"A" mother's children are "aaaa".
-Function input: String contains only letters, uppercase letters are unique.

Task:
Place all people in alphabetical order where Mothers are followed by their
children, i.e. "aAbaBb" => "AaaBbb".
"""

def find_children(dancing_brigade):
    dancing_brigade_sorted = sorted(dancing_brigade.lower())
    for i in dancing_brigade:
        if i.isupper():
            dancing_brigade_sorted[dancing_brigade_sorted.index(i.lower())] = i.upper()
    return ''.join(dancing_brigade_sorted)

def main():
    helper = (
        f"Function will return all input letters in alphabetical order with "
        f"capital letters leading. Uppercase letters must be unique and have "
        f"accompanying lower case characters elsewhere in the string."
    )
    print(helper)
    dancing_brigade = input()
    print(find_children(dancing_brigade))

if __name__ == "__main__":
    main()
