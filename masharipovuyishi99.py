# 1
# a = 98
# b = 9
# e = 8
# k = max(a,b,e)
# h = min(a,b,e)
# print(k,h)

# 2

# a = 23
# if a % 2 == 0 and a > 0:
#     print('son juft va musbat')
# else:
#     print('son toq')


# 3

# a = 78
# if a >90:
#     print('A')
# elif a <90 and a > 80:
#     print('B')
# elif a < 80 and a > 70:
#     print('C')
# elif 70 > a > 60:
#     print('D')
# elif 60 > a > 50:
#     print('D')
# else:
#     print('F')

# 4

# a = int(input('yoshingin=zni krting  - '))
# if 0 < a < 6:
#     print('bogcha')
# elif 7 < a < 17:
#     print('maktab')
# elif 18 < a < 22:
#     print('talaba')
# else:
#     print('katalar')

# 5

# a = int(input('son krting  - '))

# n = int(input('son krting  - '))
# f = int(input('son krting  - '))

# if a > n > f:
#     print(a,n,f)
# elif a > f > n:
#     print(a,f,n)
# elif f > a > n:
#     print(f,a,n)
# elif f > n > a:
#     print(f,n,a)
# elif n > f > a:
#     print(n , f, a)
# else:
#     print(n , a , f)

# 6
# n = int(input('son krting  - '))
# parol   = int(1234)
# if parol == n:
#     print('hush kelibsiz')
# else:
#     print('tur yoqal')

# 7

# n = int(input('son krting  - '))
# if n % 100==0 and n % 4 ==0:
#     print('yil kabisa')
# else:
#     print('kabisa yilmas')

# 8
# n = int(input('son krting  - '))

# if 0 < n < 6:
#     print('tun')
# elif 7 < n < 12:
#     print('tong')
# elif 13 < n < 18 :
#     print("kunduz")
# else:
#     print("kech")



# 9

# n = int(input('son krting  - '))
# h = int(input('son krting  - '))
# g = int(input('son krting  - '))
# if n+h>g:
#     print('uchburchak')
# else:
#     print('uchberchak emas')


# 10

# a = int(input('son krting  - '))
# b = int(input('son krting  - '))
# c = int(input('son krting  - '))
# if a == b == c:
#     print('teng tomonli uchburchak')
# elif a == b < c:
#     print('tengh yonli ')
# elif a > b > c:
#     print('turli tomonli')
# else:
#     print('turli tomonli')

# 13

# n = int(input('havo haroratni krting  - '))
# if n < 0:
#     print('sovuq')
# elif 0 < n < 15:
#     print('salqin')
# elif 17 < n < 30:
#     print('iliq')
# else:
#     print('issiq')



# while True:
#     print(1)


# # 79 algo

# from math import *

# a = int(input())

# x = -pi/2
# s = 0
# while x <= pi:
#     s += pow((a**a), (1/3)) + x**2 * cos(a*x)
#     x += pi / 19
# print("%.2f" % s)

# # 66 algo
# from math import *

# n, x = map(int, input().split())

# i = 1
# s = 0
# while i <=n:
#     s += (-1)**(i-1) * 1/i * sin(i*x)
#     i += 1
# print("%.3f" % s)



## 62 algo
# from math import *

# n = int(input())

# i = 1
# s = 0

# while i <= n:
#     s += (-1)**(i-1) * (sin(i**i)) / (2**i)
#     i += 1
# print("%.2f" % s)


# n = int(input("soni kiriting: "))
# juft = 0
# toq = 0
# raqam = 0
# while n != 0: 
#     s = n % 10 
#     n = n // 10
#     if s % 2 == 0:
#         juft += 1
#     else:
#         toq += 1
#     raqam += 1

# print("raqam", raqam, 'juft', juft, 'toq', toq)


# s = 0
# while True: 
#     xoxlagancha = int(input("soni kiriting: "))
#     if xoxlagancha > 0:
#         s += xoxlagancha
#     elif xoxlagancha < 0:
#         s -= xoxlagancha
#     else:
#         break

# print(s)

# i = 1
# musbat = 0
# manfiy = 0
# nol = 0
# while i <= 10:
#     son = int(input("son kiriting: "))
#     if son > 0:
#         musbat += 1
#     elif son < 0:
#         manfiy += 1
#     else:
#         nol += 1
#     i += 1
# print("musbat",musbat)
# print("manfiy",manfiy)
# print("nol",nol)

# n = int(input("soni kiriting: "))
# s = 0
# while n != 0: 
#     s += n % 10 
#     n = n // 10 
# print(s)


# n = int(input("soni kiriting: "))
# i = 2
# while i < n:
#     if n % i == 0:
#         print("tub son emasiz")
#         break
#     i += 1
# else:    
#     if n == 1:
#         print("siz son emasiz ")
#     else:
#         print("tub son")

# i = 1
# while i <= n:
#     print(i)
#     i += 2


# while True:
#     print("Assalomu alaykum")



# for i in range(1, 15, 3):
#     print(i)

# i = 1
# while i < 15:
#     i += 1.5
#     print(i)
