#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 11:03
# @Author  : Puxf
# @Site    : 
# @File    : test_class_demo.py
# @Software: PyCharm

"""11-3 雇员：编写一个名为 Employee 的类，其方法__init__()接受名、姓和年薪，并
将它们都存储在属性中。编写一个名为 give_raise()的方法，它默认将年薪增加 5000
美元，但也能够接受其他的年薪增加量。
为 Employee 编写一个测试用例，其中包含两个测试方法：test_give_default_
raise()和 test_give_custom_raise()。使用方法 setUp()，以免在每个测试方法中都创
建新的雇员实例。运行这个测试用例，确认两个测试都通过了。"""



class Employee():
    """给用户增加年薪"""

    def __init__(self,frist,last,annual_salary):
        self.frist = frist
        self.last = last
        self.annual_salary = annual_salary

    def show_user_all(self):
        print('姓名：' + self.frist + self.last +' '+ '年薪：' + str(self.annual_salary))

    def give_raise(self,annual_salary=5000):
        # self.annual_salary += annual_salary
        # return self.annual_salary
        total = self.annual_salary + annual_salary
        print('你的年薪增加为：',total)




# demo = Employee('pu','xi',2000)
# demo.show_user_all()
# demo.give_raise(9000)


