"""RGB Colour Tuple Generator.

Generates a rgb tuple from a number, e.g a temperature, inside a range.
This is in answer to the question http://stackoverflow.com/q/43716818/5990054
It can only generate colour tuples from predefined constains however these can
be change or altered, in the code, to add colours like white and black.
You change it so you can dynamically assign colours and change an existing set
with another function which uses this, idk. Just an idea.
I have done some testing but if you do find bugs please either submit them
or do a pull request with a fix. Thanks.

Written by {0}
Version {1}
Status: {2}
Licensed under {3}
URL: {4}

"""

AUTHOR = "mtech0 | https://github.com/mtech0, http://stackoverflow.com/users/5990054/max"
LICENSE = "GNU-GPLv3 | https://www.gnu.org/licenses/gpl.txt"
VERSION = "1.0.0"
STATUS = "Development"
URL = ""
__doc__ = __doc__.format(AUTHOR, VERSION, STATUS, LICENSE, URL)


def get_rgb_colour(temp, lo=0, hi=100):
    """Get an RGB tuple from a temperature.

    This uses the outer rbg colour wheel for colours.
    You can make the gradiant what ever you want really.
    Like adding white and black.
    Colour wheel (info from http://www.colorspire.com/rgb-color-wheel/)
    (R: 255, G: 0, B: 0 -> R: 255, G: 0, B: 255 ->) R: 0, G: 0, B: 255 ->
    R: 0, G: 255, B: 255 -> R: 0, G: 255, B: 0 -> R: 255, G: 255, B 0 -> R: 255, G: 0, B: 0
    I have removed the first two stages to remove overlap.
    So this will use (R: 0, G: 0, B: 255) as the lowest value and
    (R: 255, G: 0, B: 0) as the highest.

    temp - The temperature value | int
    lo - Lowest temp where it is 100% blue | int
        / Defaults to 0
    hi - highest temp where it is 100% red | int
        / Defaults to 100

    """
    if temp < lo or temp > hi:
        raise ValueError("Temperature {0} not in range: {1}, {2}".format(temp, lo, hi))
        # You could change the range instead of raisng an error.
    if lo < 0: # There has got to be a better way but I can't think of it or find one.
        hi += lo * -1
        temp += lo * -1
        lo += lo * -1 # This one last or other will not change.
    temp_range = hi - lo
    pos = (1 / temp_range) * temp # Possition in range
    total_colours = 1020 # As there is 4 255 colour ranges.
    pos_in_colours = round(total_colours * pos) # Pos in all colours
    # print(temp, lo, hi, temp_range, pos, total_colours, pos_in_colours) # Debugging
    if pos_in_colours > 765: # R: 255, G: 255, B 0 -> R: 255, G: 0, B: 0.
        g = 255 - (pos_in_colours - 765) # Decreasing g when increasing pos
        return (255, g, 0)
    elif pos_in_colours > 510: # R: 0, G: 255, B: 0 -> R: 255, G: 255, B: 0
        r = pos_in_colours - 510 # Increasing r when increasing pos
        return (r, 255, 0)
    elif pos_in_colours > 255: # R: 0, G: 255, B: 255 -> R: 0, G: 255, B: 0
        b = 255 - (pos_in_colours - 255) # Decreasing b when increasing pos
        return (0, 255, b)
    else: # R: 0, G: 0, B: 255 -> R: 0, G: 255, B: 255
        g = pos_in_colours # Increasing g when increasing pos
        return (0, g, 255)


def main(): # Examples
    from random import randint
    print(__doc__, "\nget_rgb_colour():\n", get_rgb_colour.__doc__, "\nExamples:")
    for _ in range(3):
        lo = randint(-500,500)
        hi = randint(lo, lo+1000)
        n = randint(lo, hi)
        print("{0} in range {1}, {2}:".format(n, lo, hi), get_rgb_colour(n, lo, hi))

IMPORT_CREDITS = True # Disable this to not print info on import.
if __name__ == '__main__':
    main()
elif IMPORT_CREDITS:
    print(__doc__, "\nget_rgb_colour():\n", get_rgb_colour.__doc__,
          "\nTo disable this message on import go into the source file and change IMPORT_CREDITS, at the bottom, to False.")
