"""
In this kata we want to convert a string into an integer. The strings simply
represent the numbers in words.

Examples:

    "one" => 1
    "twenty" => 20
    "two hundred forty-six" => 246
    "seven hundred eighty-three thousand nine hundred and nineteen" => 783919

Additional Notes:

    The minimum number is "zero" (inclusively)
    The maximum number, which must be supported is 1 million (inclusively)
    The "and" in e.g. "one hundred and twenty-four" is optional, in some cases
    it's present and in others it's not
    All tested numbers are valid, you don't need to validate them

"""

import re

with open('files/places.txt') as f:
    places_mapper = f.read().splitlines()

def parse_int(string):

    if string == "zero":
        return 0

    num_mapper = {"one": "1", "two": "2", "three": "3",
                  "four": "4", "five": "5", "six": "6",
                  "seven": "7", "eight": "8", "nine": "9",
                  "ten": "10", "eleven": "11", "twelve": "12",
                  "thirteen": "13", "fourteen": "14",
                  "fifteen": "15", "sixteen": "16",
                  "seventeen": "17", "eighteen": "18",
                  "nineteen": "19", "twenty": "20",
                  "thirty": "30", "forty": "40", "fifty": "50",
                  "sixty": "60", "seventy": "70", "eighty": "80",
                  "ninety": "90"}

    def format_string(string):
        string = string.replace(" and", "")
        string = string.replace("-", " ")
        return string

    def partition_places():
        places_partitioned = {}
        for place in places_mapper:
            places_partitioned[place] = '000'
        places_partitioned['hundred'] = '000'
        return places_partitioned


    def format_num():
        places = '|'.join(places_mapper)
        pattern = re.compile(f"(.*?(?:{places}))")
        matches = pattern.split(string)
        matches_stripped = [m.strip() for m in matches if m]
        num_list = [re.split('\s', i) for i in matches_stripped]

        for i, places in enumerate(num_list):
            nums = ""
            if places_mapper.count(places[-1]) > 0:
                diff = 2
            else:
                diff = 1
            for num in range(len(places) - diff, -1, -1):
                if places[num] == "hundred":
                    if num+1 > len(places) - diff:
                        nums = f"00"
                    elif len(num_mapper[places[num+1]]) == 1:
                        nums = f"0{nums}"
                elif len(num_mapper[places[num]]) == 2:
                    if num+1 > len(places) - diff:
                        nums = f"{num_mapper[places[num]]}{nums}"
                    else:
                        nums = f"{num_mapper[places[num]][0]}{nums}"
                else:
                    nums = f"{num_mapper[places[num]]}{nums}"

            if places_partitioned.get(places[-1]) == None:
                leading_zeros = 3 - len(nums)
                places_partitioned['hundred'] = f"{'0'*leading_zeros}{nums}"
            else:
                leading_zeros = 3 - len(nums)
                places_partitioned[places[-1]] = f"{'0'*leading_zeros}{nums}"

        return int(''.join(list(places_partitioned.values())))

    string = format_string(string)
    places_partitioned = partition_places()
    return format_num()

def main():
    helper = (
        f"Input a valid number up to '{places_mapper[0]}' (e.g. nine hundred "
        f"ninety nine {places_mapper[0]}and two"
            )
    print(helper)
    string = input()
    print(parse_int(string))

if __name__ == "__main__":
    main()
