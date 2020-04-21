# class Test:
#     def m1(self):
#         print("Without args")
#
#     def m1(self, a):
#         print("With 1 arga")
#
#     def m1(self, a, b):
#         print("with 2 args")
#
# t = Test()
# # t.m1()
# t.m1(12)
# t.m1(1, 3)


class Baap:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
    def display(self):
        print(self.name, "\t", self.sex)

class Beta(Baap):
    def __init__(self, name, sex, age, place):
        super().__init__(name, sex)
        self.age = age
        self.place = place

    def display_01(self):
        print(self.name, "\t", self.sex, "\t", self.age, "\t", self.place)

    def display_02(self):
        super().display()

t = Beta("Manoj", "M", 28, "Pune")
t.display()
t.display_01()
t.display_02()


t = Baap("Manoj", "M")
t.display()

