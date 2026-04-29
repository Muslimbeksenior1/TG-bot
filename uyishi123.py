# 1
# from uuid import uuid4
# class elektromobile:
#     def __init__(self, narxi, mashina, tezligi, turi, nomi):
#         self.narxi = narxi
#         self.mashina = mashina
#         self.tezligi = tezligi
#         self.turi = turi
#         self.nomi = nomi
#         self.id = uuid4()

#     def Info(self):
#         data = f"malumotlari: narxi - {self.narxi}\n mashina - {self.mashina}\n tezligi - {self.tezligi}\n turi - {self.turi}\n nomi - {self.nomi}\nId: {self.id}"
#         return data
# elektromobile1 = elektromobile(100000, "Tesla", 250, "Sedan", "Model S")
# print(elektromobile1.Info())


# 2


# from uuid import uuid4

# class Shaxs:
#     def __init__(self, name, lastname):
#         self.name = name
#         self.lastname = lastname

    
#     def Info(self):
#         data = f"Familya: {self.lastname}\nIsm: {self.name}"
#         return data



# class Student(Shaxs):
#     def __init__(self, name, lastname, kurs, manzil):
#         super().__init__(name, lastname)
#         self.kurs = kurs
#         self.manzil = manzil
#         self.id = uuid4()

#     def Info(self):
#         data = f"Familya: {self.lastname}\nIsm: {self.name}\nkurs: {self.kurs}\nId: {self.id}\n{self.manzil}"
#         return data

# class Manzil:
#     def __init__(self, viloyat, tuman, mahalla, uy):
#         self.viloyat = viloyat
#         self.tuman = tuman
#         self.mahalla = mahalla
#         self.uy = uy


#     def Info(self):
#         data = f"\nViloyat: {self.viloyat}\nTuman: {self.tuman}\nMahalla: {self.mahalla}\nUy: {self.uy}\n"
#         return data

# person1 = Shaxs(name="Ali", lastname="Valiyev")
# person2_manzil = Manzil(viloyat="Xorazm", tuman="Bog'at", mahalla="Gulzor", uy="2-uy")
# person2 = Student(name="Azizbek", lastname="Ruzimboyev", kurs=2, manzil=person2_manzil.Info())
# print(person2.Info())

# print(person1.Info())


# 4




# from uuid import uuid4
# class hisob_kitob:
#     def __init__(self, balanc, yechim, parol, turi):
#         self.balanc = balanc
#         self.yechim = yechim
#         self.parol = parol
#         self.turi = turi
#         self.id = uuid4()

#     def Info(self):
#         data = f"malumotlari: balanc - {self.balanc}\n yechim - {self.yechim}\n parol - {self.parol}\n turi - {self.turi}\nId: {self.id}"
#         return data
# hisob_kitob1 = hisob_kitob(balanc=100000, yechim="Naqd pul", parol="123456", turi="Plastik karta")
# print(hisob_kitob1.Info())
