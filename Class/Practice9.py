# class Summator():
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def return_sum(self):
#         return self.a + self.b
# s=Summator(1,3)
# s.return_sum()

# print(s.return_sum())


# class Car():
#     def __init__(self):
#         pass
#     def what_is_this(self):
#         print('I am a car')
# class Pink_car(Car):
#     def what_color(self):
#         print('Pink')
# car=Car()
# pink_car=Pink_car()
# pink_car.what_is_this()
# pink_car.what_color()


# class Person():
#     def __init__(self,name):
#         self.name = name
#     def exclaim(self):
#         print('Я человек с именем', self.name)
# class Student(Person):
#     def exclaim(self):
#         print('Я человек с именем', self.name, 'но я хочу спать больше.')
# p=Person('Vanya')
# s=Student('Vanya')
# p.exclaim()
# s.exclaim()

# class Person():
#     def __init__(self,name):
#         self.name = name
#     def exclaim(self):
#         print('Я человек с именем', self.name)
# class Student(Person):
#     def exclaim(self):
#         print('Я человек с именем', self.name, 'но я хочу спать больше.')
#     def __del__(self):
#         print('Удалён обьект', self)

# p=Person('Vanya')
# s=Student('Vanya')
# s.__del__()
# p.exclaim()
# s.exclaim()

# print(isinstance(s,Student))
# print(issubclass(Student, Person))

# class Person():
#     def __init__(self, name):
#         self.name = name
# class Student:
#     homework = 0
#     kn = 0
#     def get_kn(self):
#         self.kn += 1
#     def get_homework(self, n):
#         self.homework += n
#     def do_homework(self):
#         if self.homework > 0:
#             self.homework -= 1
#             self.kn += 1
#         else:
#             print('Нечего делать')
# class Teacher():
#     work = 0
#     def give_kn(self,*pupils):
#         for pupil in pupils:
#             pupil.get_kn()
#             self.work += 1
#     def give_homework(self, *pupils, n):
#         for pupil in pupils:
#             pupil.get_homework(n)
#             self.work += 1
# t=Teacher('Татьяна Константиновна')
# p=[Student('Виноградова Юлия') for p in range(n)]
# t.give_kn(p)
# print (


# class Rectangle():
#     def __init__(self,w, h):
#         self.w = w
#         self.h = h
#     def ger_p(self):
#         return (self.w + self.h)*2
#     def get_s(self):
#             return self.w * self.h
# r=Rectangle(4,5)
# print(r.ger_s())

# import math
# class Circle():
#     def __init__(self,r):
#         self.r = r
#         p=math.pi
#         self.p = p
#     def get_d(self):
#         return 2*self.p*self.r
#     def get_s(self):
#         return self.p*self.r*self.r
# c=Circle(8)
# print(c.get_s())

import math
class Triangle():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        p=(a+b+c)/2
        self.p = p
    def get_per(self):
        return self.a + self.b + self.c
    def get_s(self):
        return math.sqrt(self.p*(self.p-self.a)*(self.p-self.b)*(self.p-self.c))
t=Triangle(5, 6, 7)
print(t.get_s())
    
