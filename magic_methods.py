'''Special (Magic) Methods'''

# Names of these methods begin with __. An example is __init__ which initializes
# a newly created object from its class and any arguments that were passed in.
# Example: create a method that compares two words but is case insensitive.

class Word():
    def __init__(self, text):
        self.text = text
    def equals(self, word2):
        return self.text.lower() == word2.text.lower()

# testing:
first = Word('ha')
second = Word('HA')

print(first.equals(second))  # True

# __eq__
# The above works but there's an tidier way using Magic Methods:

class Word():
    def __init__(self, text):
        self.text = text
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()

first = Word('ha')
second = Word('HA')

print(first == second)  # True

# -----------------------------------------------------------------------------
# Magic Methods for comparison
# -----------------------------------------------------------------------------

def __eq__(self, other):        # self == other
    pass
def __ne__(self, other):        # self != other
    pass
def __lt__(self, other):        # self < other
    pass
def __gt__(self, other):        # self > other
    pass
def __le__(self, other):        # self <= other
    pass
def __ge__(self, other):        # self >= other
    pass

# -----------------------------------------------------------------------------
# Magic Methods for math
# -----------------------------------------------------------------------------

def __add__(self, other):       # self + other
    pass
def __sub__(self, other):       # self - other
    pass
def __mul__(self, other):       # self * other
    pass
def __floordiv__(self, other):  # self // other
    pass
def __truediv__(self, other):   # self / other
    pass
def __mod__(self, other):       # self % other
    pass
def __pow__(self, other):       # self ** other
    pass

# -----------------------------------------------------------------------------
# Other common Magic Methods
# -----------------------------------------------------------------------------

def __str__(self):
    pass
def __repr__(self):
    pass
def __len__(self):
    pass

# -----------------------------------------------------------------------------
# Testing __str__ and __repr__
# -----------------------------------------------------------------------------

print(repr(first))      # <__main__.Word object at 0x101ca8828>
print(first)            # <__main__.Word object at 0x101ca8828>

class Word():
    def __init__(self, text):
        self.text = text
    def __str__(self):
        return self.text
    def __repr__(self):
        return 'Word("' + self.text + '")'

first = Word('Ha')

print(first)            # Ha - because of the magic method __str__
print(repr(first))      # Word("Ha") - because of the magic method __repr__

# -----------------------------------------------------------------------------
# Another __str__ example
# -----------------------------------------------------------------------------

class Player(object):

    def __init__(self, name):
        self.name = name
        self.lives = 3
        self.level = 1
        self.score = 0

    def __str__(self):
        return ('Name: {0.name}, Lives: {0.lives}, Level: {0.level}, '
                'Score: {0.score}'.format(self))

player1 = Player('Morty')
print(player1)  # Name: Morty, Lives: 3, Level: 1, Score: 0

# -----------------------------------------------------------------------------
# __dict__
# -----------------------------------------------------------------------------

# Another magic method is __dict__. It's used to return the dictionary used to
# store an object’s attributes

print(player1.__dict__)  # {'name': 'Morty', 'lives': 3, 'level': 1, 'score': 0}
