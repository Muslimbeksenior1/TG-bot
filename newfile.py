# # def fibanachu(n):
# #     if n == 1 or n ==2:
# #         return 1
# #     else:
# #         return fibanachu(n-1) + fibanachu(n-2)
# # n = int(input('son kirting - '))
# # print(fibanachu(n))



# from random import choice, randint, randrange, shuffle

# kompyuter_achko = 0
# user_achko = 0
# for i in range(5):
#     top = ["ong", 'orta', 'chap']

#     kompyuter_v = choice(top)

#     user_t = input("topni teping ⚽️: ")

#     if kompyuter_v == user_t:
#         print("Seyf")
#     else:
#         print("Goal")
#         user_achko += 1

#     user_v = input(f"{top}\ntopni qaytaring:")

#     kompyuter_t = choice(top)

#     if kompyuter_t == user_v:
#         print("Seyf User")
#     else:
#         print("Goal")
#         kompyuter_achko += 1
    

# print(f"shot user {user_achko} kompyuter achko {kompyuter_achko}")
# if user_achko == kompyuter_achko:
#     print('hisob teng')
#     kompyuter_achko = 0
# user_achko = 0
# for i in range(5):
#     top = ["ong", 'orta', 'chap']

#     kompyuter_v = choice(top)

#     user_t = input("topni teping ⚽️: ")

#     if kompyuter_v == user_t:
#         print("Seyf")
#     else:
#         print("Goal")
#         user_achko += 1

#     user_v = input(f"{top}\ntopni qaytaring:")

#     kompyuter_t = choice(top)

#     if kompyuter_t == user_v:
#         print("Seyf User")
#     else:
#         print("Goal")
#         kompyuter_achko += 1


# user_son = int(input("son o'yladim"))
# cnt1 = 0
# while True:
#     kompyuter_son = randint(1, 100)
#     cnt1 += 1
#     if kompyuter_son == user_son:
#         print("TOpdingiz Kompyuter", kompyuter_son)
#         break
# print("urinishlar", cnt1)


# kompyuter = randint(1, 100)
# cnt = 0
# print("Kompyuter son o'yladim")
# while True:
#     user = int(input("soni kiriting: "))
#     cnt += 1
#     if user == kompyuter:
#         print("topdiz")
#         break
#     elif user > kompyuter:
#         print("siz katta son kiritdingiz")
#     else:
#         print("siz kichik son kiritdingiz")

# print("urinishlar", cnt)


# ismlar = ["Azizbek", "Amirxon", "Yoqubek", "Muslimbek", "Umrbek"]
# shuffle(ismlar)
# print(ismlar)

# son = randint(2, 19)
# son = randrange(1, 19, 2)

# print(son)

# ismlar = ["Azizbek", "Amirxon", "Yoqubek", "Muslimbek", "Umrbek"]

# tasodifiy = choice(ismlar)

# print(tasodifiy)


# def Factarial(son):
#     if son == 0 or son == 1:
#         return 1
#     else:
#        return (son * Factarial(son-1))

# n = int(input("son: "))
# print(Factarial(n))



# def Fibonachi(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return Fibonachi(n-1) + Fibonachi(n-2)
    

# n = int(input("son: "))
# print(Fibonachi(n))

# def Sonlar(l:list):
#     return [i for i in l if i % 2 == 0]

# def Funk(**kwargs):
#     a = []
#     for i, j in kwargs.items():
#         if isinstance(j, str) and j == "":
#             a.append(str(i))
#     return a


# print(Funk(a="", b=5, c="", d="salom"))


# def Funk(*args):
#     for i in args:
#         if i < 0:
#             return "Manfiy bor"
#     else:
#         return "Musbat bor"
# print(Funk(2, 6, 5))


# 1
# a = int(input('1chi sonni kirting - '))
# b = int(input('2chi  sonni kirting - '))
# print('qoshish 1','ayrish 2','kopaytirish 3','bolish 4')
# print('nima qilasiz?')
# belgi = int(input('>>>'))
# if belgi==1:
#     javob=a+b
#     print(javob)
# elif belgi==2:
#     javob1 = a-b
#     print(javob1)
# elif belgi==3:
#     javob3 = a*b
#     print(javob3)
# else:
#     javob4 = a%b
#     print(javob4)



# 2

# a = int(input('1chi sonni kirting - '))
# print('qoshish 1','ayrish 2','kopaytirish 3','bolish 4')
# print('nima qilasiz?')
# belgi = int(input('>>>'))
# b = int(input('2chi  sonni kirting - '))
# if belgi==1:
#     javob=a+b
#     print(javob)
# elif belgi==2:
#     javob1 = a-b
#     print(javob1)
# elif belgi==3:
#     javob3 = a*b
#     print(javob3)
# else:
#     javob4 = a%bs
#     print(javob4)

# 3
# def birinch(matnlar):
#     return [matn.capitalize() for matn in matnlar]
# royxat = ['alpomish','sonlar','ikkita','chiroq']
# print(birinch(royxat))




