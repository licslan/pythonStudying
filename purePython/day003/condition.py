# ------------------------------计算机之所以能做很多自动化的任务，因为它可以自己做条件判断 条件判断学习
age = 20
if age >= 18:
    print('your age is', age)
    print('adult')

name = "w"
if name == "hwl":
    print("hello my name is hwl")
elif name == "wl":
    print("hello my name is JACK")
else:
    print("my name is jack ma")

age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')

#  input 输入学习
birthIn = input('birth: ')
birth = int(birthIn)
if birth < 2000:
    print('00前')
else:
    print('00后')