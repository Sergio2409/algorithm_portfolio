#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------
# Copyright (c) ░s░e░r░g░i░o░v░a░l░d░e░s░2░4░0░9░
# All rights reserved.
#
# This is free software; you can do what the LICENCE file allows you to.
#
from .node import Node


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.last = None
        self.current = None
        self._size = 0

    @property
    def size(self):
        '''Return the current size of the list

        '''
        return self._size

    def is_empty(self):
        '''Return True if the list is empty otherwise return False.

        '''
        return True if self.size == 0 else False

    def get(self, index):
        '''Return the element at the index passed

        '''
        self._reset_current()
        if index < 0 or index > self.size:
            raise IndexError('Index passed does not exist!')
        pos = 0
        while pos < index:
            self.current = self.current.next
            pos += 1
        to_return = self.current
        self._reset_current()
        return to_return

    def add(self, value):
        '''Add an element to the end of the list

        '''
        node = Node(value)
        if self.size == 0:
            self.head = node
            self.last = node
            self.current = node
        else:
            self.last.next = node
            self.last = node
        self._size += 1

    def _reset_current(self):
        self.current = self.head

    def __iter__(self):
        self.current = self.head
        els = []
        while self.current.has_next:
            els.append(self.current)
            self.current = self.current.next
        els.append(self.current)  # add last element
        self._reset_current()
        return (x for x in els)

    def __str__(self):
        '''String representation of the list

        '''
        result = '['
        node = self.head
        while node.has_next:
            result += '{0},'.format(str(node.value))
            node = node.next
        return result + ']'
