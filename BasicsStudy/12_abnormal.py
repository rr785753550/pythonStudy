# coding: utf-8

# """异常"""
# # 使用try/except捕获异常
# x = int(input("Enter a number:"))
# y = int(input("Enter another number:"))
# try:
#     print(x / y)
# except ZeroDivisionError:
#     print("被除数为0")
#
#
# # 捕获异常时使用raise与不使用raise的区别
# class MuffledCalculator:
#     def __init__(self, muffled):
#         # muffled = False
#         self.muffled = muffled
#
#     def calc(self, x, y):
#         try:
#            print(x/y)
#         except ZeroDivisionError:
#             if self.muffled:
#                 print('Division by zero is illegal')
#             else:
#                 raise
# MuffledCalculator(muffled=True).calc(x=1, y=0)      # 结果：Division by zero is illegal
# MuffledCalculator(muffled=False).calc(x=1, y=0)     # 结果：报错，报错内容为ZeroDivisionError: division by zero
#
# # raise语句后自定义上下文
# try:
#     print(1/0)
# except ZeroDivisionError:
#     raise ValueError from None  # 结果：报错内容为ValueError
#
# # raise语句抛出通用异常类型(Exception)
# try:
#     print(1/0)
# except ZeroDivisionError:
#     raise Exception("抛出一个异常")       # 结果：Exception: 抛出一个异常
#
# # 自定义异常类型
# class SomeCustomException(Exception):
#     pass



# """捕获多个异常"""
# # except后跟有异常类型
# class div:
#     def division(self, x, y):
#         try:
#             print(x/y)
#         except ZeroDivisionError:
#             print("被除数为0")
#         except TypeError:
#             print("所传入的参数不是整型")
# div().division(1, 'a')      # 结果：所传入的参数不是整型
# div().division(1, 0)        # 结果：被除数为0
#
# class div1:
#     def division(self, x, y):
#         try:
#             print(x/y)
#         except (ZeroDivisionError, TypeError):
#             print("x或y的参数异常")
# div1().division(1, 'a')      # 结果：x或y的参数异常
# div1().division(1, 0)        # 结果：x或y的参数异常
#
# # 捕获到异常时记录下来，待程序结束后可查看日志以便分析异常原因
# class div2:
#     def division(self, x, y):
#         try:
#             print(x/y)
#         except (ZeroDivisionError, TypeError) as e:
#             print(e)
# div2().division(1, 'a')      # 结果：unsupported operand type(s) for /: 'int' and 'str'
# div2().division(1, 0)        # 结果：division by zero
#
# # except后不跟异常类型，即捕获所有异常错误
# class div3:
#     def division(self, x, y):
#         try:
#             print(x/y)
#         except:
#             print("x或y的参数异常")
# div3().division(1, 'a')      # 结果：x或y的参数异常
# div3().division(1, 0)        # 结果：x或y的参数异常
#
# # 捕获所有的异常对象
# class div4:
#     def division(self, x, y):
#         try:
#             print(x/y)
#         except Exception as e:
#             print(e)
# div4().division(1, 'a')      # 结果：unsupported operand type(s) for /: 'int' and 'str'
# div4().division(1, 0)        # 结果：division by zero



# """捕获异常后加else子句"""
# class div5:
#     def division(self, x, y):
#         try:
#             print(x/y)
#         except Exception as e:
#             print(e)
#         else:
#             print("运行结束")
# div5().division(1, 1)      # 结果：1.0 运行结束
# div5().division(1, 0)       # 结果：division by zero
#
# # 直到随机输出的值不会引发异常才会跳出死循环，否则会一直循环下去
# class div6:
#     def division(self):
#         while True:
#             x = input("Enter a number:")
#             y = input("Enter another number:")
#             try:
#                 print(int(x)/int(y))
#             except Exception as e:
#                 print(e)
#             else:
#                 break
# div6().division()



# """捕获异常后加finally子句"""
# class div7:
#     def division(self, x, y):
#         try:
#             print(x/y)
#         finally:
#             print("运行结束")
# div7().division(1, 1)      # 结果：1.0 运行结束
# div7().division(1, 0)       # 结果：运行结束 division by zero
#
# class div8:
#     def division(self, x, y):
#         try:
#             print(x/y)
#         except Exception as e:
#             print(e)
#         finally:
#             print("运行结束")
# div8().division(1, 1)      # 结果：1.0 运行结束
# div8().division(1, 0)       # 结果：division by zero 运行结束
#
# class div9:
#     def division(self, x, y):
#         try:
#             print(x/y)
#         except Exception as e:
#             print(e)
#         else:
#             print("else语句")
#         finally:
#             print("运行结束")
# div9().division(1, 1)      # 结果：1.0 else语句 运行结束
# div9().division(1, 0)       # 结果：division by zero 运行结束



"""警告"""
from warnings import warn
warn("it is not my expect direction!")
# 运行后会输出警告warn("it is not my expect direction!")

"""过滤警告"""
from warnings import filterwarnings
filterwarnings('ignore')
warn("filter warning")
# 运行后不再输出警告内容，而是被忽略，代表过滤filter warning的警告

from warnings import warn, filterwarnings
filterwarnings('error')
warn("this warning is error")
# 运行后会引发异常UserWarning
