# python 3.8.8
# jupyter notebook
# https://en.wikipedia.org/wiki/Mutually_orthogonal_Latin_squares
# https://en.wikipedia.org/wiki/Latin_square
from numpy import unravel_index, repeat
from pprint import pprint
from itertools import combinations


def get_latin_squares(size=3):
    cube = repeat(-1, size ** 2).reshape((size, size))  # start cube with dummy -1s
    latin_squares = []
    position = 0  # we check if we reached last cell in cube
    def rec(cube, position):
        outer, inner = unravel_index(position, (size, size))  # translate one dim. index into two dim.
        options =     set(range(size)) \
                    - set(list(cube[outer, :]) + list(cube[:, inner])) \
                    - set([-1])
        for option in options:  # no options - recursion base case
            cube_ = cube.copy()
            cube_[outer, inner] = option  # make new cube, and change one cell
            if position < (size ** 2 - 1):  # not last element
                rec(cube_, position + 1)
            else:                           # last element
                latin_squares.append(cube_)
    rec(cube, position)
    return latin_squares


def get_mut_orth_latin_squares(latin_squares):
    size = len(latin_squares[0])
    mut_orth_latin_squares = []
    for a, b in list(combinations(latin_squares, 2)):  # compare every pais of cubes
        uniques = {str(x) + str(y) 
                                   for x, y in zip(  list(a.ravel()), 
                                                     list(b.ravel()),) }
        if len(uniques) == size ** 2:
            mut_orth_latin_squares.append((a, b))  
    return mut_orth_latin_squares


if __name__ == '__main__':
    latin_squares = get_latin_squares()
    mut_orth_latin_squares = get_mut_orth_latin_squares(latin_squares)
    pprint(mut_orth_latin_squares[0])
