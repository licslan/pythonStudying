import math
# ---------------------函数学习
# Python内置了很多有用的函数，我们可以直接调用。
# 要调用一个函数，需要知道函数的名称和参数，比如求绝对值的函数abs，只有一个参数。可以直接从Python的官方网站查看文档：
# http://docs.python.org/3/library/functions.html#abs
print(abs(100))
print(abs(-20))
print(max(2, 3, 1, -5))

# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，
# 然后，在缩进块中编写函数体，函数的返回值用return语句返回。
# 我们以自定义一个求绝对值的my_abs函数为例
# -*- coding: utf-8 -*-


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(3))
print(my_abs(-7))


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(11.000))
# print(my_abs("11.000"))


# 返回多个值
# 函数可以返回多个值吗？答案是肯定的。
# 比如在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标：

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

# 但其实这只是一种假象，Python函数返回的仍然是单一值：
r = move(100, 100, 60, math.pi / 6)
print(r)
# 原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，
# 而多个变量可以同时接收一个tuple，
# 按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
# 定义函数时，需要确定函数名和参数个数；
# 如果有必要，可以先对参数的数据类型做检查；
# 函数体内部可以用return随时返回函数结果；
# 函数执行完毕也没有return语句时，自动return None。
# 函数可以同时返回多个值，但其实就是一个tuple。
# 我们先写一个计算x2的函数


def p(g):
    return g * g


print(p(5))

# 现在，如果我们要计算x3怎么办？可以再定义一个power3函数，
# 但是如果要计算x4、x5……怎么办？我们不可能定义无限多个函数。
# 你也许想到了，可以把power(x)修改为power(x, n)，用来计算xn，说干就干：


def power(g, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * g
    return s


print(power(5, 3))

# Python的错误信息很明确：调用函数power()缺少了一个位置参数n。
# 这个时候，默认参数就排上用场了。由于我们经常计算x2，
# 所以，完全可以把第二个参数n的默认值设定为2：


def power(g, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * g
    return s


print(power(5))

# 从上面的例子可以看出，默认参数可以简化函数的调用。设置默认参数时，有几点要注意：
# 一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
# 二是如何设置默认参数。
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
# 使用默认参数有什么好处？最大的好处是能降低调用函数的难度


# -------------------------------------------------------------------------------------
# 在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数
# 举个例子，我们来计算阶乘n! = 1 x 2 x 3 x ... x n，用函数fact(n)表示，可以看出：
# fact(n) = n! = 1 x 2 x 3 x ... x (n-1) x n = (n-1)! x n = fact(n-1) x n
# 所以，fact(n)可以表示为n x fact(n-1)，只有n=1时需要特殊处理。
# 于是，fact(n)用递归的方式写出来就是：
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(3))

# 递归函数的优点是定义简单，逻辑清晰。理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。
# 使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，
# 每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，
# 所以，递归调用的次数过多，会导致栈溢出。可以试试fact(1000)：
# print(fact(1000))


def facts(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


print(facts(10))
# 尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。
# 遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，
# 即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。


# 使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。
# 针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，
# 没有循环语句的编程语言只能通过尾递归实现循环。
# Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。




