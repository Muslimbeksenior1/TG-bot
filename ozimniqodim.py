import requests 

url = "https://dummyjson.com/products"
api = requests.get(url).json()

narsalar = []
narxi = 0
true = True
print('magazinmizga hush kelibsiz!!!!')
print('nima olasiz?')
pul = int(input('qancha miqdorda mablagingiz bor - '))
print(api['products'])
for i in api['products']:
    print(f"soni: {i['id']} -> nomi: {i['title']}\nnarx: {i['price']}")
narsalar2 = input('product idni kirting - ')
if narsalar2.isdigit():
    for j in api['products']:
        if j['id'] == int(narsalar2):
            print(f"\nProduct {j['title']} id -> {j['id']} nomi-> {j['title']}  narxi -> {j['price']}")
    print('naxt yoki carta')
    javob = input('>>> ')
    if javob == "naxt":
        pul - j['price']
    elif javob == "carta":
        ...
elif narsalar2 == 'carta':
    print(f'CHEKNI OLING MARHAMAT{pul}')
    for i in api['products']:
        if i['id'] in narsalar:
            narxi+= i['price']
            print(f"""nomi - > {i['title']} narxi - > {i['price']} \n """)
        print(f"umumiy miqdor {narxi}")
        print("carta bilan olasmi - ha/yoq --->")
        javob2 = input('')
        if javob2 == 'ha':
            masalan = 'masalan = 9860******677'
            number = input('karta raqam kirting - ')
            ism = input('ismingiz - ')
            print(f'TANLOV UCHUN RAHMAT!!!')
            print(F'KELIB TURING{ism}')
            break
        elif javob2 == 'yoq':
            print('yana narsa olasizmi?')
            sav = input('ha yoki yoq')
            if sav == "ha":
                ...
            elif sav == 'yoq':
                print(f"kelib turing rahmat")
                break
