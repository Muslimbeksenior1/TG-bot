# 1
# def son(n):
#     result = []
#     for i in range(1, n + 1):
#         if i % 3 == 0 and i % 9 == 0:
#             result.append(i)
#     return result

# print(son(30))

# 2

# def faqat_undoshlar(matn):
#     matn = matn.lower()
#     unlilar = "aeiououi"
#     natija = ""
#     for harf in matn:
#         if harf.isalpha() and harf not in unlilar:
#             natija += harf
#     return natija
# soz = input('matn kirting')
# print(faqat_undoshlar(soz))


# 3

# san = input('matn kiriting - ')
# m = san[::-1]
# if m == san:
#     print(True)
# else:
#     print(False)


# 4

# list = [12,32,43,34,2,34,2,3,21]
# resut = []
# for i in list:
#     if i % 2 == 0:
#         m = i * 2
#         resut.append(m)
# print(resut)

#5
# def soz(matn):
#     natija = {}
#     for harf in matn:
#         if harf in natija:
#             natija[harf] += 1
#         else:
#             natija[harf] = 1
#     return natija

# print(soz("hello"))


# 6
# def min_max_farq(royxat):
#     eng_katta = max(royxat)
#     eng_kichik = min(royxat)
#     return (eng_katta, eng_kichik, eng_katta - eng_kichik)

# print(min_max_farq([3, 7, 2, 9, 4]))


# 7

# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade

#     def baho(self):
#         if self.grade >= 90:
#             return "A"
#         elif self.grade >= 70:
#             return "B"
#         elif self.grade >= 50:
#             return "C"
#         else:
#             return "F"

# s = Student("Ali", 85)
# print(s.baho())

# 8

# import requests

# url = "https://dummyjson.com/users"
# data = requests.get(url).json()

# for user in data["users"]:
#     if user["age"] > 30:
#         print(user["firstName"], user["age"])

# 9

# from sqlite3 import connect

# con = connect('students.db')

# def AddUser(name, lastname, grede):
#     cursor = con.cursor()
#     cursor.execute("""insert into students(name, lastname, age) values(?, ?, ?)""", (name, lastname, grede))
#     con.commit()
#     return 'bajrdim'

# for i in range(6):
#     name = input('ism: ')
#     lastname = input('lastname; ')
#     grede = int(input("yosh: "))
#     print(AddUser(name, lastname, grede))



# cursor = con.cursor()
# cursor.execute("""
#         Create table Students(
#             ID INTEGER PRIMARY KEY NOT NULL,
#                name text not null,
#                lastname text not null,
#                age int
#                );

# """)
# con.commit()
# print("bajarildi")



# cursor = con.cursor()
# cursor.execute("SELECT * FROM students WHERE age > 20")
# con.commit()
# print("bajarildi")


# 10
# import sqlite3

# conn = sqlite3.connect("students.db")
# cur = conn.cursor()

# cur.execute("SELECT MIN(age) FROM students")
# print(cur.fetchone())

# cur.execute("UPDATE students SET grade = grade + 5 WHERE grade < 60")
# conn.commit()

# cur.execute("""
# SELECT grade, COUNT(*) 
# FROM students
# GROUP BY grade
# """)

# for row in cur.fetchall():
#     print(row)

# conn.close()