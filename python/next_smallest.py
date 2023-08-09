"""
Write a function that takes a positive integer and returns the next smaller
 positive integer containing the same digits.

For example:

next_smaller(21) == 12
next_smaller(531) == 513
next_smaller(2071) == 2017

Return -1 (for Haskell: return Nothing, for Rust: return None), when there is no
 smaller number that contains the same digits. Also return -1 when the next
 smaller number with the same digits would require the leading digit to be zero.

next_smaller(9) == -1
next_smaller(135) == -1
next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros

Some tests will include very large numbers.
Test data only employs positive integers.
"""
def next_smallest(n):
    nums = [int(digit) for digit in str(n)]
    for i in range(len(nums)-1, -1, -1):
        if i-1 >= 0:
            right = sorted(nums[i:],reverse=True)
            for k, val in enumerate(right):
                if nums[i-1] > val:
                    smaller = nums[:i-1]
                    smaller.append(val)
                    right[k] = nums[i-1]
                    smaller.extend(right)
                    if smaller[0] == 0:
                        return -1
                    else:
                        return int(''.join(str(num) for num in smaller))
        else:
            return -1
def main():

    helper = (
        f"Input any valid integer. The function will return the next smallest "
        f"possible integer using the same digits. If there is no smaller "
        f"number which retains the same number of digits, or there is no "
        f"smaller number, return -1."
            )

    print(helper)
    string = input()
    print(next_smallest(string))

if __name__ == "__main__":
    main()
