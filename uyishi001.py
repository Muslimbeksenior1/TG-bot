# 1
#  class futbolchi:
#     def __init__(self,ismi,yoshi,driblingballi,qayerdaoynaydi,kamandasi):
#         self.ismi = ismi
#         self.yoshi = yoshi
#         self.driblingballi = driblingballi
#         self.qayerdaoynaydi = qayerdaoynaydi
#         self.kamandasi = kamandasi
#     def Messi(self):
#         Messi = f"malumoti: \n{self.kamandasi}\n Ismi: {self.ismi}\n Driblini: {self.driblingballi}\n {self.qayerdaoynaydi}\n"
#         return Messi
#     def Kaka(self):
#         Kaka = f"malumotlari: \n{self.ismi}\n {self.yoshi}\n {self.driblingballi}\n {self.qayerdaoynaydi}\n {self.kamandasi}\n"
#         return Kaka
#     def Ronaldinho(self):
#         Ronaldinho = f"malumotlari: \n{self.ismi}\n {self.yoshi}\n {self.driblingballi}\n {self.qayerdaoynaydi}\n {self.kamandasi}\n"
#         return Ronaldinho
#     def Marsello(self):
#         Marsello = f"malumotlari: \n{self.ismi}\n {self.yoshi}\n {self.driblingballi}\n {self.qayerdaoynaydi}\n {self.kamandasi}\n"
#         return Marsello
    
# Leo_Messi = futbolchi(ismi="Messi",yoshi="yoshi - 38",driblingballi="driblingi - 5 star",qayerdaoynaydi="pazitsiya - CAM",kamandasi="klub - InterMiami")
# Ricardo_Kaka = futbolchi(ismi="\nKaka",yoshi="yoshi - 43",driblingballi="driblingi - 5 star",qayerdaoynaydi="pazitsiya - CAM",kamandasi="klub - Milan")
# Ronaldinho = futbolchi(ismi="\nRonaldinho",yoshi="yoshi - 45",driblingballi="driblingi - 5 star",qayerdaoynaydi="pazitsiya - LW",kamandasi="klub - Barselona")
# Marsello = futbolchi(ismi="\nMarsello",yoshi="yoshi - 37",driblingballi="driblingi - 5 star",qayerdaoynaydi="pazitsiya - LB",kamandasi="klub - Real Madrid")
# print(Leo_Messi.Messi())
# print(Ricardo_Kaka.Messi())
# print(Ronaldinho.Ronaldinho())
# print(Marsello.Marsello())


# 2

# class noutbuk:
#     def __init__(self,narxi,xotirasi,protsessori,videokarta,ekrangersi):
#         self.narxi = narxi
#         self.xotirasi = xotirasi
#         self.protsessori = protsessori
#         self.videokarta = videokarta
#         self.ekrangersi = ekrangersi
#     def Lenova(self):
#         lenovaLOQ = f"malumotlari: narxi - {self.narxi}\n xotirasi - {self.xotirasi}\n protsessori - {self.protsessori}\n videokarta - {self.videokarta}\n ekrangersi - {self.ekrangersi}\n"
#         return lenovaLOQ
# Lenova = noutbuk(narxi="1000 $",xotirasi="1TB",protsessori="RYZEN 7",videokarta="RTX 4070",ekrangersi="240 HZ")
# print(Lenova.Lenova())


# 3

# class noutbuk:
#     def __init__(self,narxi,mashina,tezligi,turi,nomi):
#         self.narxi = narxi
#         self.mashina = mashina
#         self.tezligi = tezligi
#         self.turi = turi
#         self.nomi = nomi
#     def byd(self):
#         SEAL = f"malumotlari: narxi - {self.narxi}\n mashina - {self.mashina}\n tezligi - {self.tezligi}\n turi - {self.turi}\n nomi - {self.nomi}\n"
#         return SEAL
    
# SEAL = noutbuk(narxi="10000 $",mashina="BYD",tezligi="300 km/h",turi="seal",nomi="BYD Seal")
# Chazor = noutbuk(narxi="100000 $",mashina="Chazor",tezligi="400 km/h",turi="chazor",nomi="Chazor")
# Han = noutbuk(narxi="1000000 $",mashina="Han",tezligi="500 km/h",turi="BYD",nomi="Han")
# print(SEAL.byd())
# print(Chazor.byd())
# print(Han.byd())





from uuid import uuid4

class Shaxs:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    
    def Info(self):
        data = f"Familya: {self.lastname}\nIsm: {self.name}"
        return data



class Student(Shaxs):
    def __init__(self, name, lastname, kurs, manzil):
        super().__init__(name, lastname)
        self.kurs = kurs
        self.manzil = manzil
        self.id = uuid4()

    def Info(self):
        data = f"Familya: {self.lastname}\nIsm: {self.name}\nkurs: {self.kurs}\nId: {self.id}\n{self.manzil}"
        return data

class Manzil:
    def __init__(self, viloyat, tuman, mahalla, uy):
        self.viloyat = viloyat
        self.tuman = tuman
        self.mahalla = mahalla
        self.uy = uy


    def Info(self):
        data = f"\nViloyat: {self.viloyat}\nTuman: {self.tuman}\nMahalla: {self.mahalla}\nUy: {self.uy}\n"
        return data

person1 = Shaxs(name="Ali", lastname="Valiyev")
person2_manzil = Manzil(viloyat="Xorazm", tuman="Bog'at", mahalla="Gulzor", uy="2-uy")
person2 = Student(name="Azizbek", lastname="Ruzimboyev", kurs=2, manzil=person2_manzil.Info())
print(person2.Info())

print(person1.Info())
