sonlar = list(range(15, 65))

def Olti(lis):
    def azizbek(li):
        x = []
        sonlar = lis(li)
        for i in sonlar:
            if i % 6 == 0:
                x.append(i)
        return x
    return azizbek   



def Uchga(lis: list):
    def Wrapper(li):
        a = []
        sonlar = lis(li)
        for i in sonlar:
            if i % 3 == 0:
                a.append(i)
        return a
    return Wrapper

@Olti
@Uchga
def Sozlar(soz):
    a = []
    for i in soz:
        if i.isdigit():
            a.append(int(i))
    return a

a = "325797539f4g5hd66fb82479"
print(Sozlar(a))

@Uchga
def Funk(a:list):
    lis = []
    for i in a:
        if i % 5 == 0:
            lis.append(i)
    return lis

# print(Funk(sonlar))
