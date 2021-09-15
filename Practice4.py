
# import string
# import random
# from random import choice

# def create_num(width):
#     s=''
#     for i in range(width):
#         c = random.choice(string.ascii_letters)
#         s+=c
#     return s

# print(create_num(9))

# import string
# import random
# from random import choice
# def count_str(s):
#     big=0
#     small=0
#     for sym in s:
#         if sum.isupper():
#             big+=1
#         else:
#             small+=1
#     if big>small:
#         return 1
#     elif small>big:
#         return 0
#     else:
#         return -1

# return [create_str(width) for i in range(num)]


def gen_name(name,num):
    i= 1
    while i <num:
        yield name 
        i+=1


ranger= gen_name('Линдси', 40)
ranger2= gen_name('Армен', 40)
ranger3= gen_name('Инга', 40)
names= [x for x in ranger]
names2= [x for x in ranger2]
names3= [x for x in ranger3]
print(names)
print(names2)
print(names3)