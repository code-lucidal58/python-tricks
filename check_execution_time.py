'''
timeit module allows user to measure the execution time of small Python code snippets
the number parameter is a multiplying factor of the resultant execution time for the given statement
'''

import timeit

print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))
print(timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000))
print(timeit.timeit('"-".join(map(str, range(100)))', number=10000))
