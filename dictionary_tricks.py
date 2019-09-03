# merging two dictionaries

x = {"a": 1, "b": 2, "c": 3}
y = {"d": 4, "e": 5}
z = {**x, **y}
print("The merged dictionary is", z)

# sort a python dict by value
# order os dictionary cannot be fixed nut conserving the data type
# hence sorting is done using dictionary values and converted to a list where each item is a tuple
xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
xs = sorted(xs.items(), key=lambda p: p[1])  # xs is now a list where each dictionary entry is a tuple
print("Sorted dictionary values using lambda", xs)
# [('d', 1), ('c', 2), ('b', 3), ('a', 4)]

# OR
import operator

xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
xs = sorted(xs.items(), key=operator.itemgetter(1))
print("Sorted dictionary values using operator.itemgetter", xs)
# [('d', 1), ('c', 2), ('b', 3), ('a', 4)]
