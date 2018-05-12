# 当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？
# 使用type()
# 首先，我们来判断对象类型，使用type()函数：
# 基本类型都可以用type()判断：
import types

from day009.InheritanceAndPolymorphism import Animal, Dog, Cat

print(type(123))

# 如果一个变量指向函数或者类，也可以用type()判断：
print(type(abs))

# 但是type()函数返回的是什么类型呢？它返回对应的Class类型。
# 如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同：
print(type(123) == type(456))
print(type(123) == int)
print(type('abc')==type('123'))
print(type('abc') == str)
print(type('abc') == type(123))

# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：


def fn():
     pass


print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)


# 使用isinstance()
# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
# 我们回顾上次的例子，如果继承关系是：
# object -> Animal -> Dog -> Husky
# 那么，isinstance()就可以告诉我们，一个对象是否是某种类型。先创建3种类型的对象：

a = Animal()
d = Dog()
h = Cat()

print(isinstance(h, Cat))
print(isinstance(h, Dog))
print("----------")
print(isinstance(h, Dog))

# 并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (dict, list)))
print(isinstance((1, 2, 3), (dict, tuple)))


# 使用dir()
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，
# 它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print(dir('ABC'))