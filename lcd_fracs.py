"""
Common denominators

You will have a list of rationals in the form
{ {numer_1, denom_1} , ... {numer_n, denom_n} }
or
[ [numer_1, denom_1] , ... [numer_n, denom_n] ]
or
[ (numer_1, denom_1) , ... (numer_n, denom_n) ]

where all numbers are positive ints. You have to produce a result in the form:
(N_1, D) ... (N_n, D)
or
[ [N_1, D] ... [N_n, D] ]
or
[ (N_1', D) , ... (N_n, D) ]
or
{{N_1, D} ... {N_n, D}}
or
"(N_1, D) ... (N_n, D)"

depending on the language (See Example tests) in which D is as small as possible and

N_1/D == numer_1/denom_1 ... N_n/D == numer_n,/denom_n.

Example:

convertFracs [(1, 2), (1, 3), (1, 4)] `shouldBe` [(6, 12), (4, 12), (3, 12)]
"""

# NumPy is necessary in order to efficiently handle very large LCDs
import numpy as np
import re

def convert_fracts(lst):
    if len(lst) == 0:
        return []

    denominators = []
    for frac in lst:
        denominators.append(frac[1])

    # It's important we cast this result to int, otherwise we will be
    # calculating the numerator using operations against numpy int64
    # and Python int, which will produce inaccurate results.
    lcm = np.lcm.reduce(denominators)

    for frac in lst:
        frac[0] = np.int64(frac[0]) * lcm // np.int64(frac[1])
        frac[1] = lcm
    return lst

def main():
    helper = (
        f"Input a list of fractions formatted as '1/3 3/4 4/12'. Do not use "
        f"delimiters other than whitespace. Function will locate the least "
        f"common denominator and convert the fractions. Fractions with very "
        f"large LCDs are acceptable."
    )
    print(helper)
    string = input()
    lst_unsplit = re.split('\s', string)
    lst_string = [re.split('\/', frac) for frac in lst_unsplit]
    lst_int = [[int(num) for num in frac] for frac in lst_string]
    print(convert_fracts(lst_int))

if __name__ == "__main__":
    main()
