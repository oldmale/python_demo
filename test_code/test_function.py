#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 09:39
# @Author  : Puxf
# @Site    : 
# @File    : test_function.py
# @Software: PyCharm

import unittest

from name_function import get_formatted_name
class NamesTestCase(unittest.TestCase):
    """测试name_function。py"""

    def test_first_last_name(self):
        """能够正确处理像Janis,Joplin这样的姓名吗"""
        formatted = get_formatted_name('janis','joplin')
        self.assertEqual(formatted,'Janis Joplin')


unittest.main



