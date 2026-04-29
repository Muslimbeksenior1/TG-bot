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



# 62 algo
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








# 62 
# from math import *

# n = int(input())

# i = 1
# s = 0

# while i <= n:
#     s += (-1)**(i-1) * (sin(i**i)) / (2**i)
#     i += 1
# print("%.2f" % s)
# 63

# from math import *
# n = int(input())
# i  = 1
# s = 0
# while i <= n:
#     s+= ((-1)**(i**2))* (1)/ (2*n-1)
#     print("%.4f" % s)
#     break


# 64

# from math import *
# s = 0
# x = 1
# s = 1                                               
# x,s = (input().split())
