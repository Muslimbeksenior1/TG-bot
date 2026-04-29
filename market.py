import requests

url = "https://dummyjson.com/products"

api = requests.get(url).json()

true = True
pr_list = []
price = 0
print("marketgaga hush kelibsiz!!! \nnima olasiz? id talang\n\n")
while true:
    print(api["products"])
    for i in api['products']:
        print(f"id: {i['id']} -> Ism: {i['title']}\nnarx: {i['price']}\n\n")

    pr_id = input("product id kiriting yoqi cart: ")
    if pr_id.isdigit():
        for j in api['products']:
            if j['id'] == int(pr_id):
                print(f""" \nProduct {j['title']} 
                \nid: {j['id']} -- ism: {j['title']} -- narh: {j['price']}\ndescription: {j['description']}\nimage: {j['images'][0]}
                """)
        print("Productni cartga koshasmi ?")
        answer = input("ha / yoq kriting:")
        if answer == 'ha':
            pr_list.append(int(pr_id))
        elif answer == 'yoq':
            ...
    elif pr_id == 'cart':
        print("""\n\n ||| Cart ||| \n\n""")
        for i in api["products"]:
            if i['id'] in pr_list:
                price += i['price']
                print(f""" ism: {i['title']} -- price: {i['price']} \n""")
        print(f"Totall price {price}")
        print("sotib olasmi ?")
        answer = input("ha / yoq ?: ")
        if answer == 'ha':
            name = input('Full name kiriting: ')
            number = input('telefon raqam kiriting: ')
            print(f"galib during {name}")
            break
        elif answer == 'yoq':
            print("Mahsulotlarni kayta korishni hohlisma ?")
            answ = input("ha \ yoq ?")
            if answ == 'ha':
                ...
            elif answ == 'yoq':
                print("Kelib during")
                break
