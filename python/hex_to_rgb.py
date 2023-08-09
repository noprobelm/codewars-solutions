"""
When working with color values it can sometimes be useful to extract the individual red, green, and blue (RGB) component values for a color. Implement a function that meets these requirements:

    Accepts a case-insensitive hexadecimal color string as its parameter (ex. "#FF9933" or "#ff9933")
    Returns an object with the structure {r: 255, g: 153, b: 51} where r, g, and b range from 0 through 255

Note: your implementation does not need to support the shorthand form of hexadecimal notation (ie "#FFF")
Example

"#FF9933" --> {r: 255, g: 153, b: 51}
"""

# This solution was developed for the purpose of mental exercise, and is by
# no means the most efficient method. A more efficient method can be developed
# by typecasting each portion of the hex input to int and passing '16' as the
# base to be used. A method such as this is demonstrated in the
# 'hex_string_to_RGB_efficient' function written below this function.
def hex_string_to_RGB(hex_string): 
    hex_dict = {'r':hex_string[1:3], 'g':hex_string[3:5], 'b':hex_string[5:7]}
    rgb_dict = {}
    letters = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5}
    for color in hex_dict:
        color_rgb = 0
        if hex_dict[color][0].isdigit():
            color_rgb = int(hex_dict[color][0]) * 16
        else:
            for letter in letters:
                if letter in hex_dict[color][0].lower():
                    color_rgb = 160 + letters[hex_dict[color][0].lower()] * 16
        if hex_dict[color][1].isdigit():
            color_rgb = color_rgb + int(hex_dict[color][1])
        else:
            for letter in letters:
                if letter in hex_dict[color][1].lower():
                    color_rgb = color_rgb + letters[hex_dict[color][1].lower()] + 10
        rgb_dict[color] = color_rgb
    return rgb_dict

def hex_string_to_RGB_efficient(hex_string):
    hex_dict = {'r':hex_string[1:3], 'g':hex_string[3:5], 'b':hex_string[5:7]}
    rgb_dict = {}

    for color in hex_dict:
        rgb_dict[color] = int(hex_dict[color], 16)
    return rgb_dict

def main():
    helper = (
        f"Input a color represented in hex format. Ensure color is preceded "
        f"with '#' symbol"
    )

    print(helper)
    hex_string = input()
    print(hex_string_to_RGB(hex_string))

if __name__ == "__main__":
    main()
