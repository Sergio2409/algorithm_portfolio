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
# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.

# O(N)
import time
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


def check_replacement(s1, s2):
    found_diff = False
    for pos in range(len(s1)):
        if s1[pos] != s2[pos]:
            if found_diff:
                return False
            else:
                found_diff = True
    return True

# aple apple
# ale  elas


def check_insert_remove(s1, s2):
    index1 = 0
    index2 = 0
    while index2 < len(s2) and index1 < len(s1):
        if s1[index1] != s2[index2]:
            if (index1 != index2):
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True


def check_one_way(s1, s2):
    """Check if a string can converted to another string with a single edit"""
    def min_len_fst(s1, s2): return (s2, s1) if len(s1) > len(s2) else (s1, s2)
    if len(s1) == len(s2):
        return check_replacement(s1, s2)
    elif abs(len(s1)-len(s2)) == 1:
        return check_insert_remove(*min_len_fst(s1, s2))
    else:
        return False


class Test(unittest.TestCase):
    test_cases = [
        # no changes
        ("pale", "pale", True),
        ("", "", True),
        # one insert
        ("pale", "ple", True),
        ("ple", "pale", True),
        ("pales", "pale", True),
        ("ples", "pales", True),
        ("pale", "pkle", True),
        ("paleabc", "pleabc", True),
        ("", "d", True),
        ("d", "de", True),
        # one replace
        ("pale", "bale", True),
        ("a", "b", True),
        ("pale", "ble", False),
        # multiple replace
        ("pale", "bake", False),
        # insert and replace
        ("pale", "pse", False),
        ("pale", "pas", False),
        ("pas", "pale", False),
        ("pkle", "pable", False),
        ("pal", "palks", False),
        ("palks", "pal", False),
        # permutation with insert shouldn't match
        ("ale", "elas", False),
    ]

    testable_functions = [check_one_way]

    def test_one_away(self):

        for f in self.testable_functions:
            start = time.perf_counter()
            for _ in range(100):
                for [text_a, text_b, expected] in self.test_cases:
                    assert f(text_a, text_b) == expected
            duration = time.perf_counter() - start
            print(f"{f.__name__} {duration * 1000:.1f}ms")


if __name__ == "__main__":
    unittest.main()
