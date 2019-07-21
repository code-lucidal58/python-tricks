"""
`for` and `while` loops support an `else` clause that executes only if the loops terminates without hitting a `break`
statement
"""
import contextlib


def contains(haystack, needle):
    # Throw a ValueError if `needle` not in `haystack`.

    for item in haystack:
        if item == needle:
            break
    else:
        # The part is executed only if the loop ran to completion without hitting a `break` statement.
        raise ValueError('Needle not found')


contains([23, 'needle', 0xbadc0ffee], 'needle')
with contextlib.suppress(ValueError):
    contains([23, 42, 0xbadc0ffee], 'needle')


# Another way to do the above task
# METHOD 1
def better_contains(haystack, needle):
    for item in haystack:
        if item == needle:
            return
    raise ValueError('Needle not found')


# METHOD 2  -> Better
haystack = [23, 'needle', 0xbadc0ffee]
if "needle" not in haystack:
    raise ValueError('Needle not found')
