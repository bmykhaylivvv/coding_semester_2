'''
Module for getting all sublines which start from the first letter of the word.
'''

import itertools


def all_prefixes(line):
    '''
    Return all sublines which start from the first letter of given word.

    >>> len(all_prefixes('lead'))
    4
    '''
    all_prfxs = set()
    for length in range(1, len(line)+1):
        certaint_length_prefix = list(
            itertools.combinations(line.lower(), length))
        for permutation in certaint_length_prefix:
            if permutation[0] == line[0].lower() and ''.join(permutation) in line.lower():
                all_prfxs.add(''.join(permutation))
    return all_prfxs
