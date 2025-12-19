#!/usr/bin/python3
from functools import reduce; import sys
sys.stdout.write(reduce(lambda a, b: a + b, map(chr, range(65, 91))) + chr(10))
