#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_case(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([3, 2, 4, 1]), 4)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-3, -2, -4, -1]), -1)
        self.assertEqual(max_integer([1000000, 2000000, 4000000, 1000000]), 4000000)
        self.assertEqual(max_integer([1, 2, 3, 4, 4.5]), 4.5)
        self.assertEqual(max_integer((1, 2, 3, 4)), 4)

    def test_types(self):
        self.assertRaises(TypeError, max_integer, [3, 2, 4, '1'])
        self.assertRaises(TypeError, max_integer, 1)
