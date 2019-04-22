# Merging two dictionaries

x = {"a": 1, "b": 2, "c": 3}
y = {"d": 4, "e": 5}
z = {**x, **y}
print("The merged dictionary is", z)
