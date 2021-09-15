# f={}
# d={'Hello': 15,
# 'World':10}


# print(d.values())

#   f={}
#   d={'Hello': 15,
#   'World':10}

#   d['I']=15
#   print(d['I'])




#  def get_value(d, k):

#      if k in d.keys():
#          print(d[k])
#          return d[k]
        
#      else:
#          print('Нет такого')
#          return -1

#  def get_values(d,k):
#      return d.get(k,-1)

# def ascii_upper():
#     d ={}
#     for i in range(65, 91):
#         d[chr(i)] = i
#     return d

# #2  вариант return {chr(i): i for i in range(65,91)}

# print(ascii_upper())

# import string
# def counter_letters(s):
#     d={}
#     for ch in string.ascii_lowercase:
#         d[ch]= s.count(ch)

#     return d

# print()



# def create_city(p,s):
#     return {'population':p,
#              'size':s}
 
# def create_region(names,cities):
#     d={}
#     for name, city in zip(names,cities):
#         d[name] = city,
#     return d
# names=[]
# cities=[]
# i=0
# while i<3:
#     name = input ('Введите название города: ')
#     population = input ('Введите население: ')
#     size = input ('Введите размер: ')
#     cities.append(create_city(population,size))
#     names.append(name)
#     i+=1

# def {}
# d={'key1': 1,
# 'key2': 3,
# 'key3': 2}