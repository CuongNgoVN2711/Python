
# def getPoints(answers, p):
#     questionPoints =  lambda i, ans : i + 1 if ans is True else -p

#     res = 0
#     for i, ans in enumerate(answers):
#     	print(i)
#         res += questionPoints(i, ans)
#     return res

# answers = [True, True, False, True]
# p = 2
# res = getPoints(answers,p)


# a = [3,5]
# b = [3,5]
# print(all(e in b for e in a))




# from itertools import cycle

# name = 'test'
# def cyclicName(name, n):
#     gen = cycle(name)
#     res = [next(gen) for _ in range(n)]
#     return ''.join(res)
# print(cyclicName(name,6))
from itertools import dropwhile, chain, permutations, count,islice,takewhile
# players = ['a','b','s','c']
# k=3
# print([i for i in sorted(list(permutations(players,k))) if i == sorted(i)])

# array = [1, -3, 2, 1, -1]
# sub_array = [i for i in array if i > 0]
# print()
#######################################################################################
#PROPERTY
# class Celsius:
#     def __init__(self, temperature = 0):
#         self._temperature = temperature

#     def to_fahrenheit(self):
#         return (self.temperature * 1.8) + 32

#     def get_temperature(self):
#         print("Getting value")
#         return self._temperature

#     def set_temperature(self, value):
#         if value < -273:
#             raise ValueError("Temperature below -273 is not possible")
#         print("Setting value")
#         self._temperature = value

#     temperature = property(get_temperature, set_temperature)
#     # temperature = temperature.getter(get_temperature)
#     # temperature = temperature.setter(set_temperature)
# temper = Celsius(-512)
# print(temper.temperature)
# temper.temperature = -32

#########################################################33
#HIGH ORDER FUNCTION
#EX1
# def is_called():
#     def is_returned(name):
#         print("Hello {}".format(name))
#     return is_returned

# new = is_called()
# new('Bill')
################################################################
#DECORATOR
# def Power(exponent):
# 	def power(base):
# 		return base**exponent
# 	return power
# power_of_two = Power(2)
# power_of_three = Power(3)
# print(power_of_two(2))
# print(power_of_three(2))

#EX2
# def smart_divide(func):
#    def inner(a,b):
#       print("I am going to divide",a,"and",b)
#       if b == 0:
#          print("Whoops! cannot divide")
#          return

#       return func(a,b)
#    return inner

# @smart_divide
# def divide(a,b):
#     return a/b

# print("Result:",divide(5,0))

#CHAINING DECORATOR
# def star(func):
#     def inner(*args, **kwargs):
#         print("*" * 30)
#         func(*args, **kwargs)
#         print("*" * 30)
#     return inner

# def percent(func):
#     def inner(*args, **kwargs):
#         print("%" * 30)
#         func(*args, **kwargs)
#         print("%" * 30)
#     return inner

# # @star
# # @percent
# def printer(msg):
#     print(msg)
# #printer("Hello")
# #Similar with this
# printer = star(percent(printer))
# printer("Hello")

########################################################
#GENERATOR
#EX1
# def my_gen():
#     # n = 1
#     # print('This is printed first')
#     # # Generator function contains yield statements
#     # yield n

#     # n += 1
#     # print('This is printed second')
#     # yield n

#     # n += 1
#     # print('This is printed at last')
#     # yield n
#     for i in range(1,3):
#     	print('this is {}'.format(i))
#     	yield i
#     print('?')
# # def my_gen():
# # 	n = 1
# # 	print('This is printed first')
# # 	return n
# for item in my_gen():
# 	print(item)

#EX2
# Intialize the list
# my_list = [1, 3, 6, 10]

# #GENARATOR EXPRESSION
# # a = (x**2 for x in my_list)
# #Similiar with this
# def my_gen():
# 	for x in my_list:
# 		yield x**2
# a = my_gen()	

# for item in a:
# 	print(item)

#EX3: INFINITE LOOP
# def all_even():
#     n = 0
#     while n < 1000:
#         yield 2**n
#         n += 1
# for i in all_even():
# 	print(i)


#ARBITRARY ARGUMENTS
# def greet(*names):
#    """This function greets all
#    the person in the names tuple."""

#    # names is a tuple with arguments
#    for name in names:
#        print("Hello " + name)

# greet("Monica","Luke","Steve","John")

#NON-LOCAL KEYWORD
# def outer():
#     x = "local"
    
#     def inner():
#         nonlocal x
#         x = "nonlocal"
#         print("inner: " + x)
    
#     inner()
#     print("outer: " + x)

# outer()

#YIELD
# def Factorial():
# 	a = 87
# 	b = a - 1
# 	while b > 0:
# 		yield a * b
# 		a = a * b
# 		b -= 1
		
# for item in Factorial():
# # 	print(item)


# #SHALLOW COPY
# import copy

# # old = [[1,2,3],[4,5,6]]
# # new = copy.copy(old)
# # new.append([7,8,9])
# # print(old)
# # print(new)
# # old[0][0] = 0
# # print(old)
# # print(new)
# # print(id(old))
# # print(id(new))

# # DEEP COPY
# old = [[1,2,3],[4,5,6]]
# new = copy.deepcopy(old)
# new.append([7,8,9])
# print(old)
# print(new)
# old[0][0] = 0
# print(old)
# print(new)
# print(id(old))
# print(id(new))

#ASSERT
def divide(number):
	assert number != 0, "number is zero"
	return 10//number

print(divide(0))