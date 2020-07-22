#!/usr/bin/env python3

import sys

count = 257 if len(sys.argv) < 2 else int(sys.argv[1])

with open('too_many_functions.acs', 'w') as f:
    for i in range(count):
        print('function void f%i(void) {}' % i, file=f)

    print('\nscript 1 enter\n{', file=f)

    for i in range(count):
        print('  f%i();' % i, file=f)

    print('}', file=f)
