#  -----------------切片 学习
from collections import Iterable

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 原始办法  取前3个元素，应该怎么做？ # 笨办法：
print([L[0], L[1], L[2]])

# 循环
r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)


# 对这种经常取指定索引范围的操作，用循环十分繁琐，因此，
# Python提供了切片（Slice）操作符，能大大简化这种操作。
# 对应上面的问题，取前3个元素，用一行代码就可以完成切片

print(L[0:3], L[3])
print(L[0:3])
print(L[3])
print(L[0:3][0])
print(L[:3])

# 类似的，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片，试试：
print(L[-2:])
print(L[-2:-1])

# 切片操作十分有用。我们先创建一个0-99的数列：
L = list(range(100))
print(L)

# 取前十条 和 后十条
print(L[:10])
print(L[-10:])

# 前11-20个数：
print(L[10:20])

# 前10个数，每两个取一个：
print(L[:10:2])

# 所有数，每5个取一个：
print(L[::5])

# 甚至什么都不写，只写[:]就可以原样复制一个list：
print(L[:])

# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
print((0, 1, 2, 3, 4, 5)[:3])

# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串
print('ABCDEFG'[:3])
print('ABCDEFG'[::2])


# ---------------------- 迭代学习
# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
# 在Python中，迭代是通过for ... in来完成的，而很多语言比如C语言，迭代list是通过下标完成的，比如Java代码
# for (i=0; i<list.length; i++) {
#     n = list[i];
# }

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)


# 因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。
# 默认情况下，dict迭代的是key。如果要迭代value，可以用，
# 如果要同时迭代key和value，可以用for k, v in d.items()。
# 由于字符串也是可迭代对象，因此，也可以作用于for循环：
for value in d.values():
    print(value)

for ch in 'ABC':
    print(ch)


# 所以，当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，
# 而我们不太关心该对象究竟是list还是其他数据类型。
# 那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))





