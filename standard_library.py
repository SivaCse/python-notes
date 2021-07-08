'''Misc examples from the Standard Library'''


# https://docs.python.org/3/library/index.html


# threading.Timer()
# -----------------------------------------------------------------------------

from threading import Timer

def do_something():
    print('doing something...')

t = Timer(10.0, do_something)
t.start()
# will print 'doing something...' after 10 seconds. The rest of the code will
# have time to run first.


# string
# -----------------------------------------------------------------------------

import string

print(string.ascii_letters)
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase)
# abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase)
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)
# 0123456789
print(string.hexdigits)
# 0123456789abcdefABCDEF
print(string.octdigits)
# 01234567
print(string.punctuation)
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(string.whitespace)
#  \t\n\r\x0b\x0c
print(string.printable)
# all of the above

# For example, here I'm using string.digits to clean up a string:
device_name = 'invchg123'
device_type = device_name.rstrip(string.digits)
print(device_type)
# invchg


# string.capwords()
# -----------------------------------------------------------------------------
# capwords() from the string library does a better job of capitalizing:

from string import capwords

example = "I'm super fun."

print(example.title())    # I'M Super Fun.
print(capwords(example))  # I'm Super Fun.


# random.choice()
# -----------------------------------------------------------------------------

import random
import string

def random_string(n):
    '''Produces a string of 'n' random ascii letters and digits'''
    s = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
    return ''.join(s)

test = random_string(20)
print(test)
# 40Sfk7NFmRjecSSezU9M

# random.choice() takes any sequence. In python, a sequence is and orderd set
# like a list, tuple or string. If you wanted to get a random item from another
# data type like a dictionary, simply convert it to a list. For example:

colors = {
  'aliceblue': '#f0f8ff',
  'antiquewhite': '#faebd7',
  'aqua': '#00ffff'
}

name, hex = random.choice(list(colors.items()))

print(name, hex)


# random.random()
# -----------------------------------------------------------------------------
# Gives you a random float between 0 and 1

random_zero_to_one = random.random()
print(f'random.random() gave me: {random_zero_to_one}')


# random.randbytes()
# -----------------------------------------------------------------------------
# Gives you a random number of bytes

rb = random.randbytes(4)

print(rb)
# b'=k\xbf4'


# secrets
# -----------------------------------------------------------------------------
# The secrets module is used for generating cryptographically strong random
# numbers suitable for managing data such as passwords, account authentication,
# security tokens, and related secrets. In particular, secrets should be used
# in preference to the default pseudo-random number generator in the random
# module, which is designed for modelling and simulation, not security or
# cryptography.

# https://docs.python.org/3/library/secrets.html


# collections.Counter()
# -----------------------------------------------------------------------------

from collections import Counter

jellybeans = ['red', 'red', 'orange', 'red', 'green', 'green']
jb_counter = Counter(jellybeans)

print(jb_counter)
# Counter({'red': 3, 'green': 2, 'orange': 1})

# most_common() returns all elements in descending order or just the top
# count if optional value passed in:

print(jb_counter.most_common(1))
# [('red', 3)]

# combine, find difference and find intersection of counters using +, -, &

jellybeans1 = ['red', 'red', 'orange', 'red', 'green', 'green']
jellybeans2 = ['black', 'red', 'yellow', 'yellow']

jb_counter1 = Counter(jellybeans1)
jb_counter2 = Counter(jellybeans2)

print(type(jb_counter1))
# <class 'collections.Counter'>

print(jb_counter1 + jb_counter2)
# Counter({'red': 4, 'green': 2, 'yellow': 2, 'orange': 1, 'black': 1})

print(jb_counter1 - jb_counter2)
# Counter({'red': 2, 'green': 2, 'orange': 1})

print(jb_counter2 - jb_counter1)
# Counter({'yellow': 2, 'black': 1})

print(jb_counter1 & jb_counter2)
# Counter({'red': 1})


# itertools
# -----------------------------------------------------------------------------
# itertools are special purpose iterator functions. Each returns one item at
# a time when called within a for loop and remembers its state between calls.

import itertools

# chain() – runs through its arguments as if they were a single iterable

for item in itertools.chain([1, 2], ['a', 'b']):
    print(item)
    # 1, 2, a, b

# cycle() – is an infinite iterator, cycling through its arguments forever:

# for item in itertools.cycle([1, 2]):
#     print(item)

# accumulate() – calculates accumulated values. By default, the sum:

for item in itertools.accumulate([1, 2, 3, 4]):
    print(item)
    # 1, 3, 6, 10

# you can provide a function as a second argument to accumulate().
# this will be used instead of addition. The function should take two
# arguments and return a single result.

def multiply(a, b):
    return a * b

for item in itertools.accumulate([1, 2, 3, 4], multiply):
    print(item)
    # 1, 2, 6, 24


# os.system()
# -----------------------------------------------------------------------------
# os.system is a simple way to run a shell command, for example to following
# will print the contents of the current directory:

import os

os.system('ls -alh')


# os.walk()
# -----------------------------------------------------------------------------
# os.walk recursively visits each directory from the root, and for each one,
# returns a tuple. The first item in the tuple is a string containing the
# current directory (path). Next is a list of all the directories in the
# current directory (directories). The last item in the tuple is a list
# containing all the file names (files). Note: os.walk is a generator. If you
# add an input to pause the loop, you can get a sense of how its drilling down
# and through the root directory.

import os

# Put the directory path here:
root = 'data/music'

# for path, directories, files in os.walk(root, topdown=True):
#     print(path)
#     print(directories)
#     for f in files:
#         print('\t', f)

# Use split() and splittext() to strip out the information you want.
# split() breaks a string into a tuple, splitext() will remove file extensions

for path, directories, files in os.walk(root, topdown=True):
    if files:
        print(path)                        # <--path is a string
        # data/music/Beatles/Sgt. Pepper's Lonely Hearts Club Band
        first_split = os.path.split(path)
        print(first_split)                 # <--first_split is a tuple
        # ('data/music/Beatles', "Sgt. Pepper's Lonely Hearts Club Band")
        print(first_split[1])              # <--contains the album name
        # Sgt. Pepper's Lonely Hearts Club Band
        second_split = os.path.split(first_split[0])
        print(second_split)                # <--second_split is a tuple
        # ('data/music', 'Beatles')
        print(second_split[1])             # <--contains the artist name
        # Beatles

        for f in files:                    # <--f is a string, files is a list
            f = os.path.splitext(f)        # f is now a tuple
            print(f)
            # ('13 - A Day In The Life', '.emp3')
            f = f[0].split(' - ')          # f is now a list
            print(f)
            # ['13', 'A Day In The Life']
        print('-' * 50)

# Using this you could easily create a database or structured file format,
# pulling out the specific bits of information.


# difflib
# -----------------------------------------------------------------------------
# the difflib module contains tools for comparing and working with differences
# between sequences. It's especially useful for comparing text. This example
# uses the SequenceMatcher class and its .ratio() method:

from difflib import SequenceMatcher

test = SequenceMatcher(None, 'rain', 'rainn')
print(type(test))
# <class 'difflib.SequenceMatcher'>
print(test.ratio())
# 0.8888888888888888

test = SequenceMatcher(None, 'rain', 'Rainn')
print(test.ratio())
# 0.6666666666666666

test = SequenceMatcher(None, ' rain', 'r a i n n ')
print(test.ratio())
# 5333333333333333

# The ratio method returns the similarity between two strings on a scale of 0–1.
# Note, it is case sensitive. Extra characters such as spaces and '\n' also
# count. The None argument is where you can specify which characters should be
# ignored (junk).

from difflib import get_close_matches

# get_close_matches(word, possibilities, n=3, cutoff=0.6)
#    - Use SequenceMatcher to return list of the best "good enough" matches.
#    - word is the sequence your trying to match (typically a string).
#    - possibilities is a list of sequences to match word against
#      (typically a list of strings).
#    - Optional arg n (default 3) is the maximum number of close matches to
#      return. n must be > 0.
#    - Optional arg ration cutoff (default 0.6) is a float in [0, 1].
#      Possibilities that don't score at least that similar to word are ignored

possibilities = ['train', 'car', 'grain', 'moose', 'rain', 'ball']

print(get_close_matches('rainn', possibilities))
# ['rain', 'train', 'grain']
print(get_close_matches('rainn', possibilities, n=1))
# ['rain']


# operator.itemgetter()
# -----------------------------------------------------------------------------
# This method allows us to sort lists of dictionaries or tuples by something
# other than their first value. For example:

from operator import itemgetter
from pprint import pprint

l = [('bob', 50), ('mary', 45), ('rick', 72), ('jane', 28)]

l.sort(key=itemgetter(1))

print(l)
# [('jane', 28), ('mary', 45), ('bob', 50), ('rick', 72)]

l = [{'id': 6, 'username': 'bob', 'email': 'bob@email.com'},
     {'id': 1, 'username': 'zed', 'email': 'zed@email.com'},
     {'id': 4, 'username': 'jane', 'email': 'jane@email.com'}]

l.sort(key=itemgetter('username'), reverse=True)

pprint(l)
# [{'email': 'zed@email.com', 'id': 1, 'username': 'zed'},
#  {'email': 'jane@email.com', 'id': 4, 'username': 'jane'},
#  {'email': 'bob@email.com', 'id': 6, 'username': 'bob'}]


# sys.argv
# -----------------------------------------------------------------------------
# This variable is a list of all the arguments passed in the command line.
# The first item will be the filename invoked with python, for example:

# $ python3 standard_library.py

import sys

print(f'sys.argv is {sys.argv}')

# Any additional variables passed in the command line can be accessed using
# list index syntax. For example:

# $ python3 standard_library.py hello

print(f'sys.argv[1] is {sys.argv[1]} and is {type(sys.argv[1])}')
# sys.argv[1] is hello and is <class 'str'>


# zoneinfo
# -----------------------------------------------------------------------------
# This module was added in Python 3.9. The zoneinfo module brings support for
# the IANA time zone database to the standard library. It adds
# zoneinfo.ZoneInfo, a concrete datetime.tzinfo implementation backed by the
# system’s time zone data.

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

# Daylight Savings
dt = datetime(2021, 10, 31, 12, tzinfo=ZoneInfo('America/Vancouver'))

print(dt)
# 2021-10-31 12:00:00-07:00
print(dt.tzname())
# 'PDT'

# Standard time
dt += timedelta(days=7)

print(dt)
# 2020-11-07 12:00:00-08:00
print(dt.tzname())
# PST

# https://www.python.org/dev/peps/pep-0615/
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones


# graphlib
# -----------------------------------------------------------------------------
# This module was added in Python 3.9. This new module, graphlib contains the
# graphlib.TopologicalSorter class to offer functionality to perform topological
# sorting of graphs.

# https://docs.python.org/3/library/graphlib.html#module-graphlib
