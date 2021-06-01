#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 10:23
# @Author  : Puxf
# @Site    : 
# @File    : test_cities.py
# @Software: PyCharm

import unittest
from city_functions import get_city_state

class CityStateTestCase(unittest.TestCase):
    """测试get_city_state.py"""

    def test_city_state(self):
        formatted_citystate = get_city_state('santiago','chile')
        self.assertEqual(formatted_citystate,'Santiago,Chile')

    def test_city_state_population(self):
        formatted_citystate = get_city_state('santiago','chile')
        self.assertEqual(formatted_citystate,'Santiago,Chile-population')

unittest.main