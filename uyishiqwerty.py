import json



with open('yangifayl.json',encoding='utf-8',mode='r') as file:
    malumot = json.load(file)
a = malumot('name_uz')
print(a)