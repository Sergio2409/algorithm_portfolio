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
# Is Unique: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

import time
import unittest
from collections import defaultdict


def is_unique_chars(some_string):
    """
    Ex: 1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. 
    What if you cannot use additional data structures?
    """
    existant = {}
    for char in some_string:
        if len(some_string) > 128:
            return False
        if existant.get(char, False):
            return False
        else:
            existant[char] = char
    return True


def is_unique_chars_pythonic(string):
    return len(set(string)) == len(string)


class Test(unittest.TestCase):
    test_cases = [
        ("abcd", True),
        ("s4fad", True),
        ("", True),
        ("23ds2", False),
        ("hb 627jh=j ()", False),
        ("".join([chr(val) for val in range(128)]), True),  # unique 128 chars
        # non-unique 129 chars
        ("".join([chr(val // 2) for val in range(129)]), False),
    ]
    test_functions = [
        is_unique_chars_pythonic,
        is_unique_chars
    ]

    def test_is_unique_chars(self):
        num_runs = 1000
        function_runtimes = defaultdict(float)

        for _ in range(num_runs):
            for text, expected in self.test_cases:
                for is_unique_chars in self.test_functions:
                    start = time.perf_counter()
                    assert (
                        is_unique_chars(text) == expected
                    ), f"{is_unique_chars.__name__} failed for value: {text}"
                    function_runtimes[is_unique_chars.__name__] += (
                        time.perf_counter() - start
                    ) * 1000

        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name}: {runtime:.1f}ms")


if __name__ == "__main__":
    unittest.main()
