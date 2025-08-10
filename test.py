import math, timeit

print(timeit.timeit('a ** 0.5', globals={'a': 123456789}, number=100_000_000), "seconds")
print(timeit.timeit('math.sqrt(a)', globals={'a': 123456789, 'math': math}, number=100_000_000), "seconds")