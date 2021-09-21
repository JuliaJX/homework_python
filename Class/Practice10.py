
# class Name():
#     def __init__(self,name):
#         self.__name = name
#     def get_name(self):
#         return self.__name
#     def set_name(self, new_name):
#         self.__name = new_name
# st=Name('Ivan')

# print(st. get_name())

# class Person():
#     def __init__(self,name):
#         self.name = name
# class Name(Person):
#     def __init__(self,name):
#         self.__name = name   
#     def get_name(self):
#         return self.__name
#     def set_name(self, new_name):
#         self.__name = new_name
# class Age(Person):
#     def __init__(self,age):
#         self.__age = age
#     def get_age(self):
#         return self.__age
#     def set_age(self, new_age):
#         self.__age = new_age
# n=Name('Vanya')
# a=Age('18')
# print(n.get_name())
# print(a.get_age())

# class Person():
#     def __init__(self,name,age):
#         self.__name = name
#         self.__age = age
#     def get_name(self):
#         return self.__name
#     def set_name(self, new_name):
#         self.__name = new_name
#     def get_age(self):
#         return self.__age
#     def set_age(self, new_age):
#         self.__age = new_age
# p = Person('Vanya',12)
# print(p.get_name())
# print(p.get_age())

# class Field():
#     __pos_hare = 0
#     __pos_tort = 0
#     def __init__(self, n, m, x):
#         if n<m:
#             print('Неверные данные.')
#             return
#         self.__step_hare = n
#         self.__step_tort = m
#         self.__length = x    
#     def get_pos_hare(self):
#         return self.__pos_hare
#     def get_pos_tort(self):
#         return self.__pos_tort
#     def set_pos_hare(self, new_pos_hare):
#         self.__pos_hare=new_pos_hare
#     def set_pos_tort(self, new_pos_tort):
#         self.__pos_tort=new_pos_tort
#     def step(self):
#         hare_new_pos = self.__pos_hare + self.__step_hare
#         if hare_new_pos > self.__length:
#             hare_new_pos -= self.__length
#         self.__pos_hare = hare_new_pos

#         tort_new_pos = self.__pos_tort + self.__step_tort
#         if tort_new_pos > self.__length:
#             tort_new_pos -= self.__length
#         self.__pos_tort = tort_new_pos
# f=Field(5,2,11)
# i=0
# first_meet = 0
# while (i<100):
#     f.step()
#     i+=1
#     if f.get_pos_hare()==f.get_pos_tort():
#         print('Они встретились через', i-first_meet)
#         first_meet=i
# import random

# # n=[N]
# # {0,1,2,3,4,5,6,7,8,9}
# # N+n %2=0
# class Game():
#     def __init__(self):
#         pass
#     def play(self):
#         p = random.randrange(0, 10)
#         k=random.randrange(0, 10)
#         m=random.randrange(0, 10)
#         new_n1 = self.n1 + p
#         new_n2 = self.n2 + k
#         new_n3 = self.n3 + m
#         return new_n1, new_n2, new_n3
    
#     def play(cards):
#         table_card = random.randrange(0,10)
#         winners=[]
#         i=0
#     for card in cards:
#         if(card+table_card)%2==0:
#             winners+=1
#         i+=1
#     if len(winners)>0:
#         print('Победители: ', winners)
#     else:
#         print('Все проиграли.')
# f = Game()
# i = 0
# randomlist = []
# for i in range (0, 10):
#     n = random.randint(1, 30)
#     randomlist.append(n)
# while i < 13:
#     f.play2(randomlist)
#     i += 1

import random


class Game():
    def __init__(self):
       pass

    def play(self):
        p = random.randrange(0, 10)
    
        new_n1 = self.n1 + p
        new_n2 = self.n2 + k
        new_n3 = self.n3 + m
        return new_n1, new_n2, new_n3

    def play2(self, cards):
        cable_card = random.randrange(10)
        winners = []
        i = 0
        for card in cards:
            if(card + cable_card) % 2 == 0:
                winners.append(i)
            i += 1
        if len(winners) > 0:
            print('Победители ', winners)
        else:
            print('EВсе проиграли')

f = Game()
i = 0
randomlist = []
for i in range (0, 10):
    n = random.randint(1, 30)
    randomlist.append(n)
while i < 13:
    f.play2(randomlist)
    i += 1