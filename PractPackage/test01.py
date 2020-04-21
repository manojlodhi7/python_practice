# x=1
# while x<=10 :
#     print(x)
#     x +=1

# y = int(input("enter number"))
# sum = 0
# i=1
# while i<=y :
#     sum = sum + i
#     i += 1
# print(sum)

# y = input("enter name : ")
# while y!= "manoj" :
#     y = input("enter name : ")
# print("thanks")

# l = int(input("enter number"))
# for k in range(l) :
#     for x in range(k+1) :
#         print("*", end=(""))
#     print()
#     k+=1

# n = int(input("enter number"))
# for i in range(1, n+1) :
#     print("*"*i)

# n = int(input("enter number"))
# for i in range(1, n+1) :
#     print(" "*(n-i), end=" ")
#     print("* "*i)


# n = int(input("enter number"))
# for i in range(1, n+1) :
#     k = i
#     for j in range(k) :
#         print(n-j, " ", end="")
#     print()
#
# for i in range(n+1, 1, -1) :
#     k = i
#     for j in range(k):
#         print(n - j, " ", end="")
#     print()


# for i in range(10) :
#     if i == 11:
#         print("value is 5, do not print it")
#         # continue
#         break
#         # pass
#     print(i)
# else:
#     print("else")


# for i in range(1, 50):
#     if i%9 == 0 :
#         print(i)

# x=99
# del x
# print(x)   # NameError: name 'x' is not defined

#
# x =input("enter: ")
# i=0
# for k in x :
#     print("Value is :{} and index is :{}".format(k, i))
#     i+=1

#
# s = "ABCDEFG"
# #   A  B  C  D  E  F  G
# #   0  1  2  3  4  5  6
# #  -7 -6 -5 -4 -3 -2 -1
#
# h = s[4:-2:-1]  # Back Direction : -2+1 = -1 >> 4 to -1 >> not possible in back dir >> o/p empty string
# k = s[2:-1:-1]  # Back Direction : -1+1 =  0  >> 2 to 0  >> -0 or -Zero not possible in back dir >> o/p empty string
# l = s[:0:1]     #  Foreword Dir  :  0-1 = -1 >> 0 to -1 >> -1 not available in frwd dir
# j = s[4:-2:-1]
# print(" Sliced string :", j)


# s, b = [eval(x) for x in input("Enter numbers : ").split(" ")]
# print(type(s), s, type(b), b)


# s = input("Enter string : ")
# ctyList = ["Pune", "Mumbai", "Bhopal"]
# if s.strip() in ctyList:
#     print("Valid city name")
# else:
#     print("Enter correct city name")

# s = input("Enter string to reverse: ")
# print(s[::-1])
# l = len(s) - 1
# while l >= 0:
#     print(s[l], end="")
#     l = l-1
# print()
# d = s.split(" ")
# for x in d:
#     print(x[::-1], end=" ")
# print()


# s = input("Enter string :")
# subString = input("Enter sub string to reverse :")
# print("First occurance", s.find(subString))
# print("Second occurance", s.find(subString, s.find(subString)+1, len(s)))

#
# s = input("Enter string :")
# subString = input("Enter sub string to reverse :")
# try:
#     print("First occurance", s.index(subString))
#     try:
#         print("Second occurance", s.index(subString, s.index(subString) + 1, len(s)))
#     except ValueError:
#         print("Second occ not found")
# except ValueError:
#     print("String not found")


# s = input("Enter string :")
# sb = ""
# for x in s:
#     k = 0
#     l = []
#     if x not in sb:
#
#         while k < len(s):
#             try:
#                 k = s.index(x, k, len(s)) + 1
#                 l.append(k-1)
#             except ValueError:
#                 break
#     if len(l) != 0:
#         print("{} occurance".format(x), l)
#     sb = sb + x


# s = input("Enter string :")
# sb = input("last index of : ")
# print("last index of {} is {}".format(sb, s.rfind(sb)))


# s = input("Enter string :")
# sb = input("string to count : ")
# print("Count {} is {}".format(sb, s.count(sb)))

# s = input("Enter string :")
# old = input("Old string value :")
# new = input("New string value :")
# print("Replcaed string is", s.replace(old, new))


# s = input("Enter string list :").split()
# old = input("Seprator value :")
# print(type(s))
# o = old.join(s)
# print(o)
#
#
# l = ["kkk", "llllll", "jjjjjj"]
# s = "-".join(l)
# print(s)

# s = input("Enter string to convert in different case :")
# print(s.upper())
# print(s.lower())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())


# s = 'learning Python is very easy'
# print(s.startswith("learning"))
# print(s.endswith("learning"))
# print(s.endswith("easy"))

# s = input("Enter string :")
# # if s.isalnum():
# #     print("Contains Alpha numeric values")
# # if s.isalpha():
# #     print("Contains only Alpha values")
# # if s.isnumeric():
# #     print("Contains only numeric values")
# # if s.isspace():
# #     print("Contains only spaces values")
# # if s.isdigit():
# #     print("Contains only Digit values")
# # if s.isupper():
# #     print("Contains upper case")
# # if s.islower():
# #     print("Contains lower case")


# s = input("Enter string :")
# print("Contains Alpha numeric values : ", s.isalnum())
# print("Contains only Alpha values : ", s.isalpha())
# print("Contains only numeric values : ", s.isnumeric())
# print("Contains only spaces values : ", s.isspace())
# print("Contains only Digit values : ", s.isdigit())
# print("Contains only upper case : ", s.isupper())
# print("Contains only lower case : ", s.islower())


# name = 'Python'
# salary = 10000
# age = 48
# print("Name : {}, Salary : {}, age : {}".format(name, salary, age))
# print("Name : {2}, Salary : {1}, age : {0}".format(age, salary, name))
# print("Name : {x}, Salary : {y}, age : {z}".format(x=name, y=salary, z=age))


# name = 'Python'
# print(''.join(reversed(name)))


# s = input("Enter string :")
# for x in s:
#     print("Char is : {} and occurance count is : {}".format(x, s.count(x)))

# s = "a3b4h2a4"
# output = previous = ""
# for x in s:
#     if x.isalpha():
#         output = output + x
#         previous = x
#     else:
#         output = output + previous*(int(x)-1)
#         previous = ""
# print(output)


# s = input("Enter duplicate char string:")
# st = set()
# for x in s:
#     st.add(x)
# print(''.join(st))
# print(sorted(''.join(st)))

# print("{:0>9}".format("manoj"))

# d = {"Name": "Manoj", "Age": 29}
# print("{Name}'s age is {Age}".format(**d))


# l1 = []
# l2 = [2, 5, 8, 9]
# l3 = eval(input("Enter List:"))
# l4 = "My Name Contains List Of Elements".split()
# print(type(l1), type(l2), type(l3), type(l4))
# print(l3)
# print(l4)

# l = [2, 5, 8, 9, 7, 4, 6, 76, 34]
# print(l[0])
# print(l[1:6:2])
# for x in l:
#     if x % 2 == 0:
#         print(x)

# l = [2, 5, 8, 9, 7, 4, 6]
# i = 0
# for x in l:
#     print("Element at index {} is {}".format(i, x), i - len(l))
#     i = i + 1


# l = [2, 5, 8, 9, 7, 4, 6]
# i = len(l)
# for x in range(i):
#     print(l[x], x, x-i)

# l = []
# l.append("a")
# l.append("b")
# l.insert(0, list(range(4)))
# print(l)


# l = [2, 5, 2, 9, 7, 2, 6]
# l.remove(2)
# print(l)
# print(l.pop())
# print(l.pop(1))
# print(l)

# l1 = [4, 66, 87, 23, 66]
# l2 = ["H", "K", "a", "n", "A", "h"]
# l1.sort()
# l2.sort()
# print(l1)
# print(l2)


# l1 = [4, 66, 87, 23, 66]
# l2 = l1
# print(id(l1))
# print(id(l2))
# l2.insert(1, 55)
# print(l1)
# print(l2)

# l1 = [4, 66, 87, 23, 66]
# l2 = l1[:]
# print(id(l1))
# print(id(l2))
# l2.insert(1, 55)
# print(l1)
# print(l2)

# l1 = [4, 66, 87, 23, 66]
# l2 = l1.copy()
# print(id(l1))
# print(id(l2))
# l2.insert(1, 55)
# print(l1)
# print(l2)


# l1 = [4, 66, 87, 23, 66]
# l2 = [4, 55, 66, 87, 23, 66]
# l3 = l1 + l2
# print(l3*2)

# l1 = ["Dog", "Cat"]
# l2 = ["Dog", "Rat"]
# print(l1 == l2)
# print(l1[0] == l2[0])
# print(id(l1[0]), id(l2[0]))


# l1 = [4, 20, 87, 23, 66]
# l2 = [4, 11, 66, 87, 23, 66]
# print(l1 >= l2)


# l1 = [4, 20, 87, 23, 66]
# print(l1)
# l1.clear()
# print(l1)

# l1 = [[4, 20, 87, 23, 66], [5, 1, 43, 23, 55], [33, 11, 34, 23, 78]]
# for i in l1:
#     for j in i:
#         print(j, end=" ")
#     print()


# l1 = [4, 20, 87, 23, 43, 22, 66]
# l2 = [x for x in l1 if x % 2 == 0]
# print(l2)

# l1 = [4, 20, 87, 23, 66, 1]
# l2 = [5, 1, 43, 23, 55, 20]
# print([x for x in l1 if x in l2])
# print([x for x in l1 if x not in l2] + [x for x in l2 if x not in l1])


# s1 = "A string containing all ASCII characters that are considered whitespace. This includes the characters space, tab, linefeed, return, formfeed, and vertical tab."
# print([[x, len(x)] for x in s1.split()])
#
# vowels = ['a', 'e', 'i', 'o', 'u']
# found = []
# for letter in s1:
#     if letter in vowels:
#         if letter not in found:
#             found.append(letter)
#
# print(found)


# t = (10, 55, 30, 2, 12, 66)
# print(id(t))
# t2 = sorted(t)
# t = sorted(t)  # this is list
# print(id(t))
# print(id(t2))
# print(t2.count(222))
# print(min(t2))
# print(max(t2))

# t = (10, 55, 30, 2, 12, 66)
# t = sorted(t)
# print(type(t))  # return list
# t = tuple(t)
# print(type(t))  # return tuple

# t2 = "manoJ"
# print(min(t2))
# print(max(t2))

# a = 9
# b = 7
# c = 6
# t = a, b, c
# l = [a, b, c]
# print(type(t))
# print(type(l))
# x, y, z = t
# q, w, e = l
# print(x,y,z,q,w,e)


# s = {1, 2, 3, 4, 5}
# s.update([6, 7, 8])  # not allowed ==> s.update(6, 7, 8) or s.update(9,) or s.update(9)
# print(s)
# s.update((9,))
# print(s)

# s1 = "A string containing all ASCII characters that are considered whitespace. This"
# vowels = {'a', 'e', 'i', 'o', 'u'}
# s2 = set(s1)
# for x in s2:
#     if x in vowels:
#         print(x, end=" ,")

# s1 = "A string containing all ASCII characters that are considered whitespace. This"
# vowels = {'a', 'e', 'i', 'o', 'u'}
# s2 = set(s1)
# print(vowels & s2)
# print(vowels.intersection(s2))

# d = {1: "Manoj", 2: "Kumar", 3: "Ok"}
# print(d)
# d[3] = "Lodhi"
# print(d)

# d = {1: "Manoj", 2: "Kumar", 3: "Ok"}
# print(d)
# del d[1]
# print(d)
# d.clear() # {}  empty dic
# print(d)
# del d # Name error d is not defined
# print(d)

# s = "missippiss"
# d = {}
# for x in s:
#     d[x] = d.get(x, 0)+1
# print(d)
#
#
# def printhello():
#     print("Hi', There")
#
#
# printhello()
#
#
# def welcome(name):
#     print("Hi {}, Welcome".format(name))
#
#
# welcome("Manoj")
#
#
# def square(num):
#     print("Square root of number {} is : {}".format(num, num*num))
#
#
# square(4)

# def add(x, y):
#     return x+y
# print(add(10,4))
#
# def chek_num(num):
#     if num%2 == 0:
#         return "Even"
#     else:
#         return "Odd"
#
# print(chek_num(0))

# def factorial(num):
#     result = 1
#     while num != 0:
#         result = result*num
#         num = num-1
#     return result
#
# print(factorial(3))

#
# def sum_sub(x, y):
#     return x+y, x-y
#
# print(sum_sub(40,20))

# def wish(name, msg):
#     print("Hi {}, we have message for you: '{}'".format(name, msg))
#
# wish(msg="Go to hell", name="Rahul")
# wish( name="Rahul", msg="Go to hell")


# def wish(num, name, msg):
#     print("Hi {}, we have {} message for you: '{}'".format(name, num, msg))
#
# wish(1, msg="Go to hell", name="Rahul")

#
# def wish(name = "Manoj"):
#     return "{} lets learn python".format(name)
#
# print(wish())
# print(wish("Kumar"))


# def sun_of_all_input(*num):
#     sum = 0
#     for n in num:
#         sum = sum + n
#     return sum
#
# print(sun_of_all_input())
# print(sun_of_all_input(23,55,10))
# print(sun_of_all_input(10,20,30,40))


# def sun_of_all_input(id,  *num):
#     sum = 0
#     for n in num:
#         sum = sum + n
#     return "Student Name is {}, id : , clg name :  and total numbers : {}".format(id, sum)
#
# print(sun_of_all_input(2,4,5,6,7))


# def f1(*num, v1):
#     sum = 0
#     for n in num:
#         sum = sum + n
#     return sum, v1
#
# print(f1(12,8,80, v1="Manoj"))
# print(f1(12,8,80,"Manoj")) #  TypeError: f1() missing 1 required keyword-only argument: 'v1'


# def display_items(**item):
#     for k, v in item.items():
#         print(k, "=", v)
#
# display_items(r1=10, r2=2, r3=50, r4=30)
# display_items(name="Manoj", middleName="Kumar", surname="Lodhi")

# a = 10
# def f1():
#     a = 20
#     print(a)
#     print(globals()['a'])
# f1()

#
# def factorial(n):
#     if n == 0:
#         result = 1
#     else:
#         result = n * factorial(n-1)
#     return result
#
# print(factorial(5))

# print(list(filter(lambda x:x%2 == 0, [12,3,1,56,45,67,66,88])))
# print(list(filter(lambda x:x%2 != 0, [12,3,1,56,45,67,66,88])))

# l1 = [12,3,1,56,45,67,66,88]
# l2 = [45,67,66,88,12,3,1,56]
# l3 = [45,67,66,88,12,3,1]
# print(list(map(lambda x: 2*x, l1)))
# print(list(map(lambda x,y: x*y, l1, l2)))
# print(list(map(lambda x,y: x*y, l1, l3)))

# from functools import *
# l3 = [6,3,1, 2]
# print(reduce(lambda x,y: x+y, l3))
# print(reduce(lambda x,y: x*y, l3))
# print(reduce(lambda x,y: x*y, range(1, 10, 2)))
# print(list(range(1,10,2)))


# def wish():
#     print("Hi, Goodmorning")
#
# greeting = wish
#
# greeting()
# wish()
#
# del wish
#
# greeting()
# wish()


# def outer():
#     print("outer started")
#     def inner():
#         print("inner started")
#     print("return inner")
#     return inner
#
# f1 = outer
# f2 = outer()
# f1()
# print("-----------")
# f2()

# def smart_div(func):
#     def inner(a, b):
#         if a == 0:
#             return "First value is zero"
#         elif b == 0:
#             return "second value is zero"
#         else:
#             return func(a, b)
#     return inner
# @smart_div
# def divide(a, b):
#     return a / b
# print(divide(12, 5))
# print(divide(10, 0))
# print(divide(0, 40))


# def no_wish(func):
#     def inner(name):
#         if name=="MONGO":
#             return "{}, Not welcome".format(name)
#         else:
#             return func(name)
#     return inner
#
# def wish(name):
#     return "Hi {}, Welcome".format(name)
#
# updated_wish = no_wish(wish)
#
# print(updated_wish("Manoj"))
# print(updated_wish("MONGO"))


# def num_02(func):
#     def inner(n):
#         n = n*2
#         func(n)
#     return inner
#
# def num_01(func):
#     def inner(n):
#         n = n * n
#         func(n)
#     return inner
#
# @num_02
# @num_01
# def num(n):
#     print(n)
#
# num(3)


# def my_frst_gen():
#     yield "a"
#     yield "b"
#     yield "c"
#
# g = my_frst_gen()
# print(type(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))  # Traceback (most recent call last):


# def counter(num):
#     print("Start counter")
#     while num > 0:
#         yield num
#         num = num - 1
#
# value = counter(5)
#
# print(type(value))
# for x in value:
#     print(x)


# def fabonacci(max_num):
#     a, b = 0, 1
#     while b <= max_num:
#         yield a
#         a, b = b, a+b
#
# fab = fabonacci(50)
#
# print(list(fab))
#
#
# import random
# import time
# name = ["Manoj", "Kumar", "Lodhi", "Singh"]
# subjects = ["P", "M", "C", "B"]
#
# def p_list(n_people):
#     result = []
#     for i in n_people:
#         person = {
#             'id' : i,
#             'name' : random.choice(name),
#             'sub' : random.choice(subjects)
#         }
#         result.append(person)
#     return result
#
#
# def p_gen(n_people):
#     for i in n_people:
#         person = {
#             'id' : i,
#             'name' : random.choice(name),
#             'sub' : random.choice(subjects)
#         }
#         yield person
#
# t1 = time.perf_counter()
# p_list(range(10000000))
# t2 = time.perf_counter()
# print(t2-t1)
# t3 = time.perf_counter()
# p_gen(range(10000000))
# t4 = time.perf_counter()
# print(t4-t3)

# from random import *
# print(randint(100000, 999999))  # this does not include number like 000001 etc
# print(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), sep="")
# print(str(randint(000000, 999999))) # 000000 = 0 from 0 to 999999
# print("------Simplest OTP-----")
# for i in range(6):
#     print(randint(0, 9), end="")
# print()
# print("----------- Alpha Numberic random ---------")
# for i in range(6):
#     if i % 2 == 0:
#         print(randint(0, 9), end="")
#     else:
#         print(chr(randint(65, 65+25)), end="")


# from random import *
# l1 = list(range(10))
# print(l1)
# for i in l1:
#     print(random())
# print("----------")
# for i in l1:
#     print(randint(10, 20))
# print("----------")
# for i in l1:
#     print(uniform(10, 20))
# print("----------")
# for i in l1:
#     print(choice(l1))


