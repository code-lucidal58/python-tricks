"""
This script contains all out of box features related to functions in Python
"""
import contextlib

'''Python 3.5+ supports 'type annotations' that can be used with tools like Mypy to write statically typed Python'''


def my_add(a: int, b: int) -> int:
    return a + b


'''The lambda keyword in Python provides a shortcut for declaring small and anonymous functions'''
add = lambda x, y: x + y
add(5, 3)

'''the above lambda function is the same as the below one'''


def add(x, y):
    return x + y


add(5, 3)

'''Lambdas are *function expressions*'''
(lambda x, y: x + y)(5, 3)

"""
• Lambda functions are single-expression functions that are not necessarily bound to a name (they can be anonymous).
• Lambda functions can't use regular Python statements and always include an implicit `return` statement.
"""


# Function argument unpacking

def myfunc(x, y, z):
    print(x, y, z)


tuple_vec = (1, 0, 1)
dict_vec = {'x': 1, 'y': 0, 'z': 1}

myfunc(*tuple_vec)

myfunc(**dict_vec)

"""
A bare "*" asterisk can be used in function parameter lists to force the caller to use keyword arguments for certain 
parameters:
"""


def hello(a, b, *, c='x', d='y', e='z'):
    print('Hello')


# To pass the value for c, d, and e, it has to be explicitly passed as "key=value" named arguments
with contextlib.suppress(TypeError):
    hello(1, 2, 'p', 'q', 'v')  # This will throw TypeError: hello() takes 2 positional arguments but 5 were given

hello(1, 2, c='p', d='q', e='v')
