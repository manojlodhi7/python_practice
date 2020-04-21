# # *************     find largest element in an array
#
# # ar = [121, 434, 353, 2342, 6457, 5, 75534, 3546, 453435, 5, 640000]
# # n = ar[0]
# # for i in ar:
# #     if i > n:
# #         n = i
# # print(n)
#
#
# #  *****************  array rotation
# # ar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # copy = ar.copy()
# # r = int(input("ENter rotation : "))
# # for i in range(len(ar)):
# #     if i < len(ar) - r:
# #         ar[i] = copy[i + r]
# #     else:
# #         ls = -len(ar)*2 + r + i
# #         ar[i] = copy[ls]
# #
# # print(ar)
#
# #  OR Easy one
# # ar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # copy = ar.copy()
# # r = int(input("rotation vlue"))
# # for i in range(len(ar)):
# #     ar[i] = copy[-(len(ar) - i) + r]
# #
# # print(ar)
# #
# # #  reverse rotaion
# # ar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # copy = ar.copy()
# # r = int(input("rotation vlue"))
# # for i in range(len(ar)):
# #     ar[i] = copy[i - r]
# #
# # print(ar)
#
# # ar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # copy = ar.copy()
# # r = len(ar)//2
# # for i in range(len(ar)):
# #     ar[i] = copy[-(len(ar) - i) + r]
# #
# # print(ar)
#
# # Python program to split array and move first
# # part to end.
#
#
# def splitArr(arr, n, k):
#     for i in range(0, k):
#         x = arr[0]
#         print("X : ", x)
#         for j in range(0, n - 1):
#             print("arr[j] : ", arr[j], " arr[j + 1] : ", arr[j + 1])
#             arr[j] = arr[j + 1]
#         arr[n - 1] = x
#
# # main
# arr = [12, 10, 5, 6, 52, 36]
# n = len(arr)
# print("len : ", n)
# position = 2
#
# splitArr(arr, n, position)
#
# for i in range(0, n):
#     print(arr[i], end=' ')

#
# ar = [1, 4, 3]
#
#
# def mono(arr):
#     return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
#
#
# print(mono(ar))


# ***************  remove Nth occurrence of the given word

# ls = ["can", "you",  "can", "a", "can", "?"]
# r = 'can'
# n = 2
# counter = 0
# ls2 = list()
# for i in range(len(ls)):
#     if ls[i] == r:
#         counter = counter + 1
#     if counter == n and ls[i] == r:
#         pass
#     else:
#         ls2.append(ls[i])
#
# print(ls2)

# ls = ["can", "you",  "can", "a", "can", "?"]
# print(ls.__contains__("an"))
# ls2 = []
# for i in range(len(ls)):
#     if ls2.__contains__(ls[i]):
#         pass
#     else:
#         ls2.append(ls[i])
#         print(ls[i], " : ", ls.count(ls[i]))
#
# ils = [1, 3, 5, 6, 7, 44]
# print(sum(ils))
#
# # CLear list 1
# ls2.clear()
# print("ls2 : ", ls2)
#
# # CLear list 2
# for i in range(len(ils)):
#     print(0)
#     ils.remove(ils[0])
#
# print("ils : ", ils)
#
#  # CLear list 3
# il2 = [1, 3, 5, 6, 7, 44]
# il2 = il2*0
# print(" il2 ", il2)

# # CLear list 4
# il3 = [1, 3, 5, 6, 7, 44]
# del il3[:]
# print(il3)

#
# # Second highest
# il4 = [1, 3, 5, 6, 7, 44]
# il4.remove(max(il4))
# print(max(il4))

# *******    N largest elements from a list

# l4 = [1, 33, 5, 6, 7, 44]
# tmp = []
# t = 0
# for j in range(3):
#     for i in range(len(l4)):
#         if l4[i] == max(l4) and l4[0] not in tmp:
#             t = l4[i]
#     l4.remove(t)
#     tmp.append(t)
# print(tmp)
# print(l4)


