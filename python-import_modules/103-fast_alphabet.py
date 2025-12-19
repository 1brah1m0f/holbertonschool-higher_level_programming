#!/usr/bin/python3
from functools import reduce
print(reduce(lambda a, b: a + b, map(chr, range(65, 91))))
