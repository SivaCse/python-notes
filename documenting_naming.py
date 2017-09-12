# Documenting and Naming

# docstrings -----------------------------------------------------------------

# For obvious reasons, it helps to document your code. Documentation can
# include comments and docstrings, but it can also incorporate informative
# naming of variables, functions, modules, and classes. Don't be obsessive, say
# why you assigned the value. Point out why you called the variable whatever.

def example():
    '''A brief, clear description'''
    pass

# In larger or more complex projects however, it is often a good idea to give
# more information like, what it does, any exceptions it may raise, what it
# returns, or relevant details about the parameters, arguments, methods,
# variables or attributes . In multiline functions it's best to start with a
# single summary line, a space and then the rest of the information. For more
# detailed documentation of code a popular style is one often called Numpy
# style. While it can take up more lines, it allows the developer to include a
# more information about a method, function, class.

def example(arg1=0.0, arg2=None):
    '''
    Summary line.

    Extended description of function - The docstring should describe the function, class, or method in a way that is easy to understand.

    Parameters:
    arg1 (int) - Description of arg1, default 0.0
    arg2 (str) - Description of arg2, default None

    Returns:
    int - Description of return value
    '''
    pass

help(example)  # output all the docstrings (a class could have many)
print(example.__doc__)  # print just the one docstring

# Example --------------------------------------------------------------------

# if you were writing a Fahrenheit to Celsius converter:

def ftoc(f_temp):
    '''Convert Fahrenheit temperature <f_temp> to Celsius and return it.'''
    f_boil_temp = 212.0
    f_freeze_temp = 32.0
    c_boil_temp = 100.0
    c_freeze_temp = 0.0
    f_range = f_boil_temp - f_freeze_temp
    c_range = c_boil_temp - c_freeze_temp
    f_c_ratio = c_range / f_range
    c_temp = (f_temp - f_freeze_temp) * f_c_ratio + c_freeze_temp
    return c_temp

# And a little test code wouldn't hurt:

if __name__ == '__main__':
    for f_temp in [-40.0, 0.0, 32.0, 100.0, 212.0]:
        c_temp = ftoc(f_temp)
        print('%f F => %f C' % (f_temp, c_temp))

# Constants ------------------------------------------------------------------

# Python doesn't have constants, but the PEP8 stylesheet recommends using
# capital letters and underscores (e.g., ALL_CAPS) when naming variables that
# should be considered constants.

# Because we precompute values based on constant values, move them to the top
# level of the module. Then, they'll only be calculated once rather than in
# every call to the ftoc() function:

F_BOIL_TEMP = 212.0
F_FREEZE_TEMP = 32.0
C_BOIL_TEMP = 100.0
C_FREEZE_TEMP = 0.0
F_RANGE = F_BOIL_TEMP - F_FREEZE_TEMP
C_RANGE = C_BOIL_TEMP - C_FREEZE_TEMP
F_C_RATIO = C_RANGE / F_RANGE

def ftoc(f_temp):
    "Convert Fahrenheit temperature <f_temp> to Celsius and return it."
    c_temp = (f_temp - F_FREEZE_TEMP) * F_C_RATIO + C_FREEZE_TEMP
    return c_temp

# Private functions ----------------------------------------------------------

# If you're building a module that will be imported, you can identity functions
# that aren't intended to be called on their own by naming them with a leading
# underscore.

def _guts():
    pass

# Private attributes (name mangling) -----------------------------------------

# The naming convention for hidden attributes in classes is a leading double
# underscore. Python "mangles" the names of attributes that start with two
# underscores to make it more difficult to accidentally mess with it. The
# mangling is this: _Classname__attibutename

class Person():
    def __init__(self, name, alias):
        self.name = name       # public attribute
        self.__alias = alias   # private attribute

x = Person(name='Bob', alias='boktoktok')
print(x.name)
print(x.alias)   # AttributeError: 'Person' object has no attribute 'alias'
print(x.__alias)  # AttributeError: 'Person' object has no attribute '__alias'
print(x._Person__alias)  # This will actually return the attribute

# Throwaway values -----------------------------------------------------------

# in the event that you need to give something a name but you have no intention
# of using it, it's acceptable to use the name '-'. The perfect example of this
# is with tuple unpacking. In the example below, I don't want the age
# information, but I need to give it a name in order to unpack the rest:

person = ('Kali', '50', 'Peru')

name, _, country = person

print(name, country)

# Variables names using Python keywords --------------------------------------

# If you're desperate to name something using one of Pythons keywords, the
# accepted standard is to follow the with an underscore:

from_ = 'example'
