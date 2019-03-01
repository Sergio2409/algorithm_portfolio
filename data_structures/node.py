#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------
# Copyright (c) ░s░e░r░g░i░o░v░a░l░d░e░s░2░4░0░9░
# All rights reserved.
#
# This is free software; you can do what the LICENCE file allows you to.
#


class Node(object):

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    @property
    def has_next(self):
        '''Return True if the node has a next otherwise returns False.

        '''
        return True if self.next else False

    def __repr__(self):
        return str(self.value)
