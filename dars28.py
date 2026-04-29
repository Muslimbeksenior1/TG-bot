# import os

# os.rmdir('Muslimbek')

# for i in range(1000000):
#     os.mkdir(f'Muslimbek/{i}')

# open('Muslimbek/test.py', 'x')
# os.mkdir('Muslimbek')

# os.remove('Muslimbek/test.py')
# print("bajarildi")


# import pickle

# with open("malumot", 'rb') as file:
#     malumot = pickle.load(file)

# print(malumot)

# a = {
#     'ism': 'Ali',
#     'familiya':'Valiyev',
#     'age':25
# }

# with open("malumot", 'wb') as file:
#     pickle.dump(a, file)

# b = pickle.dumps(a)
# c = pickle.loads(b)
# print(type(a))
# print(type(b))
# print(type(c))



# soz = input("soz: ")

# with open('malumotim.txt', 'w') as file:
#     file.write(soz)

# with open('malumotim.txt', 'a') as file:
#     file.write(f"\n{soz}")

# with open("malumotim.txt", 'r') as file:
#     malumot = file.read()



# try:
#     a = int(input("soni kiriting: "))
#     b = float(input("soni kiriting: "))
#     s = a / b
#     print(s)
# except:
#     print("sizda xato bor")
# else:
#     print("dastur ishladi")
# finally:
#     print("bu qachon ishlaydi")


# try:

# except ZeroDivisionError:
#     print("siz soni no'lga bo'lib bo'lmaydi")
# except ValueError:
#     print("sonlarni to'g'ri kiriting ? ")



# a = {
#     "name":"Ali",
#     'lastname':'Valiyev',
#     'age':25
# }
# try:
#     print(a['name'])
# except KeyError:
#     print("siz dictdan keyni xato yozdingiz")

# try:
#     a = 15
#     b = "salom"

#     s = a + b

#     print(s)
# except TypeError:
#     print("sizda intergerni stringa qo'shmoqchisiz")




def shifrlash(matn, kalit):
    natija = ""
    for belgi in matn:
        if belgi.isalpha():
            if belgi.islower():
                natija += chr((ord(belgi) - ord('a') + kalit) % 26 + ord('a'))
            else:
                natija += chr((ord(belgi) - ord('A') + kalit) % 26 + ord('A'))
        else:
            natija += belgi
    return natija


def ochish(matn, kalit):
    return shifrlash(matn, -kalit)

matn = input("Matn kiriting: ")
kalit = int(input("Kalit (son) kiriting: "))

shifr = shifrlash(matn, kalit)
print("Shifrlangan matn:", shifr)

asl = ochish(shifr, kalit)
print("Ochilgan matn:", asl)