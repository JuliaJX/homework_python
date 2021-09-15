# set()
# list_= [1,1,2,2,3,3,4,4]
# set(list_)
# print(set(list_))

# set('aabbbffhh')
# print(set('aabbbffhh'))

# set_1={1,2,3,4,5,6}
# set_2={4,5,6,7,8,9}
# print(set_1.isdisjoint(set_2))

# set_1={1,2,3,4,5,6}
# set_2={4,5,6,7,8,9}
# print(set_1 | set_2) (set.union(set_2))

# set_1={1,2,3,4,5,6}
# set_2={4,5,6,7,8,9}
# print(set_1 - set_2)

# set_1={1,2,3,4,5,6}
# set_2={4,5,6,7,8,9}
# print(set.intersection(set_2))

# set_1={1,2,3,4,5,6}
# set_2={4,5,6,7,8,9}
# print(set_1 == set_2)

# set_1={1,2,3,4,5,6}
# set_2={4,5,6,7,8,9}
# print(set_1.symmetric_difference(set_2)) (set_1 ^ set_2)

# set_1={1,2,3,4,5,6}
# set_2={4,5,6,7,8,9}
# print(set_1.issubset(set_2)) (set_1 <= set_2)

# set_1={1,2,3,4,5,6}
# set_2={4,5,6,7,8,9}
# print(set_1.issuperset(set_2)) (set_1 >= set_2)

# set_1={1,2,3,4,5,6}
# set_2={4,5,6,7,8,9}
# set_3= set_1.copy() 
# print(set_3)

# set_1={1,2,3,4,5,6}
# set_2={4,5,6,7,8,9}
# set.update(set_2)
# print(set_2)

# set_1={1,2,3,4,5,6}
# set_2={4,5,6,7,8,9}
# set_3=set_1.copy()
# set.intersection_update(set_2, set_3)
# print(set_3)

# set_1={1,2,3,4,5,6}
# set_2={4,5,6,7,8,9}
# set_1.difference_update(set_2)
# print(set_2)

# set_1={1,2,3,4,5,6}
# set_2={4,5,6,7,8,9}
# set_2.add(10)
# print(set_2)

# set_1={1,2,3,4,5,6}
# set_2={4,5,6,7,8,9}
# set_1.remove(1)
# print(set_1)

# s=[1,2,2,2,3,4,4,5,6] 
# def unique(s):
#     return list(set(s))

# print(unique(s))

# Я сделала так:
# s=[1,2,3,4,4,4,4,5,6,6,6]
# def unique(s):
#     set(s)
#     return list(set(s))
# print(list(set(s)))

a=[1,2,2,2,3,4,5,5,5,6,7]
b=[5,6,7,8,9,9,9,10,11,11,12]
def intersection_lists(a, b):
    return set(a).intersection(set(b))

print(list(set(a).intersection(set(b))))




