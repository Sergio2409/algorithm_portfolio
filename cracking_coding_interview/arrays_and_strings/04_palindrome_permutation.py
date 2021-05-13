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
# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

# O(N)
import unittest
from collections import Counter


def letter_counter(some_string):
    ret_dict = {}
    for char in some_string:
        if ret_dict.get(char, False):
            ret_dict[char] = ret_dict[char] + 1
        else:
            if char != ' ':
                ret_dict[char] = 1
    return ret_dict


def is_odd(number):
    return not number % 2 == 0


def is_palindrome_permutation(phrase):
    phrase = phrase.lower()
    phrase_dict = letter_counter(phrase)
    not_even_count = 0
    for key in phrase_dict:
        if is_odd(phrase_dict[key]):
            not_even_count += 1
    return not_even_count <= 1


def is_palindrome_permutation_pythonic(phrase):
    """function checks if a string is a permutation of a palindrome or not"""
    counter = Counter(phrase.replace(" ", "").lower())
    return sum(val % 2 for val in counter.values()) <= 1


class Test(unittest.TestCase):
    test_cases = [
        ("aba", True),
        ("aab", True),
        ("abba", True),
        ("aabb", True),
        ("a-bba", True),
        ("Tact Coa", True),
        ("jhsabckuj ahjsbckj", True),
        ("Able was I ere I saw Elba", True),
        ("So patient a nurse to nurse a patient so", False),
        ("Random Words", False),
        ("Not a Palindrome", False),
        ("no x in nixon", True),
        ("azAZ", True),
    ]
    testable_functions = [is_palindrome_permutation,
                          is_palindrome_permutation_pythonic]

    def test_pal_perm(self):
        for f in self.testable_functions:
            for [test_string, expected] in self.test_cases:
                assert f(test_string) == expected


if __name__ == "__main__":
    unittest.main()
