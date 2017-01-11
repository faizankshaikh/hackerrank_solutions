__author__ = "jalfaizy"

# code for https://www.hackerrank.com/challenges/handshake

#!/bin/python

import sys


T = int(raw_input().strip())
for a0 in xrange(T):
    N = int(raw_input().strip())
    ans = (N*(N - 1))/2
    print ans
