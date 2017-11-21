# f = open('record.txt','w')
# f.write('hello world')
# f = open('record.txt','r')
# contents = f.read()
# f.close()
# # x = open('record.txt','r')
# # contents = x.read()
# # x.close()
#
# print contents
#
# for line in open('record.txt'):
#      print line
# xl = [1, 3, 5]
# yl = [9, 12, 13]
# L = [x ** 2 for (x, y) in zip(xl, yl) if y > 10]
# print L

# def test_func():
#     try:
#         m = 1/0
#     except NameError:
#         print("Catch NameError in the sub-function")

# try:
#     test_func()
# except ZeroDivisionError:
#     print("Catch error in the main program")


# def f(x):
#     x = 100
#     print x
#
# a = 1
# f(a)
# print a

# import this
# import string
# def f(x):
#     x[0] = 100
#     print x
#
# a = [1,2,3]
# f(a)
# print a
# import logging
# logging.basicConfig(level=logging.INFO)
# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print (10 / n)


import requests
r = requests.get('https://www.douban.com')
print r.content

