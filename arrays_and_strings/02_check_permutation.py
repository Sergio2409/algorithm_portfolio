#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------
# Copyright (c) ░s░e░r░g░i░o░v░a░l░d░e░s░2░4░0░9░
# All rights reserved.
#
# This is free software; you can do what the LICENCE file allows you to.
#

# Problem
#
# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.

import unittest
from collections import Counter


def str2dict(some_string):
    ret_dict = {}
    for char in some_string:
        if ret_dict.get(char, False):
            ret_dict[char] = ret_dict[char] + 1
        else:
            ret_dict[char] = 1
    return ret_dict


def check_permutations(str1, str2):
    if len(str1) != len(str2):
        return False

    str2_dict = str2dict(str2)
    for char in str1:
        if str2_dict.get(char, 0) > 0:
            str2_dict[char] -= 1
        else:
            return False
    return True


def check_permutation_pythonic(str1, str2):
    if len(str1) != len(str2):
        return False
    return Counter(str1) == Counter(str2)


check_permutation_by_count = check_permutations


class Test(unittest.TestCase):
    # str1, str2, is_permutation
    test_cases = (
        ("dog", "god", True),
        ("abcd", "bacd", True),
        ("3563476", "7334566", True),
        ("wef34f", "wffe34", True),
        ("dogx", "godz", False),
        ("abcd", "d2cba", False),
        ("2354", "1234", False),
        ("dcw4f", "dcw5f", False),
        ("DOG", "dog", False),
        ("dog ", "dog", False),
        ("aaab", "bbba", False),
    )

    testable_functions = [
        # check_permutation_by_sort,
        check_permutation_by_count,
        check_permutation_pythonic,
    ]

    def test_cp(self):
        # true check
        for check_permutation in self.testable_functions:
            for str1, str2, expected in self.test_cases:
                print('Str1: {0}, Str2: {1}, Expected: {2}'.format(
                    str1, str2, str(expected)))
                assert check_permutation(str1, str2) == expected


if __name__ == "__main__":
    unittest.main()
