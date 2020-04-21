# a = int(input("enter number 1 : "))
# b = int(input("enter number 2 : "))
#
# print("Sum of a and b is :", a+b)


# ***************    Factorial  **********
# import math
# a = int(input("enter number 1 : "))
# print("Factorial of a is :", math.factorial(a))
#
# # or
#
# i = 1
# fact = 1
# while i <= a:
#     fact = fact * i
#     i = i + 1
#
# print("Factorial of a is :", fact)
#
# # or
#
#
# def factorial(n):
#     return 1 if (n == 0 or n == 1) else n * factorial(n-1)
#
#
# print("Factorial of a is :", factorial(a))


# ************* Armstrong Number  153 = 1*1*1 + 5*5*5 + 3*3*3       ***********

# a = input("ENter number : ")
# print("User input is : ", a)
# l = len(a)
# a = int(a)
# b = a
# n = 0
# while a > 0:
#     n = n + pow(a % 10, l)
#     a = a // 10
#
# print(" number is Armstrong", b == n)


# ************* Prime number  2, 3, 5, 7, 11, …      ***********

# a = int(input("ENter number : "))
# b = 2
# prime = True
# if a > 1:
#     while b < a // 2:
#         if a % b == 0:
#             print("number is not Prime")
#             prime = False
#             break
#         b = b + 1
# if prime:
#     print("number is Prime")
#
# # OR
#
# if a > 1:
#     for n in range(2, a):
#         if a % n == 0:
#             break
#     else:
#         print("number is Prime")


# ************* n-th Fibonacci number  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, …     ***********

# a = int(input("ENter number : "))
#
# def feb(n):
#
#     if n <= 0:
#         return "incorrect number"
#     elif n == 1:
#         return 0
#     elif n == 2:
#         print(1)
#         return 1
#     else:
#         return feb(n - 1) + feb(n - 2)
#
#
# print(feb(a))

# OR

# fn = 0
# n1 = 0
# n2 = 1
# i = 3
# if a <= 0:
#     print( "incorrect number")
# elif a == 1:
#     print(0)
# elif a == 2:
#     print(1)
# elif a > 2:
#     while i <= a:
#         fn = n1 + n2
#         n1 = n2
#         n2 = fn
#         i = i + 1
#     print(fn)


# ****************** check if a given number is Fibonacci number?

# def check_num(n):
#     fibonacci = False
#     a = 0
#     if n == 0 or n == 1:
#         fibonacci = True
#     else:
#         fn1 = 0
#         fn2 = 1
#         for i in range(2, n):
#             a = fn1 + fn2
#             fn1 = fn2
#             fn2 = a
#             if a == n:
#                 fibonacci = True
#                 break
#     return "Number is Fibonacci" if fibonacci else "Number is not Fibonacci"
#
#
# print(check_num(int(input("Enter number : "))))


# ***************** Cube sum of first n natural numbers
total = 0
for i in range(1, int(input("Enter number : "))+1):
    total = total + pow(i, 3)

print(total)


