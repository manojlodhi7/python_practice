# class Employee:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#
#     def display(self):
#         print(self.id, "--------", self.name)
#
#
# o = Employee(12, "Manoj")
# o.display()
# o = Employee(14, "Kumar")
# o.display()


# class Employee:
#     st = 100
#
#     def __init__(self):
#         self.a = 10
#         self.b = 20
#
#     def m1(self):
#         self.c = 30
#         self.d = 40
#
#
# t = Employee()
# print("t  :", t.st)
# t.st = 55
# print("t  :", t.st)
# t2 = Employee
# print("t2 :", t2.st)
# Employee.st = 66
# del t.st
# print("t  :", t.st)
# print("t2 :", t2.st)


#
# class Test:
#     a1 = 100
#
#     def __init__(self):
#         self.b = 20
#         Test.a2 = 200
#
#     def m1(self):
#         self.c = 30
#         Test.a3 = 300
#
# print("Befor object creation Test.__dict__ : ", Test.__dict__)
# t1 = Test()
# t1.m1()
# print("After object creation Test.__dict__ : ", Test.__dict__)
#
#
# print("After object creation t1.__dict__ : ", t1.__dict__)
#
# Test.a1 = 500
# Test.a2 = 600
# Test.a3 = 700
# print("After value update Test.__dict__ : ", Test.__dict__)
#
# print("t1.a1 : ", t1.a1)
# print("Before value update t1.__dict__ : ", t1.__dict__)
# t1.a1 += 50
# t1.a2 = 60
# t1.a3 = 70
# print("After value update t1.__dict__ : ", t1.__dict__)
# print("After value update Test.__dict__ : ", Test.__dict__)


# class Test:
#     a = 10
#     def __init__(self):
#         self.b = 20
#
#     @classmethod
#     def m1(cls):
#         cls.a = 50
#         cls.b = 60
#         # del cls.b
#
#
# t1 = Test()
# t2 = Test()
# t1.m1() # Here m1 method updates static var permanently
# print(t1.a, t1.b)  # 50 20
# print(t2.a, t2.b)  # 50 20
# print(Test.a, Test.b)  # 50 60
# # del Test.a
# print(t1.a, t1.b)
# del t1.a  # cannot delete static var with objecr reference or self



# class Test:
#     count = 0
#     def __init__(self):
#         Test.count += 1
#
#     @classmethod
#     def m1(cls):
#         print(cls.count)
#
# t1 = Test()
# t2 = Test()
# Test.m1()
# t3 = Test()
# Test.m1()


# class Test1:
#     def __init__(self, ids, name, sal):
#         self.ids = ids
#         self.name = name
#         self.sal = sal
#
#     def display(self):
#         print(self.ids, "\t", self.name, "\t", self.sal)
#
#
# class Test2:
#     def modify(emp):
#         emp.sal = emp.sal + 1000
#         emp.display()
#
# e = Test1(1, "Manoj", 2000)
# Test2.modify(e)