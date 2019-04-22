'''
List slicing
'''

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
