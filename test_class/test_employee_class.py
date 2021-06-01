#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 11:23
# @Author  : Puxf
# @Site    : 
# @File    : test_employee_class.py
# @Software: PyCharm

import unittest
from test_class_demo import Employee
class TestEmployee(unittest.TestCase):
    """针对Employee的测试"""

    def test_give_default_raise(self):

        demo = Employee('pu','xi',2000)
        a = demo.give_raise()
        self.assertEqual(a,7000)

unittest.main()


