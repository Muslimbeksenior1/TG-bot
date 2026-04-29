# 1
# def tarvuz():
#     tarvuzogirligi = int(input("kilogram kirting = "))
#     if tarvuzogirligi % 2 == 0:
#         print('ha')
#     else:
#         print('yoq')
# tarvuz()


# 2


# for i in range(1987,2014):
#     katta = max(i)
#     kichik = min(i)
#     print(katta,kichik)


# 3

# def funk():
#     royhat1 = [12,12,12,123,2,32]
#     royhat2 = [12,23,2231,2,123,32]
#     royhat3 = len(royhat2)
#     royhat22 = len(royhat1)
#     if royhat1 == royhat2:
#         print('mos')
#     else:
#         print('mosmas')
# funk()


# boshqa masalalar
# 1


# def funk(a,b,c):
#     kopaytma = a*b*c
#     print(kopaytma)
# funk(2,3,4)
# 2

# def funk(a,b):
#     kopaytma = a*a
#     kopaytma2 = b*b
#     print(kopaytma,kopaytma2)
# funk(2,3)

# 3
# def mevalar(*args):
#     uzun = len(args[0])
#     for i in args:
#         if uzun < len(i):
#             uzun = len(i)
#             meva = i
#     return meva
# print(mevalar('olma','banan','mevalar','anananasa'))

# 4

# def func(*sonlar):
#     return sum(sonlar)

# print(func(1, 2, 3))



# 5
# def func(*sonlar):
#     return min(sonlar)

# print(func(1, 2, 3))

# 6

# def func(*sonlar):
#     return min(sonlar)

# print(func(1, 2, 3,23,32,12,23,21,321,21,43))

# 7

# def numbers(*args):
#     return list(set(args))

# print(numbers(1, 2, 3, 2, 4, 1, 5))



# 8

# def numbers(*args):
    
#     return (args)

# print(numbers(1, 2, 3, 2, 4, 1, 5))