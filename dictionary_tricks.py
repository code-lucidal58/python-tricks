# merging two dictionaries

x = {"a": 1, "b": 2, "c": 3}
y = {"d": 4, "e": 5}
z = {**x, **y}
print("The merged dictionary is", z)

# sorting python dict by value
# order of dictionary cannot be fixed
# hence sorting is done using dictionary values and converted to a list where each item is a tuple
xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
xs = sorted(xs.items(), key=lambda p: p[1])  # xs is now a list where each dictionary entry is a tuple
print("Sorted dictionary values using lambda", xs)

# OR
import operator

xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
xs = sorted(xs.items(), key=operator.itemgetter(1))
print("Sorted dictionary values using operator.itemgetter", xs)

# The get() method on dictionaries checks if the key exists. If exists, return the value else return default given

name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}


def greeting(userid):
    print("Hi %s!" % name_for_userid.get(userid, "there"))


greeting(382)
greeting(333333)
