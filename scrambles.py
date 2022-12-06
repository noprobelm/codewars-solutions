"""
Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

    Only lower case letters will be used (a-z). No punctuation or digits will be included.
    Performance needs to be considered

Input strings s1 and s2 are null terminated.

Examples

scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
"""

def scramble(s1, s2):
    def count_char(s):
        s_count = {}
        for char in s:
            if s_count.get(char) == None:
                s_count[char] = 1
            else:
                s_count[char] += 1
        return s_count

    s1_count = count_char(s1)
    s2_count = count_char(s2)
    for char in s2_count:
        if s1_count.get(char) == None:
            return False
        elif s1_count[char] < s2_count[char]:
            return False
    return True

def main():
    helper = (
        f"Input 2 strings. Function will return True if a portion of str1 "
        f"characters can be rearranged to match str2. Otherwise, return False. "
        f"\n"
        )
    print("Input str1:")
    s1 = input()
    print("Input str2:")
    s2 = input()
    print(scramble(s1, s2))

if __name__ == "__main__":
    main()
