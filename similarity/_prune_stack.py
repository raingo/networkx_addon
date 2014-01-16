#!/usr/bin/env python

"""
Python source code - replace this with a description of the code and write the code below this text.
"""

import operator
from collections import defaultdict

# prune the searching space
# top-K
def _prune_stack(d, K):

    sorted_d = sorted(d.iteritems(), key = operator.itemgetter(1))

    res = defaultdict(float)

    for key, value in sorted_d[-K:]:
        res[key] = value

    return res

def main():

    d = {'A':0.01, 'B':0.34, 'C':0.99, 'D':0.001, 'E':0.19}
    print _prune_stack(d, 2)

    d = {'A':0.01, 'B':0.34, 'C':0.99, 'D':0.001, 'E':0.19}
    print _prune_stack(d, 10)

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
