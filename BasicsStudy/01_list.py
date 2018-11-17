# coding: utf-8
"""列表的相关操作"""

"""索引"""
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
# dayEnding为天数1-31对应的结尾
dayEndig = ['st', 'nd', 'rd'] + 17 * ['th'] + ['st', 'nd', 'rd'] + 7 * ['th'] + ['st']
year = input("Enter year:")
month = input("Enter month(1-12):")
day = input("Enter day(1-31):")
# int()由于input输出的值为str，故需int()强制转化为int类型
month_Name = months[int(month)-1]
day_Name = day + dayEndig[int(day)-1]
print(month_Name + ' ' + day_Name + ',' + year)

"""切片"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[::2])
# 结果为：[1, 3, 5, 7, 9]
print(numbers[8: 4: -1])
# 结果为：[9, 8, 7, 6]
print(numbers[1:6:3])
# 结果为：[2, 5]
print(numbers[1: 5])
# 结果：[2, 3, 4, 5]
print(numbers[1: -5])
# 结果：[2, 3, 4, 5]
print(numbers[-3: -1])
# 结果：[8, 9]
print(numbers[: 4])  # 切片第一个索引为序列的开头，故可省略
# 结果：[1, 2, 3, 4]
print(numbers[6:])   # 切片第二个索引为序列的结题，故可省略
# 结果：[7, 8, 9, 10]

"""相加相乘"""
print('hello,' + 'world!')
# 结果：hello,world!
print([1, 2, 3] + [4, 5, 6])
# 结果：[1, 2, 3, 4, 5, 6]
print('abc' * 2)
# 结果：abcabc
print([1, 2, 3] * 2)
# 结果：[1, 2, 3, 1, 2, 3]

"""成员资格"""
database = [
    ['Jemmy', '1234'],
    ['Cat', '1256'],
    ['Merry', '2578']
]
userName = input('Enter User Name:')
pin = input('Enter pin：')
if [userName, pin] in database:
    print("Success")
else:
    print("Fail")

"""长度、最小值、最大值"""
numbers = [1, 20, 10, 450, 25]
print(len(numbers))
# 结果：5
print(min(numbers))
# 结果：1
print(max(numbers))
# 结果：450

"""列表与字符串之间的转换"""
str = "hello"
str_list = list(str)
print(str_list)
# 结果： ['h', 'e', 'l', 'l', 'o']
list_str = ''.join(str_list)
print(list_str)
# 结果： hello

"""修改列表：重新赋值、删除元素"""
list1 = [1, 2, 4, 4, 5]
list1[2] = 3
print(list1)
# 结果：[1, 2, 3, 4, 5]
del list1[1]
print(list1)
# 结果：[1, 3, 4, 5]

"""给切片赋值"""
list2 = ['a', 'b', 'c', 'd', 'e']
list2[2:] = list('xy')
print(list2)
# 结果：['a', 'b', 'x', 'y']
list2[2:2] = ['c', 'd', 'e']    # 不替换原有元素的情况下插入新元素
print(list2)
# 结果：['a', 'b', 'c', 'd', 'e', 'x', 'y']
list2[5:] = []  # 替换一个空切片，即相当于删除
print(list2)
# 结果：['a', 'b', 'c', 'd', 'e']


"""列表方法：增加append，删除clear"""
lists = [1, 2, 3]
lists.append(4)
print(lists)
# 结果：[1, 2, 3, 4]
lists.clear()
print(lists)
# 结果：[]

"""列表方法：copy"""
a = [1, 2, 3]
b = a
b[0] = 5
print("a=", a)
print("b=", b)  # 结果： a= [5, 2, 3] b= [5, 2, 3]
c = a.copy()
print("c=", c)  # 结果：
c[0] = 1
print("a=", a)
print("c=", c)  # 结果：a= [5, 2, 3] c= [1, 2, 3]

"""列表方法：extend"""
d = [1, 2, 3]
e = [4, 5, 6]
print(d + e)      # 结果：[1, 2, 3, 4, 5, 6]
print("d=", d)    # 结果：d= [1, 2, 3]
d.extend(e)
print("d=", d)    # 结果：d= [1, 2, 3, 4, 5, 6]

"""列表方法： count"""
list3 = ['a', 'b', 'c', 'a', 'd']
print(list3.count('a'))     # 结果：2

"""列表方法：index"""
print(list3.index('d'))     # 结果：4

"""列表方法：insert"""
list3.insert(1, 'e')
print(list3)    # 结果：['a', 'e', 'b', 'c', 'a', 'd']

"""列表方法：pop"""
list3.pop()
print(list3.pop(2))     # 结果：b
print(list3)        # 结果：['a', 'e', 'c', 'a']

"""列表方法：remove"""
print(list3.remove('a'))    # 结果：None
print(list3)        # 结果：['e', 'c', 'a']

"""列表方法：reverse，reversed"""
x = [1, 5, 2, 6, 3]
x.reverse()
print(x)    # 结果：[3, 6, 2, 5, 1]
y1 = list(reversed(x))
print(y1)   # 结果：[1, 5, 2, 6, 3]

"""列表方法：sort和sorted，默认按名称排序"""
x.sort()    # sort()方法不可赋值，因其返回的是空值，若需赋值可用sorted
print(x)    # 结果：[1, 2, 3, 5, 6]
y2 = sorted(x)
print(y2)    # 结果：[1, 2, 3, 5, 6]

"""列表方法：高级排序，通过元素长度排序"""
m = ['heel', 'aaaaa', 'bb', 'heea']
m.sort(key=len)
print(m)    # 结果：['bb', 'heel', 'heea', 'aaaaa']
m.sort(reverse=True)
print(m)    # 结果：['heel', 'heea', 'bb', 'aaaaa']
