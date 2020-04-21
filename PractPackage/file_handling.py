# f1 = open("C:/Practice_Python_Projects/PyPractice/PractPackage/files/first_file.txt", "r")
# print("File Name : ", f1.name)
# print("File Closed : ", f1.closed)
# print("File Mode : ", f1.mode)
# print("File readable : ", f1.readable())
# print("File writable : ", f1.writable())
# print("File read : ", f1.read())
# f1.close()
# print("File Closed : ", f1.closed)


# f1 = open("C:/Practice_Python_Projects/PyPractice/PractPackage/files/first_file.txt", "w")
# print("File Mode : ", f1.mode)
# print("File readable : ", f1.readable())
# print("File writable : ", f1.writable())
# # print("File read : ", f1.read())  # io.UnsupportedOperation: not readable
# f1.write("gold mine \n")
# l1 = ["Manoj \n", "Kumar \n", "Lodhi \n"]
# f1.writelines(l1)
# f1.close()


# f1 = open("C:/Practice_Python_Projects/PyPractice/PractPackage/files/first_file.txt", "a")
# print(f1.mode)
# print(f1.readable())
# print(f1.writable())
# f1.write("Append mODE \n")
# f1.writelines(["Appnd_01 \n", "Appen_02 \n"])
# # print(f1.read())  # UnsupportedOperation: not readable
# f1.close()

#  Dangerous Operation Bawa
# f1 = open("C:/Practice_Python_Projects/PyPractice/PractPackage/files/first_file.txt", "r+")
# print(f1.readable())
# print(f1.writable())
# f1.write("r+ mode \n")
# f1.close()


# f1 = open("C:/Practice_Python_Projects/PyPractice/PractPackage/files/first_file.txt", "w+")
# print(f1.readable())
# print(f1.writable())
# f1.write("w+ mode \n")
# f1.close()


# Bahut Dangerous Bawa for reading
# f1 = open("C:/Practice_Python_Projects/PyPractice/PractPackage/files/first_file.txt", "a+")
# print(f1.name)
# print(f1.readable())
# print(f1.writable())
# s1 = f1.read()
# # f1.write("a+ mode \n")
# s2 = f1.readline()
# f1.close()
# print("s1", s1)
# print("s2", s2)


# f1 = open("C:/Practice_Python_Projects/PyPractice/PractPackage/files/first_file.txt", "x")  # FileExistsError

#
# f1 = open("C:/Practice_Python_Projects/PyPractice/PractPackage/files/first_file.txt", "w")
# f1.write("W write \n")
# f1.writelines(["Write \n", "Lists \n"])
# f1.close()
# f2 = open("C:/Practice_Python_Projects/PyPractice/PractPackage/files/first_file.txt", "r")
# print("------")
# print(f2.read())
# print("------")
# print(f2.readlines())
# print("------")
# print(f2.readline())
# print("------")
# print(f2.read(2))
# f2.close()


# with open("C:/Practice_Python_Projects/PyPractice/PractPackage/files/first_file.txt", "w") as f:
#     f.write("dkljfld\n")
#     print(f.closed)
# print(f.closed)


# with open("C:/Practice_Python_Projects/PyPractice/PractPackage/files/first_file.txt", "w+") as f1:
#     f1.write("W_write \n")
#     f1.writelines(["Write \n", "Lists"])
#     print("------", f1.tell())
#     f1.seek(0)
#     print(f1.read())
#     print("------", f1.tell())
#     f1.seek(0)
#     print(f1.readlines())
#     print("------", f1.tell())
#     f1.seek(0)
#     print(f1.readline())
#     print("------", f1.tell())
#     f1.seek(0)
#     print(f1.read(2))

# import os, sys
# def read_file(file_name):
#     if os.path.isfile(file_name):
#         with open(file_name, "r") as f1:
#             print(f1.tell())
#             f1.seek(0)
#             print(f1.read())
#     else:
#         print("File not available")
#     sys.exit(0)
#
# read_file(input("Enter file path: "))


# import os, sys
# def read_file(file_name):
#     if os.path.isfile(file_name):
#         f1 = open(file_name, "r")
#         print(f1.tell())
#         f1.seek(0)
#         print(f1.read())
#         f1.seek(0)
#     else:
#         print("File not available")
#         sys.exit(0)
#     f1.seek(0)
#     print("--------------")
#     l_count = w_count = c_count = 0
#     for line in f1:
#         l_count = l_count + 1
#         c_count = c_count + len(line)
#         words = line.split()
#         w_count = w_count + len(words)
#
#     print(l_count, c_count, w_count)
#
# read_file(input("Enter file path: "))


# f1 = open("C:/Practice_Python_Projects/PyPractice/PractPackage/files/image.jpeg", "rb")
# f2 = open("C:/Practice_Python_Projects/PyPractice/PractPackage/files/image_02.jpeg", "wb")
# new_image = f1.read()
# # print(new_image)
# f2.write(new_image)
# f1.close()
# f2.close()


# import csv
# with open("C:/Practice_Python_Projects/PyPractice/PractPackage/files/first_file.csv", "w", newline="") as f1:
#     w = csv.writer(f1)
#     w.writerow(["ID", "Name", "Role", "Location"])
#     n = int(input("Enter total number of employees: "))
#     for i in range(n):
#         e_id = input("Enter ID: ")
#         name = input("Enter name: ")
#         role = input("Enter role: ")
#         location = input("Enter location details: ")
#         w.writerow([e_id, name, role, location])
# print("All Details saved successfully")


# import csv
# with open("C:/Practice_Python_Projects/PyPractice/PractPackage/files/first_file.csv", "r", newline="") as f1:
#     r = csv.reader(f1)
#     for line in list(r):
#         for words in line:
#             print(words, "\t", end="")
#         print()


# from zipfile import *
# with ZipFile("C:/Practice_Python_Projects/PyPractice/PractPackage/files/first_zip.zip", "w", ZIP_DEFLATED) as z:
#     z.write("C:/Practice_Python_Projects/PyPractice/PractPackage/files/first_file.csv")
#     z.write("C:/Practice_Python_Projects/PyPractice/PractPackage/files/first_file.txt")
#     z.write("C:/Practice_Python_Projects/PyPractice/PractPackage/files/image.jpeg")
# print("Zipping done")


# from zipfile import *
# with ZipFile("C:/Practice_Python_Projects/PyPractice/PractPackage/files/first_zip.zip", "r", ZIP_STORED) as z:
#     f_list = z.namelist()
#     for file in f_list:
#         print("File name : ", file)


# import os
# for dirpath, dirnames, filenames in os.walk("C:/Practice_Python_Projects/PyPractice/PractPackage/"):
#     print("dirpath : ", dirpath)
#     print("dirnames : ", dirnames)
#     print("filenames : ", filenames)
#     print()

#
# import pickle
# class Employee:
#     def __init__(self, e_id, e_name, e_role):
#         self.e_id = e_id
#         self.e_name = e_name
#         self.e_role = e_role
#
#     def display(self):
#         print(self.e_id, "\t", self.e_name, "\t", self.e_role)
#
#     def disp_id(self):
#         print(self.e_id)
#
#
# with open("C:/Practice_Python_Projects/PyPractice/PractPackage/files/pickle.txt", "wb") as f1:
#     o = Employee(100, "Manoj", "QA")
#     pickle.dump(o, f1)
#     print("Dumping done")
#
# with open("C:/Practice_Python_Projects/PyPractice/PractPackage/files/pickle.txt", "rb") as f1:
#     obj = pickle.load(f1)
#     obj.display()
#     obj.disp_id()


# *********************************************** Program to Merge Mails

# with open("C:\\Practice_Python_Projects\\PyPractice\\PractPackage\\files\\names.txt", 'r') as names:
#     with open('C:\\Practice_Python_Projects\\PyPractice\\PractPackage\\files\\email_body.txt') as body:
#         b = body.read()
#         for name in names:
#             # print(b)
#             email = "Dear " + name + "\n" + b + "\n\n"
#             print(email)
#             with open("C:\\Practice_Python_Projects\\PyPractice\\PractPackage\\files\\Final_mail.txt", 'a') as final:
#                 final.write(email)


# ***************************************** Find the Size (Resolution) of a Image
# with open("C:\\Practice_Python_Projects\\PyPractice\\PractPackage\\files\\image.jpeg", "rb") as img:
#     img.seek(163)
#     a = img.read(2)
#     height = (a[0] << 8) + a[1]
#     a = img.read(2)
#     width = (a[0] << 8) + a[1]
#     print(height, width)

# *************************************** read first n lines of a file
# with open("C:\\Practice_Python_Projects\\PyPractice\\PractPackage\\files\\Final_mail.txt", "r") as file:
#     for i in range(7):
#         data = file.readline()
#         print(data)


# ************************************* program to find the longest words.
# max = 0
# max_s = ""
# with open("C:\\Practice_Python_Projects\\PyPractice\\PractPackage\\files\\Final_mail.txt", "r") as file:
#     lines = file.readlines()
#     for line in lines:
#         arry = line.split(" ")
#         for i in range(len(arry)):
#             if len(arry[i]) > max:
#                 max = len(arry[i])
#                 max_s = arry[i]
#
# print(max_s, max)

# **************************************** Count the frequency of words in a file
# d = {}
# with open("C:\\Practice_Python_Projects\\PyPractice\\PractPackage\\files\\Final_mail.txt", "r") as file:
#     lines = file.readlines()
#     for line in lines:
#         arr = line.split(" ")
#         for s in arr:
#             d[s] = d.get(s, 0) + 1
#
# print(d)

# ***************************************************** size of file
# import os
# f = os.stat("C:\\Practice_Python_Projects\\PyPractice\\PractPackage\\files\\Final_mail.txt")
# print(f.st_size)

# ***************************************************** list files
# import os
# f = "C:\\Practice_Python_Projects\\PyPractice\\PractPackage\\files\\"
# for path, subdirs, files in os.walk(f):
#     print(files)

# ********* program to combine each line from first file with the corresponding line in second file
# with open('C:\\Practice_Python_Projects\\PyPractice\\PractPackage\\files\\file1.txt', "r") as file1:
#     f1 = file1.readlines()
#     with open('C:\\Practice_Python_Projects\\PyPractice\\PractPackage\\files\\file2.txt', "r") as file2:
#         f2 = file2.readlines()
#         min = len(f1) if len(f1) < len(f2) else len(f2)
#         max = len(f1) if len(f1) > len(f2) else len(f2)
#         with open('C:\\Practice_Python_Projects\\PyPractice\\PractPackage\\files\\file_1_2_combine.txt', 'a') as op:
#             for i in range(min):
#                 k = f1[i] + " " + f2[i]
#                 op.write(k)
#             for i in range(min, max):
#                 if len(f1) > len(f2):
#                     k = f1[i]
#                     op.write(k)
#                 else:
#                     k = f2[i]
#                     op.write(k)

# ************************************************** read random line
# import random as rn
# with open('C:\\Practice_Python_Projects\\PyPractice\\PractPackage\\files\\file_1_2_combine.txt', 'r') as op:
#     data = op.readlines()
#     n = int(rn.choice(range(len(data))))
#     print(n)
#     print(data[n])


# *********************************************** file is closed or not
# f = open('C:\\Practice_Python_Projects\\PyPractice\\PractPackage\\files\\file_1_2_combine.txt', 'r')
# f.close()
# try:
#     f.read()
# except ValueError:
#     print("File is closed")
# # OR
# f = open('C:\\Practice_Python_Projects\\PyPractice\\PractPackage\\files\\file_1_2_combine.txt', 'r')
# print(f.closed)
# f.close()
# print(f.closed)


