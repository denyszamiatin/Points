'''
What it do:
1. Generates the field. So far it filled up with symbols "0".
2. change_field function defined, by changing it you can reassign values that will be printed in final.
(it will be useful for taking input from user, or view visual changes)
3. Generate a list, to numerate a columns in alphabetical.
4. Generate a list, to numerate a rows in digital.

Tips for future:
- can to add set_defualts function to put there symbols that will fill field, maybe var with dimension of field'''


def generate_field(x=10, y=10):
    '''Generate field
    at the moment it have const parameters,
    x = 10 (elements in nested list)
    y = 10 (element in list)
    but it could be easily changed just by typing var in function'''
    field = [[0 for i in range(x)] for j in range(y)]
    return field


def change_field(l):
    '''Function for making changes in field.
    It's created for future development. For now it's doing nothing.
    It just take the list and return it back without changes'''
    return l


def create_list_alphabet():
    '''Creates a list of letter in alphabetical.'''
    l = [chr(i) for i in range(65, 90)]
    return l


def generate_dig_list(x = 10):
    '''Generate list'''
    l = [i for i in range(1, x + 1)]
    return l

