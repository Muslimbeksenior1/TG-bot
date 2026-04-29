# lis = [12, 21, 36, 71, 24, 85, 12, 30, 25]
# del lis[5]
# print(lis)
# # lis.pop(5)
# katta = max(lis)
# print(katta)

# katta = lis[0]

# for i in lis:
#     if katta < i:
#         katta = i
# print(katta)



# arry = list(map(int, input().split()))



# print(arry)











# ismlar = ["Ali", "Vali", "Guli", "Bek"]

# ismlar.insert(2, "Alisher")
# print(len(ismlar))


# yangi_qol = ismlar[1]
# ismlar[1] = ismlar[3]
# ismlar[3] = yangi_qol

# print(ismlar)



# a = ismlar.index("Guli")
# print(a)


# ismlar[2] = "Alisher"
# print(ismlar)







# print(ismlar[2])

# ism = input("ism: ")

# ismlar.append(ism)

# print(ismlar)


# lis = [2, 5, 7, 9, 12, "salom", 'Hayr', True, False, 4.6, 5.9, 5+6j]


# print(lis)













# from math import factorial as ff

# n, x = map(int, input().split())

# i = 1
# s = 0

# while i <= n:
#     s += ((-1)**(i-1) * x ** (2*i-2)) / (ff(2*i-2))
#     i += 1

# print("%.3f" % s)

# lis =  [6, 25, 91, 23, 72, 9, 18, 6]
# soni = 0
# s = 0
# for i in lis:
#     soni += 1
#     s += i
# print(s / soni)


# n = 5
# array=[1,2,3,7,4] 
# pustoy_list = []
# for i in array:
#     for j in array:
#         s = i + j
#         if not j in pustoy_list:
#             if s == n:
#                 pustoy_list.append(i)
#                 print(f"{i} + {j} = {n}")




# 1
# foundition = {"masharipov","muslimbek",'Jovoghuiir',"JAhongiz"}
# phyton = {"masharipov","muslimbek","LOL"}
# lol = phyton.intersection(foundition)
# print(lol)

# 2

# foundition = {"masharipov","muslimbek",'Jovoghuiir',"JAhongiz"}

# print(len(foundition)**2)


# 3

# foundition = {"masharipov","muslimbek",'Jovoghuiir',"JAhongiz"}
# phyton = {"masharipov","muslimbek","LOL"}
# lol = phyton.intersection(foundition)
# print(lol)

# 4

# sonlar = {2,3,1,4,5,3,2}
# b = []
# for i in sonlar:
#     b.append(i**2)
# print(set(b))

# 5

# foundition = {"masharipov","muslimbek",'Jovoghuiir',"JAhongiz"}
# phyton = {"masharipov","muslimbek","LOL"}
# lpl = foundition.union(phyton)
# print(lpl)


# 6

# foundition = {"masharipov","muslimbek",'Jovoghuiir',"JAhongiz"}
# phyton = {"masharipov","muslimbek","LOL"}
# lol = phyton.intersection(foundition)
# print(lol)

# 7
# foundition = {"masharipov","muslimbek",'Jovoghuiir',"JAhongiz"}
# phyton = {"LOL","lola"}

# lol = foundition.difference(phyton)
# print(lol)


# 8

# foundition = {"masharipov","muslimbek",'Jovoghuiir',"JAhongiz"}
# phyton = {"LOL","lola","masharipov"}
# lola =phyton.intersection(foundition)
# print(lola)


# 9

# foundition = {"masharipov","muslimbek",'Jovoghuiir',"JAhongiz"}
# lol = list(foundition)
# de = len(lol)
# if de > 0:
#     print('ichida bor')
# else:
#     print("BOSh SET")

#10

# foundition = {"masharipov","muslimbek",'Jovoghuiir',"JAhongiz"}
# lol = list(foundition)
# de = len(lol)
# if de > 0:
#     print('ichida bor ',de+2)
# else:
#     print("BOSh SET")















# mevalar = ["orik", 'shaftoli', 'anor', 'olma', 'banan']
# narxlar = [5000, 6000, 10000, 100000, 25000]

# savat = []
# savat_kg = [] 
# savat_p = []

# print("Do'konimizga Xush kelibsiz\n")
# while True:
#     for i in range(len(mevalar)):
#         print(mevalar[i], "->", narxlar[i], 'so\'m')

#     user = input("meva tanlang: ")

#     if user == "yoq":
#         print("Do'konimizga kelib trung")
#         break

#     if user in mevalar:
#         user_kg = float(input("kg kiriting: "))
#         savat.append(user)
#         savat_p.append(narxlar[mevalar.index(user)])
#         savat_kg.append(user_kg)
#     else:
#         print("siz so'ragan meva yo'q ‼️‼️‼️")
# jami = 0
# print("\nSizning Xaridingiz\n")
# for j in range(len(savat)):
#     print(f"| {savat[j]}      |   {savat_kg[j]} kg  |  {savat_p[j]}  so'm")
#     jami += savat_p[j] * savat_kg[j]

# print(f"Sizdan {jami} so'm bo'ldi")


keys = ['Ten', 'Twenty', 'Thirty']

values = [10, 20, 30]
print(dict(zip(keys,values)))
# dic = {}

# for i in range(len(keys)):
#     dic.update({keys[i]:values[i]})

# print(dic)


# dic = {'hello':'Salom', 'Good bye':'xayr', 'black':'qora', 'one':1}


# for i, j in dic.items():
#     print(i, j)




# dic = {'phone':'samsung', 'phone':'redmi', 'color':"dark", 'telefon':'iphone'}

# print(dic)

# dic = {
#     'car':{
#     'chevralet':['matiz', 'coablat', 'muliba'],
#     'color':('green', 'yellow', 'blue', 'dark'),
# },
#     'phone':{
#         'apple':'iphone 13 pro',
#         'samsung': 's25 ultra'
#     }
# }
# print(dic['phone']['samsung'])
# print(dic['car']['chevralet'][1])


# print(len(dic))
