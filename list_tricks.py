"""
List slicing
"""

# clear all elements from a list:
lst = [1, 2, 3, 4, 5]
del lst[:]
print(lst)  # []

# replace all elements of a list
a = lst
lst[:] = [7, 8, 9]
print(lst)  # [7, 8, 9]
print(a)  # [7, 8, 9]
print(a is lst)  # True

# create a (shallow) copy of a list:
b = lst[:]
print(b)  # [7, 8, 9]
print(b is lst)  # False

'''
List comprehension
'''
even_squares = [x * x for x in range(10) if not x % 2]
print(even_squares)  # [0, 4, 16, 36, 64]

"""
ways of checking if all items in a list are equal:
"""

lst1 = ['a', 'a', 'a']

# Most efficient
print(len(set(lst)) == 1)
print(all(x == lst[0] for x in lst))
print(lst.count(lst[0]) == len(lst))
# Least efficient

# constructing a set is less efficient memory and speed-wise
