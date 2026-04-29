# # 1
# # n = int(input("soni kiriting: "))
# # arry = list(map(int, input().split()))
# # kichik = min(arry)
# # a, b = map(int, input().split())

# # for i in range(n):
# #     if a-1 <= i < b:
# #         print("%.1f" % (arry[i] / kichik), end=" ")
# #     else:
# #         print("%.1f" % arry[i], end=" ")



# # 2






# # dic = {"ten":10,"twenty":20,"thirty":30}
# # dic2 = {"thirty":30,"fourty":40,"fifty":50}
# # dic1 = dic|dic2
# # print(dic1)



# # 3

# # dict = {"class":{
# #     "student":{
# #         "name":"Make",
# #         "Marks":{
# #             "physics":70,
# #             "history":80
# #         }

# #     }
# # }}
# # natija = (dict['class']["student"]["Marks"]["history"])
# # print(natija)

# # 4
# # sample_dict = { "name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
# # dict = ["name", "salary"] 
# # print(sample_dict['name'])
# # print(sample_dict['salary'])

# # 5

# # keys = {'a', 'b', 'c'}
# # valus = {100,200,300}
# # dic = dict(zip(keys,valus))
# # for i in valus:


# #     if dic == 200:
# #         print("bor")
# #     else:
# #         print("yoq")
# # 6

# # dict = { "name": "Kelly", "age":25, "salary": 8000, "city": "New york" }
# # dict1 = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New York'}
# # dict.update(dict1)
# # print(dict)

# # 7


# # sample_dict = { 'emp1': {'name': 'Jhon', 'salary': 7500}, 'emp2': {'name': 'Emma', 'salary': 8000}, 
# # 'emp3': {'name': 'Brad', 'salary': 500} }
# # for i in sample_dict.items():
# #     print(i)



# # 8

# # ist1 = ["M", "na", "i", "Ke"] 
# # list2 = ["y", "me", "s", "lly"]
# # dic = {}

# # for i in range(len(ist1)):
# #     dic.update({ist1[i]:list2[i]})
# # print(dic)

# # 9
# # list1 = [10, 20, 30, 40] 
# # list2 = [100, 200, 300, 400] 
# # list2.reverse()
# # print(dict(zip(list1,list2)))


# # 10

# # list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"] 
# # sub_list = ["h", "i", "j"] 
# # sub_list.insert(6,list1)
# # print(sub_list)

# # 11

# # List1 = [5, 10, 15, 20, 25, 50, 20]

# # if List1==List1:
# #     List1.remove(20)
# #     List1.append(200)
# #     print(List1)
# # else:
# #     print(List1)

# # 12
# # str1 = "P@#yn26at^&i5ve"
# # str = []
# # son = []
# # res = str1.isalpha
# # if res == str1.isalpha():
# #     str += 1
# #     print(str)
# # elif res == str1.isalnum():
# #     son += 1
# #     print(son)
    
# # else:
# #     print(son)
# # 1

# # dic = {'a':2,'b':3,'c':5}
# # s = 0 
# # for i in dic.values():
# #     s += i
# # print(s)


# # 2

# # dict = {'x':-1,'y':4,'t':2,'z':0}
# # s = 0
# # for i in dict.values():
# #     s += i
# # print(s)

# # 3
# # dic = {'vali':12,'ali':13,'sami':15}
# # s = 0
# # for i in dic.values():
# #     dic2 = max(dic.values())
    
# # print(dic2)



# # 4

# # dict = {'a':-1,'b':-3,}







# # from math import *



# # def Funk(a, b, c):
# #     hisobla = (2*a- b - sin(c)) / (5+abs(c)) 
# #     return hisobla

# # t, s = map(float, input().split())

# # natija = Funk(t, -2*s, 1.17) + Funk(2.2, t, s-t)

# # print("%.2f" % natija)



# # def Yosh(yil:int) -> int:
# #     siz  = 2026-yil
# #     return siz



# # yoshingiz = int(input("yoshingizni kiriting: "))
# # print(Yosh(yil=yoshingiz))


# # a = float(input("yil: "))
# # print(Yosh(a))



# # son = int(input("son: "))
# # son2 =int(input("son2: "))
# # def Raqam(son):
# #     s = 0
# #     while son != 0:
# #         s += son % 10
# #         son = son // 10
# #     return s

# # (Raqam(son=son))
# # print(Raqam(son=son2))


# # def Salom():
# #     print("Assalomu alaykum")

# # def IkkiSon(a, b):
# #     s = a + b
# #     print(s)




# # IkkiSon(a=3, b=16)
# # IkkiSon(a=21, b=16)
# # IkkiSon(a=54, b=16)

# # 1
# # def salom():
# #     print("salom dunyo")
# # salom()


# # 2

# # def salom():
# #     a = input()
    
# #     print(f"salom {a}")
# # salom()


# # 3


# # def salom():
# #     a = int(input())
# #     b = int(input())
# #     print(f"natija {a+b}")
# # salom()


# # 4


# # def salom():
# #     a = int(input())
# #     b = int(input())
# #     print(f"natija {a**b}")
# # salom()


# # 5


# # def salom():
# #     a = int(input())
# #     b = int(input())
# #     c = int(input())
# #     a1 = a + b + c
# #     a2 = a1 // 3
# #     print(f"natija {a2}")
# # salom()


# # 6

# # def salom():
# #     a = int(input())
# #     if a % 2 == 0:
# #         print("juft")
# #     else:
# #         print('toq')
# # salom()


# # 7

# # def salom():
# #     a = int(input())
# #     b = int(input())
# #     c = int(input())
# #     a1 = max(a,b,c)
    
# #     print(f"natija {a1}")
# # salom()



# # 8

# # def salom():
# #     a = str(input())
# #     b = a[::-1]
# #     if a == b:
# #         print("palindrom")
# #     else:
# #         print('palindrom emas')
# # salom()


# # 9


# # def salom():
# #     a = int(input())
# #     if a > 0:
# #         print("musbatt")
# #     elif a == 0:
# #         print("0ga teng")
# #     else:
# #         print('manfiy')
# # salom()


# # 10




# # def salom():
# #     a = int(input())
# #     if a % 400==0 and a % 4==0 and a%100==0:
# #         print('kabisa yil')
# #     else:
# #         print('kabisa yil emas')

# # salom()

# #11

# # def salom():
# #     a = str(input())
# #     b = ['a','u','e','i','o']
# #     if a in b:
# #         print("bor")
# #     else:
# #         print("yoq")

# # salom()

# # 12

# # def salom():
# #     a = ['a','b','a','s','d','w','q']
# #     l = len(a)
# #     print(l,'sm')

# # salom()

# # 13


# # def salom():
# #     a = [12,132,32,54,32,54,65]
# #     b = max(a)
# #     min3 = min(a)
# #     print(b,'- eng kattasi',min3,'- eng kichik')

# # salom()

# # 14


# # def salom():
# #     s = str(input('soz kirting - '))
# #     reverse_s = s[::-1]
# #     print(reverse_s)


# # salom()

# # 15

# # def salom():
# #     s = ['salom','dunyo','qanday','san']
# #     b = len(s)
# #     print(b,'soz bor')


# # salom()

# # 16

# # def salom():
# #     a = [12,23,21,3,54,32]
# #     yangi = []
# #     for i in a:
# #         yangi.append(i**2)
# #     print(yangi)
# # salom()

# # 17

# # def sanash():
# #     a = 'salom 124'
# #     harf = 0
# #     raqam = 0
    
# #     for i in a:
# #         if i.isalpha():
# #             harf += 1
# #         elif i.isdigit():
# #             raqam += 1
    
# #     print(raqam,'raqam soni',harf,'harf soni')
# # sanash()

# # 18

# # def salom():
# #     n = 12
# #     a = 0
# #     for i in range(1,n):
# #         if n % i == 0:
# #             a += i
# #     if a == n:
# #         print( 'mukammal')
        
# #     else:
# #         print( 'yoq')

# # salom()


# # 19


# # def salom():
# #     a = {'adw','as','buy','buy'}
# #     print(a)
# # salom()

# # 20


# # def salom():
# #     a = ['salom','uzun','yaqin','zor']
# #     a.sort()
# #     print(a)
# # salom()

# # 21

# # def Yosh(yil:int) -> int:
# #     siz  = 2026-yil
# #     return siz



# # yoshingiz = int(input("yoshingizni kiriting: "))
# # print(Yosh(yil=yoshingiz))


# # a = float(input("yil: "))
# # print(Yosh(a))

# # 22
# # def salom():
# #     a = int(input('son krting - '))
# #     b = a**2
# #     kub = a**3
# #     print(a,'kvadrat',kub,'kubi')
# # salom()

# # 23

# # def salom():
# #     a = int(input('son krting - '))
# #     if a % 2==0:
# #         print('juft')
# #     else:
# #         print("toq")
# # salom()

# # 24

# # def salom():
# #     a,b = map(int,input().split())
# #     b1 = max(a,b)
# #     print(b1)
# # salom()

# # 25

# # def salom():
# #     y,x = map(int,input().split())
# #     12 == y
# #     print(x)
# # salom()




# def parolnitop(p,*ags):
#     n = 0
#     for i in ags:
#         if i in p:
#             n = 1
#     return True if n else False

#     # savat = 0
#     # user = int(input('parol kirting - '))
#     # for i in user:
#     #     if ags in user:
#     #         savat += i
#     #         print("kirishingiz mumkin!!!")
#     #     else:
#     #         print("False")

# print(parolnitop("Aalex1234",'@','5','a'))



# # 1
# # def salom(*ags):
    
# #     savat = max(ags)
# #     print(savat)
# # salom(12,321,43,23,321)




