"""
Complete the method which returns the number which is most frequent in the given
input array. If there is a tie for most frequent number, return the largest
number among them.
Note: no empty arrays will be given.
"""

from collections import Counter
import re

def highest_rank(arr):
    return Counter(sorted(arr, reverse=True)).most_common()[0][0]

def main():
    helper = (
        f"Function takes a list of numbers and returns the most frequently "
        f"occurring. If there is a tie for the most frequent number, return "
        f"the largest.\n"
    )

    print(helper)
    print("Input a series of numbers (do not use delimiters)")
    arr = list(input())
    print(highest_rank(arr))

if __name__ == "__main__":
    main()
