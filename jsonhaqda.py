import json

with open('viloyatlar.json', 'r', encoding="UTF-8") as file:
    malumot = json.load(file)

with open('tuman.json', 'r', encoding="UTF-8") as file:
    tumanlar = json.load(file)

for viloyat in malumot:
    print(viloyat['id'], viloyat['name_uz'])

user_t =int(input("viloyatingiz id: "))

for tuman in tumanlar:
    if user_t == tuman['region_id']:
        print("\n\n",tuman['id'], tuman['name_uz'])


# print(f"Testlar {malumot['fan']}")
# cnt = 0
# for test in malumot.get('testlar'):
#     print(f"{test['id']}) {test["savol"]}")
#     variant = {'a': test['variantlar'][0], "b": test['variantlar'][1], "c":test['variantlar'][2], "d":test['variantlar'][3]}
#     print(f"a) {test['variantlar'][0]}\nb) {test['variantlar'][1]}\nc) {test['variantlar'][2]}\nd) {test['variantlar'][3]}\n")
#     user = input("variantlardan birini tanlang: ")
#     if variant[user] == test['togri_javob']:
#         cnt += 1
#         print("ajoyib")
#     else:
#         print("bro xato")

# print(f"natijangiz {cnt / 10 * 100} % ")





















# a = malumot['fanlar'][1]
# print(a)

# a = malumot.values()
# print(a)

# with open('test.json', 'r') as file:
#     malumot = json.load(file)

# print(type(malumot))







# dic = {
#     "name":"Ali",
#     'lastname':'Valiyev',
#     'age': 15
# }
# b = json.dumps(dic)
# print((b))

# a = 5

# a = json.dumps(a)
# a = json.loads(a)
# print(type(a))
