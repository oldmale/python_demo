#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/28 13:33
# @Author  : Puxf
# @Site    : 
# @File    : try_except.py
# @Software: PyCharm

"""10-6 加法运算：提示用户提供数值输入时，常出现的一个问题是，用户提供的是
文本而不是数字。在这种情况下，当你尝试将输入转换为整数时，将引发 TypeError 异
常。编写一个程序，提示用户输入两个数字，再将它们相加并打印结果。在用户输入的
任何一个值不是数字时都捕获 TypeError 异常，并打印一条友好的错误消息。对你编写
的程序进行测试：先输入两个数字，再输入一些文本而不是数字。"""

# print('Give me two numbers, and I will add them.')
# first = input('\nFirst number: ')
# second = input('Second number: ')
# try:
#     first =int(first)
#     second = int(second)
# except ValueError:
#     print('it is text,please input numbers')
# else:
#     answer = first + second
#     print('result: '+str(answer))


# number1 = input('请输入一个数字：')
# number2 = input('请输入另一个数字：')
# try:
#     number1 = int(number1)
#     number2 = int(number2)
# except ValueError:
#     print('你不可以输入文本')
# else:
#     sums = number1 + number2
#     print(str(sums))


"""10-7 加法计算器：将你为完成练习 10-6 而编写的代码放在一个 while 循环中，让
用户犯错（输入的是文本而不是数字）后能够继续输入数字。"""

# while True:
#     input1 = input('请输入一个数：')
#     input2 = input('请输入一个数：')
#     try:
#         input1 = int(input1)
#         input2 = int(input2)
#     except ValueError:
#         print('\n对不起，你输入的不是数字')
#     else:
#         sums = input1 + input2
#         print(str(sums))


"""10-8 猫和狗：创建两个文件 cats.txt 和 dogs.txt，在第一个文件中至少存储三只猫的
名字，在第二个文件中至少存储三条狗的名字。编写一个程序，尝试读取这些文件，并
将其内容打印到屏幕上。将这些代码放在一个 try-except 代码块中，以便在文件不存
在时捕获 FileNotFound 错误，并打印一条友好的消息。将其中一个文件移到另一个地方，
并确认 except 代码块中的代码将正确地执行。"""

def get_file(filename):
    try:
        with open(filename) as f:
            counter = f.read()
            print(counter)
    except FileNotFoundError:
        # msg = '没有找到' + filename + '这个文件'
        # print(msg)
        pass

# filename = 'dogs.txt'
filename = 'cats.txt'
get_file(filename)