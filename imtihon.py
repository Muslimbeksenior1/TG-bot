# 1
# class PrimeNumber:
#     def tekshir(self,n):
#         def tub(x):
#             if x<2: return False
#             for i in range(2,int(x**0.5)+1):
#                 if x%i==0: return False
#             return True
        
#         a=n-1
#         while not tub(a): a-=1
#         b=n+1
#         while not tub(b): b+=1
        
#         if tub(n):
#             return [a,n,b]
#         else:
#             return [a,b]

# p=PrimeNumber()
# print(p.tekshir(11))
# print(p.tekshir(12))

# 2

# class CustomList:
#     def __init__(self,l):
#         self.l = l

#     def unique_sort(self):
#         return sorted(list(set(self.l)), reverse=True)

# c = CustomList([3,5,3,2,7,5])
# print(c.unique_sort())

# 3

# class Triangle:
#     def __init__(self,a,b,c):
#         self.a,self.b,self.c = a,b,c

#     def check(self):
#         a,b,c = self.a,self.b,self.c
#         if a+b>c and a+c>b and b+c>a:
#             if a==b==c:
#                 return "teng tomonli"
#             elif a==b or b==c or a==c:
#                 return "teng yonli"
#             else:
#                 return "turli tomonli"
#         return "uchburchak yasab bo'lmaydi"

# t = Triangle(3,3,3)
# print(t.check())




# 4


# class NumberOperations:

#     def __init__(self, n):
#         self.n = n

#     def teskari(self):
#         s = str(self.n)[::-1]
#         s = s.replace('0','')
#         return s

#     def yigindi(self):
#         y = sum(int(i) for i in str(self.n))
#         if y % 2 == 0:
#             return y / 2
#         else:
#             return y + 5

# b = int(input('son kirting - '))
# a = NumberOperations(b)
# print(a.teskari())
# print(a.yigindi())

# 5

# class TupleAnalyzer:

#     def __init__(self, t):
#         self.t = t

#     def sonlani_chiqar(self):
#         sonlar = []
#         for i in self.t:
#             if isinstance(i, (int, float)):
#                 sonlar.append(i)

#         if sonlar:
#             return sonlar
#         else:
#             return "Sonlar yo'q"


# x = TupleAnalyzer((1, "salom", 3.5, "hi"))
# print(x.sonlani_chiqar())