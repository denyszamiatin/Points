'''
TODO value check in install_dot
TODO same_dots list should to be relocated. to refresh correctly
make doc test
'''
import string
from generate_field import generate_field
from display_field import output_field

field = generate_field()


def make_dict():
    '''
    Create a dictionary with numerate letters.
    Using for translation letters into digits
    :return:
    '''
    key = list(string.ascii_uppercase)
    value = [i for i in range(0, 25)]
    dict = {}
    for i, j in zip(key, value):
        dict[i] = j
    return dict


def check_position(x, y):
    l = field
    if l[y][dict[x]] != 0:
        print("Position already occupied")


def check_around(y, x):
    '''
    Check position for similar marker in position around,
    if marker the same = append position to the same_dots list
    :param x:
    :param y:
    :return:
    '''
    list_yx = [[0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1]]
    marker = 1
    same_dots = []
    for i in list_yx:
        if field[y + i[0]][x + i[1]] == marker:
            same_dots.append([y + i[0], x + i[1]])
    return same_dots

def create_path(y, x, path = [], a = 0, b = 0):
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
    if [y, x] in path:
        print(path)
        print("Closed!")
        return path
    dots_around = check_around(y, x)
    if [a, b] in dots_around:
        dots_around.remove([a, b])
    a, b = y, x
    if dots_around != []:
        path.append([y, x])
        for i in dots_around:
            create_path(i[0], i[1], path, a, b)
    elif dots_around == []:
        print("There is no dots around.")
        path.clear()
    else:
        print("You SHALL NOT PASS!!!")



def install_dot(marker):
    '''
    Check if position is free, if True:
        install dot in choosen position.
    :param marker: set a marker param you want to display
    :return:
    '''
    l = field
    dict = make_dict()
    while True:
        x, y = take_input()
        x = dict[x]
        if l[y][x] != 0:
            print("Position is already occupied")
            continue
        else:
            l[y][x] = marker
        create_path(y, x)
        print("After create_path")
        return l


def take_input():
    '''
    Takes x and y params from user
    :return:
    '''
    input_y = int(input("y?")) - 1
    input_x = input("x?").upper()
    return input_x, input_y


field[2][1] = 1
field[3][1] = 1
field[1][2] = 1
print(output_field(field))
while True:
    output_field(install_dot(1))
