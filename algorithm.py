#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------
# Copyright (c) ░s░e░r░g░i░o░v░a░l░d░e░s░2░4░0░9░
# All rights reserved.
#
# This is free software; you can do what the LICENCE file allows you to.
#
"""
Module description goes here

"""


class Algorithm(object):
    """
    Base class for all algorithms to be implemented.

    """
    @property
    def best_case(self):
        """
        Returns the algorithm complexity for the best case scenario.
        :return:

        """
        pass

    @property
    def average_case(self):
        """
        Returns the algorithm complexity for the average case scenario.

        :return:
        """
        pass

    @property
    def worst_case(self):
        """
        Returns the algorithm complexity for the worst case scenario.
        :return:
        """
        pass
