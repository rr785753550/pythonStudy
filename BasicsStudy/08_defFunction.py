"""自定义def函数"""


"""计算斐波那契数，那每个数都是前两个数的和"""
def fibs(num):
    # fibs为自定义函数的函数名，num为形参
    s = [0, 1]
    for i in range(num-2):
        s.append(s[-2] + s[-1])
    return s


n = 5
result = fibs(n)    # 调用函数fibs，n为传入的实参值
print(result)       # 结果：[0, 1, 1, 2, 3]
print(n)            # 结果：5
n = fibs(n)
print(n)            # 结果：[0, 1, 1, 2, 3]


"""修改列表中的值"""
def change(n):
    n[0] = "G"


names = ['A', 'B']
change(names)
print(names)    # 结果：['G', 'B']


"""使用关键字参数和位置参数调用"""
def hello(greeting, name):
    s = '{}, {}'.format(greeting, name)
    return s


# 使用关键字参数调用
s1 = hello(name="Mr zhang", greeting="hello")
print(s1)   # 结果：hello, Mr zhang
# 使用位置参数调用
s2 = hello("Mr zhang", "hello")
print(s2)   # 结果：Mr zhang, hello
s2 = hello("hello", "Mr zhang")
print(s2)   # 结果：hello, Mr zhang


"""def函数参数有默认值"""
def hello1(name, greeting='hello'):
    s = '{}, {}'.format(greeting, name)
    return s


print(hello1(name="zhang"))                 # 结果：hello, zhang
print(hello1(name="zhang", greeting="Hi"))  # 结果：Hi, zhang


def hello2(name="zhang", greeting="hello"):
    s = '{}, {}'.format(greeting, name)
    return s


print(hello2())                 # 结果：hello, zhang
print(hello2(greeting='Hi'))    # 结果：Hi, zhang


"""收集参数：定义函数形参中含有星号"""
def params(title, *parms):
    print(title, parms)


params('test', 1, 2, 3,)     # 结果：test (1, 2, 3)
params('test', 1)           # 结果：test (1,)
params("test")              # 结果：test ()

def params1(title, *parms, result):
    print(title, parms, result)


params1('test', 1, 2, 3, result='pass')     # 结果：test (1, 2, 3) pass
# params1('test', 1, 2, 3, 'pass')    # 报错：missing 1 required keyword-only argument: 'result'

def params2(title, *parms1, **parms2):
    print(title, parms1, parms2)         # 结果：test {'a': 1, 'b': 2, 'c': 3}


params2('test', 1, 2, a=1, b=2, c=3)    # 结果：test (1, 2) {'a': 1, 'b': 2, 'c': 3}


"""分配参数：调用函数时实参中含有星号"""
def add(title, x, y):
    print(title, x + y)


num = (1, 2)
print(*num)    # 结果：1 2
add('sum=', *num)       # 结果：sum= 3


def add(title, x, y):
    print(title, x + y)


num = {'x': 1, 'y': 2}
add('sum=', **num)      # 结果：sum= 3


"""作用域"""
# 局部变量
x = 1
def localVar():
    x = 2
localVar()
print(x)        # 结果：1

# 全局变量
def globalVar():
    global x
    x += 1
globalVar()
print(x)        # 结果：2


"""嵌套函数"""
msg = "hello"
def outerFunction(msg):
    def nestedFunciton():
       print(msg)
    nestedFunciton()
outerFunction(msg)      # 结果：hello

"""闭包函数"""
msg = "hello"
def outerFunction(msg):
    def nestedFunciton():
       print(msg)
    return nestedFunciton()
# 嵌套函数nestedFunciton中引用有封闭函数outerFunciton的值，且返回nestedFunciton函数，故nestedFunction为闭包函数
outerFunction(msg)      # 结果：hello


def outer():
    b = 1
    c = [1, 2, 3]
    def inner():
        nonlocal b      # 闭包中申请全局变量使用nonlocal
        b += 1
        c[0] += 1
        print(b, c)     # 结果：2 [2, 2, 3]
    return inner()
outer()


"""递归函数"""
# 使用递归方法计算n的阶乘
def fun(n):
    if n == 1:
        return 1
    else:
        return n * fun(n-1)
print(fun(5))               # 结果：120
# 使用递归方法计算x的n次幂，若使用power方法则直接power(x, n)
def fun1(x, n):
    if n == 0:
        return 1
    else:
        return x * fun1(x, n-1)
print(fun1(2, 3))           # 结果：8
