import datetime

"""
In-place value swapping
"""
# swapping the values of a and b
a = 23
b = 42

# The "classic" way to do it with a temporary variable:
tmp = a
a = b
b = tmp

# Python also lets us use this
a, b = b, a

"""
When To Use __repr__ vs __str__?
"""
# Emulate what the std lib does:hand

today = datetime.date.today()

# Result of __str__ should be readable:
print(str(today))

# Result of __repr__ should be unambiguous:
print(repr(today))

# Python interpreter sessions use__repr__ to inspect objects:
print(today)
