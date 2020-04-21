# ************************************ Sort Python Dictionaries by Key or Value
# key_value = dict()
# key_value[2] = '64'
# key_value[1] = '69'
# key_value[4] = '23'
# key_value[5] = '65'
# key_value[6] = '34'
# key_value[3] = '76'
#
# s = list(key_value.keys())
# s.sort()
# print(s)
# print()  # Sort by key
# for i in s:
#     print(i, " : ", key_value.get(i))
# print()
# v = list(key_value.values())
# v.sort()   # Sort by Value
# for i in v:
#     for key in key_value:
#         if key_value.get(key) == i:
#             print(key, " : ", key_value.get(key))
#             break
#


# ***************************************Handling missing keys
# d = {"a": 1, "b": 23, "d": 12, "e": 21}
# i = input("enter key : ")
# if i in d.keys():
#     print(i, " : ", d.get(i))
# else:
#     print("Key not found : ", i)
#
# print(i, " : ", d.get(i, "Key not found"))

# OR

# from collections import defaultdict
# dic = defaultdict(lambda : "Key not found")
# dic["a"] = 1
# dic["c"] = 23
# dic["e"] = 12
# i = input("enter key : ")
# print(dic[i])


# ********************* ********dictionary with keys having multiple inputs
# d = dict()
# n = int(input("ENter number of time user want to perform action"))
# for i in range(n):
#     x = int(input("Ener value of x : "))
#     y = int(input("Ener value of y : "))
#     z = int(input("Ener value of y : "))
#     d[x, y, z] = x + y - z
#
# print(d)


# ****************************  find the sum of all items in a dictionary
# key_value = {2: 64, 1: 69, 4: 23, 5: 65, 6: 34, 3: 76}
# print(sum(list(key_value.keys())))
# print(sum(list(key_value.values())))
#
# print(sorted(key_value.values()))


# ********************************* sort list of dictionaries by values
# from operator import itemgetter
# lis = [
#     {"name": "Nandini", "age": 20},
#     {"name": "Manjeet", "age": 20},
#     {"name": "Nikhil", "age": 19}
# ]
# print(sorted(lis, key=itemgetter('age')))
# print(sorted(lis, key=itemgetter('name')))
# print(sorted(lis, key=lambda i: i['age']))
# print(sorted(lis, key=lambda i: i['name']))

# ***************************************************** Merging two Dictionaries
# key_value1 = {2: 64, 1: 69, 4: 23, 5: 65, 6: 34, 3: 76}
# key_value2 = {20: 64, 10: 69, 40: 23, 50: 65, 60: 34, 30: 76}
# ok = {**key_value1, **key_value2}
# key_value1.update(key_value2)
# print(key_value1)
# print(ok)


# ****************************************** Program to create grade calculator
# j = { "name":"Jack Frost",
#          "assignment" : [80, 50, 40, 20],
#          "test" : [75, 75],
#          "lab" : [78.20, 77.20]
#        }
#
#
# def get_avrg(k):
#     total = sum(k)
#     total = float(total)
#     return total/len(k)
#
# def get_final(jack):
#     assignment = get_avrg(jack['assignment'])
#     test = get_avrg(jack['test'])
#     lab = get_avrg(jack['lab'])
#
#     total = .1*assignment + .7*test + .2*lab
#     if total >= 90:
#         return total, 'A'
#     elif total >= 80:
#         return total, 'B'
#     elif total >= 70:
#         return total, 'C'
#     elif total >= 60:
#         return total, 'D'
#     else:
#         return 'E'
#
#
# print(get_final(j))


# ****************************** Check order of character in string using OrderedDict()
# from collections import OrderedDict
#
#
# def check_order(in_string, pattern):
#     dic = OrderedDict.fromkeys(in_string)
#     print(dic)
#     ptrlen = 0
#     for key, value in dic.items():
#         if key == pattern[ptrlen]:
#             ptrlen = ptrlen + 1
#
#         if ptrlen == len(pattern):
#             return True
#     return False
#
#
# inpt = 'kengineers rock'
# pattern = 'egr'
# print(check_order(inpt, pattern))


# ******************************** Find common elements in three sorted arrays
# ar1 = [1, 5, 10, 20, 40, 80]
# ar2 = [6, 7, 20, 80, 100]
# ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
#
# for i in ar1:
#     if i in ar3 and i in ar3:
#         print(i)


# ***************************** use Dictionary and counter to find winner of election
# from collections import Counter
# inpt = ['john', 'johnny', 'jackie', 'johnny', 'john', 'jackie', 'jamie', 'jamie',
#         'john', 'johnny', 'jamie', 'johnny', 'john', 'john']
#
# votes = Counter(inpt)
# max_vote = max(votes.values())
# for k, v in votes.items():
#     if max_vote == v:
#         print("Winner is : ", k)
#         break

# ******************************************* Find all duplicate characters in string
# s = 'geeksforgeeeks'
# d = {}
# for i in s:
#     d[i] = d.get(i, 0) + 1
#
# print([[i, d.get(i)] for i in d.keys() if d.get(i) > 1])


# *********************************************** Print anagrams together
# arr = ['cat', 'dog', 'tac', 'god', 'act']
# tmp = list()
#
# for i in range(len(arr)):
#     if arr[i] not in tmp:
#         tmp.append(arr[i])
#         for j in range(i+1, len(arr)):
#             if (arr[j] not in tmp) and (sorted(arr[i]) == sorted(arr[j])):
#                 tmp.append(arr[j])
#
# print(tmp)

# OR

# arr = ['cat', 'dog', 'tac', 'god', 'act']
# d = dict()
# l1 = list()
# for i in range(len(arr)):
#     l1.append(arr[i])
#     d[''.join(sorted(arr[i]))] = d.get(''.join(sorted(arr[i])), []) + l1
#     l1.remove(arr[i])
#
# print(d)

# ********************************* binary representations of two numbers are anagram
# def check_anagram(n1, n2):
#     bin1 = bin(n1)[2:]
#     bin2 = bin(n2)[2:]
#
#     l_diff = abs(len(bin1) - len(bin2))
#
#     if len(bin2) > len(bin1):
#         bin1 = "0"*l_diff + bin1
#     else:
#         bin2 = "0"*l_diff + bin2
#
#     if bin1 == bin2[::-1]:
#         print(True)
#     else:
#         print(False)
#
#
# check_anagram(8, 1)


# ********************************** Remove all duplicates words from a given sentence
# inpt = 'Geeks for Geeks'
# s = set(inpt.split(" "))
# print(' '.join(s))

# ****************************** find mirror characters in a string
# char_asc = 'abcdefghijklmnopqrstuvwxyz'
# char_dsc = 'zyxwvutsrqponmlkjihgfedcba'
# n = 3
# strng = "paradox"
# prefix = strng[0:n]
# postfix = strng[n:]
# for i in range(len(postfix)):
#     l = char_dsc[char_asc.index(postfix[i])]
#     postfix = postfix.replace(postfix[i], l)
#
# print(prefix+postfix)


# # ********************************** Convert a list of Tuples into Dictionary
# Input = [("akash", 10), ("gaurav", 12), ("anand", 14),
#          ("suraj", 20), ("akhil", 25), ("ashish", 30)]
#
# print(dict(Input))
#
# d = {}
# for k, v in Input:
#     d.setdefault(k, []).append(v)
# print(d)
