# ********************************************     string is palindrome or not
# s = "NITIN"
# r = s[::-1]
# print(s == r)
# print(s[1])

# OR

# s = "NITIN"
# for i in range(len(s)//2):
#     if s[i] != s[len(s) - 1 - i]:
#         print("False")
#         break
# else:
#     print("True")


# ********************************************* Reverse words in a given String

# s = "geeks quiz practice code"  # "code practice quiz geeks"
# sar = s.split(" ")
# s2 = ""
# for i in sar:
#     s2 = i + " " + s2
#
# print(s2)
#
#
# # ********************************************* Reverse words in a given String
#
# s = "geeks quiz practice code"  # edoc ecitcarp ziuq skeeg
# sar = s.split(" ")
# s2 = ""
# for i in sar:
#     s2 = i[::-1] + " " + s2
#
# print(s2)
# # OR
# print(s[::-1])
#
#
# # ********************************************* Reverse words in a given String
#
# s = "geeks quiz practice code"  # skeeg ziuq ecitcarp edoc
# sar = s.split(" ")
# s2 = ""
# for i in sar:
#     s2 = s2 + " " + i[::-1]
#
# print(s2)


# *********************************************** remove i’th character from string
# s = "geeks quiz practice code"
# n = int(input("Enter index to remove :"))
# print(s[n-1])
# print(s)
# s1 = s[0:n-1] + s[n:]
# s2 = s.replace(s[n-1], '')
# print(s1)
# print(s2)
# s3 = ""
# for i in range(len(s)):
#     if i != n-1:
#         s3 = s3 + s[i]
# print(s3)

# ******************************   Check if a Substring is Present in a Given String
#
# s = "geeks quiz practice quiz code quiz"
# print(s.find("quiz"))
# print(s.rfind("quiz"))
# print(s.index("quiz"))
# print(s.count("quiz"))
# print()
# print(s.find("ok"))  # -1 if not present
# print(s.rfind("ok"))  # -1 if not present
# # print(s.index("ok")) # Error substring not found
# print(s.count("ok"))  # count 0


# *********************************************** Find length of a string
# len(s)
# for loop
# while loop

# s = "geeks"
# some_random_str = '--'
# print((some_random_str.join(s)))  # g--e--e--k--s
# print((some_random_str.join(s)).count(some_random_str) + 1)


# **************************** Program to accept the strings which contains all vowels
# s = "aeuo"
# if s.find("a")*s.find("e")*s.find("i")*s.find("o")*s.find("u") >=0:
#     print("contains all vowels")
# else:
#     print("False")
# # OR
# if s.count("a")*s.count("e")*s.count("i")*s.count("o")*s.count("u") > 0:
#     print("contains all vowels")
# else:
#     print("False")

# OR
# s1 = "aedlfdla"
# s2 = "aeiou"
# s3 = set()
# for i in s1:
#     if i in s2:
#         s3.add(i)
#
# if len(s3) == 5:
#     print("True")
# else:
#     print("False")

# ********************************  Remove all duplicates from a given string

# s = "adbababcdcdefabcab"
# tmp = ""
# for i in range(len(s)):
#     if s[i] not in tmp:
#         tmp = tmp + s[i]
#
# print(tmp)
#
# # or
# s1 = "adbababcdcdefabcab"
# ln = len(s)
# for i in range(ln):
#     f = s.find(s[i])
#     s = s[0:f+1] + s[f+1:].replace(s[i], " ")
#
# print(s.replace(" ", ""))
# # OR
# s1 = "adbababcdcdefabcab"
# print("".join(set(s1)))

# ****************************** Program to check if a string contains any special character
# import re
# s = "eghoergerh89745(^#("
# tmp = ""
# for i in s:
#     if len(re.findall("[a-zA-Z0-9]", i)) == 0:
#         tmp = tmp + i + " "
#
# print(tmp)
#
# for i in s:
#     if (ord(i) not in range(97, 123)) and (ord(i) not in range(65, 91)) and (ord(i) not in  range(48, 58)):
#         print(i)
#
# print("******")
# for i in s:
#     if not (i.isalpha() or i.isalnum() or i.isspace()):
#         print(i)


# ************************* Generating random strings until a given string is generated
# import string
# import random
# print(string)
# poss_comb = string.ascii_lowercase + string.digits + string.ascii_uppercase
# print(poss_comb)
# print(string.ascii_letters)
# # given string
# k = "Man"
# tmp = ""
# count = 0
# while tmp != k and len(tmp) < 3:
#     n = random.choice(poss_comb)
#     count = count + 1
#     # print("n : ", n, "   : ", count)
#     if n == k[len(tmp):len(tmp)+1]:
#         tmp = tmp + n
#
# print("    tmp : ", tmp, "Total count : ", count)

# **************** random
# s= "10101a01"
#
# if __name__ == "__main__":
#     print(s)


# ***************************** Find all close matches of input string from a list
# from difflib import get_close_matches
# print(get_close_matches('appel', ['ape', 'apple', 'peach', 'puppy']))

# ****************************** find uncommon words from two Strings
# A = "Geeks for Geeks abc"
# B = "Learning from Geeks for Geeks"

# tmp = ""
# for i in A.split(" "):
#     if (i not in B) and (i not in tmp):
#         tmp = tmp + i + " "
#
# for i in B.split(" "):
#     if (i not in A) and (i not in tmp):
#         tmp = tmp + i + " "
#
# print(tmp)

# OR
# s1 = set(A.split(" "))
# s2 = set(B.split(" "))
# print((s2 - s1).union(s1 - s2))

# OR
#
# def UncommonWords(A, B):
#     # count will contain all the word counts
#     count = {}
#
#     # insert words of string A to hash
#     for word in A.split():
#         count[word] = count.get(word, 0) + 1
#
#     # insert words of string B to hash
#     for word in B.split():
#         print("1 ", type(count.get(word, 0)))
#         print("2 ", type(count.get(word)))
#         count[word] = count.get(word, 0) + 1
#
#
# # return required list of words
#     return [word for word in count if count[word] == 1]
#
#
# # Driver Code
# A = "Geeks for Geeks"
# B = "Learning from Geeks for Geeks"
#
# # Print required answer
# print(UncommonWords(A, B))

# ***************************************** Permutation of a given string
# from itertools import permutations
# s = 'ABC'
# for i in permutations(s):
#     print(''.join(i))
#
# OR
# def permute(data, i, length):
#     if i == length:
#         print(''.join(data))
#     else:
#         for j in range(i,length):
#             #swap
#             data[i], data[j] = data[j], data[i]
#             print("      : ", data[i], data[j], "  i : ", i+1, "data : ", data)
#             permute(data, i+1, length)
#             data[i], data[j] = data[j], data[i]
#             print("**************   : ", data[i], data[j], "  i : ", i, "data : ", data)
#
#
# string = "ABC"
# n = len(string)
# data = list(string)
# permute(data, 0, n)

# *********************************        Check for URL in a String

# import re
#
# def Find(string):
#     url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ] |(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
#     return url
#
#
# # Driver Code
# string = '''My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/
# articles in the portal
# of http://www.geeksforgeeks.org/   lkjl kh'''
# print("Urls: ", Find(string))

# ******************** String slicing in Python to check if a string can become empty by recursive deletion
# **********Not perfectly working
# s = "dlfijdlf"
# def dl(strng):
#     if len(strng) == 0:
#         pass
#     print("strng len  ***** : ", strng)
#     while True:
#         if len(strng) == 0:
#             break
#         else:
#             strng = strng.replace(strng[0], "")
#             print("strng len : ", len(strng))
#             dl(strng)
#
# dl(s)

# OR correct way
# a = ""
# def delete(s, w):
#     global a
#     if s.find(w) >= 0:
#         s = s.replace(w, "")
#         delete(s, w)
#     else:
#         a = s
#     return a
#
#
# s1 = "GGEEKSEEKGEEKSSBGGEEGEEKSKSADGEEKS"
# w1 = "GEEKS"
# print(" remain string is : ", delete(s1, w1))


# ****************************************** Find all duplicate characters in string
s1 = "GKSADGEEKS"
count = {}
for char in s1:
    count[char] = count.get(char, 0) + 1

for i in count:
    if count.get(i) >1:
        print(i)




