# 1
# n = int(input("Son kiriting - "))

# yigindi = 0

# for i in str(n):
#     yigindi += int(i)

# natija = n + yigindi

# print("javob:", natija)


# # 2

# n = int(input("Son kiriting - "))

# i = 2
# tub = "Tub"

# while i < n:
#     if n % i == 0:
#         tub = "tub emas"
#         break
#     i += 1

# if n > 1 and tub:
#     print(n * 2)
# else:
#     print(n)

# 3

# def Funk(a:list):
#     lis = []
#     for i in a:
#         if i % 3 == 0:
#             lis.append(i)
#     if len(lis) == 0:
#         return 0
#     else:
#         return lis
# son = int(input('son kirting - '))
# print(Funk([son]))

# 4


# son = float(input('son kirting - '))
# print(round(son))

# 5

# son = int(input('son kirting - '))
# son2 = str(son)
# son3 = son2[::-1]
# print(son3)

# 6

# a = int(input('son kirting - '))
# if a < 0:
#     print(a-a-a)
    
# else:
#     print(a)

# 7

# n = int(input('son kirting - '))
# raqamlar = [int(r) for r in str(n)]
# katta = max(raqamlar)
# natijasi = n + katta
# print(natijasi)

# 8

# n = int(input('son kiriting - '))
# if str(n) == str(n)[::-1]:
#     n+= 1
# print(n)

# 9

# n = 123
# son = len(str(n))
# print(son+n)

# 10

# a = int(input('son kirting - '))
# if a % 2 ==0:
#     print(a)
# else:
#     print(a*3)

# 11

# N = int(input("son - "))

# for i in range(1, N+1):
#     if i % 3 == 0:
#         print(i, end=" ")

# 12

# N = int(input())

# for i in range(1, N+1):
#     s = 0
#     x = i
#     while x > 0:
#         s += x % 10
#         x //= 10
#     if s % 2 == 0:
#         print(i, end=" ")

# 13

# N = int(input())

# for i in range(N, 1, -1):
#     tub = True
#     for j in range(2, i):
#         if i % j == 0:
#             tub = False
#             break
#     if tub:
#         print(i, end=" ")

# 14

# nums = input().split()
# for n in nums:
#     s = 0
#     for d in n:
#         s += int(d)
#     print(s, end=" ")

# 15

N = int(input())

for i in range(1, N+1):
    if str(i) == str(i)[::-1]:
        print(i, end=" ")