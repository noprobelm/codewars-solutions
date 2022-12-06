"""
Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.

move_zeros(1012013) should return 1121300
"""

import re

def move_zeros(num):
    array = [int(i) for i in num]
    count = 0
    for num in array:
        if num == 0:
            count+=1

    for zeros in range(count):
        array.remove(0)
        array.append(0)
    return int(''.join([str(num) for num in array]))

def main():
    helper = (
        f"Input a valid int with zeros. The result will be an int with all "
        f"zeros moved to the end, while preserving the original order of the "
        f"other input digits."
            )
    print(helper)
    num = input()
    print(move_zeros(num))

if __name__ == "__main__":
    main()
