"""
contextlib can be used to suppress exceptions selectively.
contextlib.suppress returns a context manager that suppresses any of the specified exceptions if they occur in the body
of the with statement and resumes execution
"""
import contextlib
import os

with contextlib.suppress(FileNotFoundError):
    os.remove('somefile.tmp')

# This is equivalent to:

try:
    os.remove('somefile.tmp')
except FileNotFoundError:
    pass

