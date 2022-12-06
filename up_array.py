"""
Given an array of integers of any length, return an array that has 1 added to
the value represented by the array.

    the array can't be empty
    only non-negative, single digit integers are allowed

Return nil (or your language's equivalent) for invalid inputs.
Examples

For example the array [2, 3, 9] equals 239, adding one would return the array
[2, 4, 0].

[4, 3, 2, 5] would return [4, 3, 2, 6]
"""

def up_array(arr):
    for i in arr:
        if i < 0 or i > 9:
            return None
    if not arr:
        return None
    
    else:     
        num = ''.join([str(i) for i in arr])
        num = int(num)+1
        return [int(i) for i in str(num)]

def main():
    helper = (
        f"Given an list of integers, this function will return a list of "
        f"integers where the joined value of all ints is incremented by 1. "
        f"uses simple string methods and list comprehension to join the list, "
        f"typecast to int, increment by 1, then return a new list.\n\n"
    )

    print("Input an int. main() will convert to a list and pass to the func.")
    arr = [int(i) for i in input()]
    print(f"List being passed is {arr}")
    print(f"List of ints incremented by 1 is {up_array(arr)}")

if __name__ == "__main__":
    main()
