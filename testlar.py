import json

with open('test.json', 'r', encoding="UTF-8") as file:
    malumot = json.load(file)


cnt = 0

print(f"savollar {malumot['fanlar']}")
cnt = 0
for test in malumot.get('fanlar'):
    print(f"{test['fan_nomi']}")
    for i in test.get('savollar'):
        for j in i['variantlar']:
            if i['variantlar'] == i['togri_javob']:
                cnt += 1
                print('togri')
            else:
                print('xato')       