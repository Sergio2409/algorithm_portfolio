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
# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)

# O(N)
import unittest


def urlify_algo(string, length):
    pos = len(string) - 1
    arr = [False] * len(string)
    result = ''
    i = length - 1
    while pos >= 0:
        if string[i] == ' ':
            arr[pos-2] = '%'
            arr[pos-1] = '2'
            arr[pos] = '0'
            pos -= 3
        else:
            arr[pos] = string[i]
            pos -= 1
        i -= 1
    return result.join(arr)


def urlify_pythonic(text, length):
    """solution using standard library"""
    return text.rstrip().replace(" ", "%20")


class Test(unittest.TestCase):
    """Test Cases"""

    test_cases = [
        #("much ado about nothing      ", "much%20ado%20about%20nothing"),
        ("much ado  ", "much%20ado"),
        #("Mr John Smith    ", "Mr%20John%20Smith"),
    ]
    testable_functions = [urlify_algo]

    def test_urlify(self):
        for urlify in self.testable_functions:
            for test_string, expected in self.test_cases:
                stripped_length = len(test_string.rstrip(" "))
                actual = urlify(test_string, stripped_length)
                assert actual == expected


if __name__ == "__main__":
    unittest.main()
