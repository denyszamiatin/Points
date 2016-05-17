'''
TODO value check in install_dot
TODO same_dots list should to be relocated. to refresh correctly
make doc test
'''
import string
from generate_field import generate_field
from display_field import output_field, create_list_alphabet

field = generate_field()


def make_dict():
    '''
    Create a dictionary with numerate letters.
    Using for translation letters into digits
    :return:
    '''
    return {letter: i for i, letter in enumerate(create_list_alphabet())}


def is_free(x, y):
    return not field[y][dict[x]]


def check_around(y, x, marker=1):
    '''
    Check position for similar marker in position around,
    if marker the same = append position to the same_dots list
    :param x:
    :param y:
    :return:
    '''
    list_yx = ((0, 1), (-1, 1), (-1, 0), (-1, -1),
               (0, -1), (1, -1), (1, 0), (1, 1))

    same_dots = [
        (y + y_offset, x + x_offset)
         for y_offset, x_offset in list_yx
         if field[y + y_offset][x + x_offset] == marker
    ]
    return same_dots


def remove_previous_position(dots, prev_pos):
    if prev_pos in dots:
        dots.remove(prev_pos)
    return dots


def create_path(y, x, path, a=0, b=0):
    '''
    Function use check_around() func that:
    looking for points that surround start point in hop equal 1
    and that have the same marker(the same param of point)
    After that it's begin to check for closed circuit, build by
    points.
    :param y: input y
    :param x: input x
    :param path: list with nested list's, consists coordinates of points,
    which formed a closed circuit
    :param a, b: vars that needed in order to exclude start point
    from new search.
    :return: created path.
    '''
    if (y, x) in path:
        return path
    dots_around = remove_previous_position(check_around(y, x), a, b)
    a, b = y, x
    if dots_around:
        for y_p, x_p in dots_around:
            create_path(y_p, x_p, path + [(y, x)], a, b)


def set_dot(x, y, marker):
    if not is_free(y, x):
        print("Position is already occupied")
        return False
    field[y][x] = marker
    return True


def install_dot(marker):
    '''
    Check if position is free, if True:
        install dot in choosen position.
    :param marker: set a marker param you want to display
    :return:
    '''
    while True:
        x, y = take_input()
        x = make_dict()[x]
        if not set_dot(x, y, marker):
            continue
        create_path(y, x)
        print("After create_path")
        return field


def take_input():
    '''
    Takes x and y params from user
    :return:
    '''
    input_y = int(input("y?")) - 1
    input_x = input("x?").upper()
    return input_x, input_y

# Test commit

field[2][1] = 1
field[3][1] = 1
field[1][2] = 1
print(output_field(field))
while True:
    output_field(install_dot(1))
