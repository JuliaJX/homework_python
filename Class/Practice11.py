# def f(n):
#     print(n)
#     if n>0:
#         f(n-1)
# print(f(50))

# def max(n, m):
#     if n > m:
#         return n
#     else:
#         return m

# print(max(3, 5))

# def factorial(n):
#     res = 1
#     for i in range(1, n + 1):
#         res *= i
#     return res

# print(factorial(3)) мой вариант

# def factorial(n):
#     if n==0:
#         return 1
#     elif n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(3))

# def dividers(n, div=1, all_divs=[]):
#     if n==div:
#         all_divs.append(div)
#         return all_divs
#     elif div<n:
#         if n%div==0:
#             all_divs.append(div)
#         return dividers(n, div=div+1, all_divs=all_divs)
#     else:
#         print('Неверное n')
# print(dividers(10))

   
# n=int(input())
# s=str(n)
# def div(n,s):
    
#         div (n,z-1)
#         print (n)
        
# print (div(n,z))




def order(n):
    res = [int(x) for x in str(n)]
    return res

def order1(n):
    if len(n) == 1:
        return 1
    else:
        print(-n)
        order1(n-1)
        print(n)
n=str(input())