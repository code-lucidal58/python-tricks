# Using namedtuple is way shorter than defining a class manually
import contextlib
from collections import namedtuple

Car = namedtuple('Car', 'color mileage')

# "Car" class works as expected
my_car = Car('red', 3812.4)
print("My car's color is", my_car.color)
print("My car's mileage is", my_car.mileage)

# We get a nice string repr for free:
print("My car has the following properties:", my_car)

# Like tuples, namedtuples are immutable
with contextlib.suppress(AttributeError):
    my_car.color = 'blue'
print(my_car.color)
