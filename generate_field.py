'''
What it do:
1. Generates the field. So far it filled up with symbols "0".
2. change_field function defined, by changing it you can reassign values that
will be printed in final.
(it will be useful for taking input from user, or view visual changes)
3. Generate a list, to numerate a columns in alphabetical.
4. Generate a list, to numerate a rows in digital.


Tips for future:
- can to add set_defaults function to put there symbols that will fill field,
maybe var with dimension of field
'''
import string
FIELD_WIDTH = 10
FIELD_HEIGHT = 10


def generate_field(x=FIELD_WIDTH, y=FIELD_HEIGHT):
    '''Generate field
    '''
    return [[0 for _i in range(x)] for _j in range(y)]


def create_list_alphabet():
    '''Creates a list of letter in alphabetical.'''
    return list(string.ascii_uppercase)


def generate_dig_list(x=FIELD_HEIGHT):
    '''Generate list'''
    return list(range(1, x + 1))
