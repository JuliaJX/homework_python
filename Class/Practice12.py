# class Person():
#     def __init__(self, name, age,height, weight):
#         self.name = name
#         self.age = age
#         self.height = height
#         self.weight = weight
# class Student(Person):
#     def __init__(self, name,age, height, weight,study):
#         self.study = study
#         super().__init__(name, age, height, weight)



# class Name():
#     def __init__(self, name):
#         self.__hidden_name=name
#     def get_name(self):
#         print('getter')
#         return self.__hidden_name
#     def set_name(self, name):
#         print('setter')
#         self.__hidden_name=name
#     name = property(get_name, set_name)
# n=Name('Саша')
# n.name='Надя'
# print(n.name)

# class Counter():
#     __hidden_counter=0
#     def count(self):
#         self.__hidden_counter+=1
#     def counret_to_zero(self):
#        self.__hidden_counter=0
#     def get(self):
#         return self.__hidden_counter
#     def set(self, n):
#         self.__hidden_counter=n
# c=Counter()
# c.count()
# print(c.get())




# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# class Parent(Person):
#     def __init__(self, name, age, hair, eyes):
#         super().__init__(name, age)
#         self.hair=hair
#         self.eyes = eyes
# import random
# class Child(Person):
#     def __init__(self, name, age, parent1,parent2):
#         super().__init__(name, age)
#         hair_1, eyes_1= parent1.hair, parent1.eyes
#         hair_2, eyes_2=parent2.hair,parent2.eyes
#         self.hair=random.choice([hair_1, hair_2])
#         self.eyes=random.choice([eyes_1, eyes_2])
# p1=Parent('Вильям', '42 года', 'глаза голубые', 'волосы чёрные')
# p2=Parent('Мира', '36 лет','глаза карие', 'волосы рыжие')
# child=Child('Эбигейл', '8 лет', p1,p2)
# print(child.name,child.age, child.hair, child.eyes)

# import random
# class Car():
#     type='Car'
#     def __init__(self,speed):
#         self.speed = speed
# class Mercedes(Car):
#     model = 'Mercedes'
#     def __init__(self,speed):
#         super().__init__(speed)
# class BMV(Car):
#     model='BMV'
#     def __init__(self,speed):
#         super().__init__(speed)
# class Porshe(Car):
#     model= 'Porshe'
#     def __init__(self,speed):
#         super().__init__(speed)

# Mercedes = Mercedes(270)
# BMV = BMV(300)
# Porshe = Porshe(320)
# finish=1000
# pos_m=0
# pos_b=0
# pos_p=0
# while pos_m< finish and pos_b<finish and pos_p<finish:
#     pos_m+=Mercedes.speed
#     pos_b+=BMV.speed
#     pos_p+=Porshe.speed 
# if pos_p>pos_b:
#     print('Porshe!')
# elif pos_b>pos_m:
#     print ('BMV!')
# else:
#     print('Mersedes!')

# import keyword
# class Person():
#     def __init__(self, name):
#         self.name = name
#     def say(self, text):
#         print(self.name, ': ', text)
# p1=Person('Anna')
# p2=Person('Ivan')
# first=True
# for word in keyword.kwlist:
    
#     if first:
#         p1.say(word)
        
#     else:
#         p2.say(word)
#     first= not first

class Reader():
    books=[]
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age   
    def take_book(self, book):
        if len(self.books)<2:
            self.books.append('book')
        else:
            print('Nononononoooo')
    def return_book(self, book):
        if book in books:
            self.books.remove(book)
        else:
            print('No book')
h=0
while True:
    l = input ('Взять книгу?(q)')
    if l == 'q':
        break
    x= int(input('Берём книгу:'))