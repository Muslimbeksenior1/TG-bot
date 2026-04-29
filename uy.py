# restoran = {
#     "Gazaklar": {
#         "Bahorcha Roll": {
#             "narx": 5_000,
#             "ingredientlar": ["karam", "sabzi", "shisha vermishel", "qo'ziqorinlar"],
#             "vegetarian": True,
#             "achchiqlik_darajasi": 1
#         },
#         "Qo'ziqorin To'ldirmasi": {
#             "narx": 7_500,
#             "ingredientlar": ["qo'ziqorin", "krem pishloq", "ziravorlar", "non uvoqlari"],
#             "vegetarian": False,
#             "achchiqlik_darajasi": 0
#         },
#     },
#     "Asosiy Taomlar": {
#         "Gril Salmon": {
#             "narx": 18_000,
#             "ingredientlar": ["salmon baliq", "limon", "ukrop", "yog'"],
#             "vegetarian": False,
#             "achchiqlik_darajasi": 0
#         },
#         "Achchiq Tailand Karri": {
#             "narx": 15_500,
#             "ingredientlar": ["kokos sut", "tofu", "reyhan", "chili", "guruch"],
#             "vegetarian": True,
#             "achchiqlik_darajasi": 3,
#             "mavjud_hajmlar": ["kichik", "o'rtacha", "katta"]
#         },
#         "Pasta Carbonara": {
#             "narx": 14_500,
#             "ingredientlar": ["spagetti", "tuxum", "parmezan", "pancetta"],
#             "vegetarian": False,
#             "achchiqlik_darajasi": 0
#         },
#     },
#     "Shirinliklar": {
#         "Shokolad Lava Keki": {
#             "narx": 6_500,
#             "ingredientlar": ["shokolad", "un", "tuxum", "yog'"],
#             "vegetarian": False,
#             "kaloriya": 450
#         },
#         "Mevali Salat": {
#             "narx": 5_000,
#             "ingredientlar": ["qulupnay", "ko'k rezavor", "kivi", "apelsin", "yalpiz"],
#             "vegetarian": True,
#             "kaloriya": 120
#         },
#     },
#     "Ichimliklar": {
#         "Yangi Siqilgan Apelsin Sharbati": {
#             "narx": 3_500,
#             "ingredientlar": ["apelsin"],
#             "vegetarian": True
#         },
#         "Ko'k Choy": {
#             "narx": 2_000,
#             "ingredientlar": ["ko'k choy barglari"],
#             "vegetarian": True
#         },
#     }
# }
# print("restoranimzga hush kebsiz\n")
# savat = {}
# while True:
#     for i in restoran:
#         print(i, end=" ")
#     user = input("\n\nbo'lim tanlang: ")
#     if user == "yoq":
#         print("\restoranimzga yena kelib trung\n")
#         break
#     if user in restoran:
#         while True:
#             for i, j in restoran[user].items():
#                 print(i, j, "$")
#             user_t = input("nomini tanlang: ")
#             if user_t == "yoq":
#                 print("\nmenyuga Xush kelibsiz\n")
#                 break
#             if user_t in restoran[user]:
#                 savat.update({user_t:restoran[user][user_t]})
#             else:
#                 print("siz so'ragan model yoq")
#     else:
#         print("siz so'ragan maxsulot yoq")
# jammi =0
# print("\n\nSizning CHekingiz\nMaxsulot nomi    |    maxsulot narxi     |\n")
# for i, j in savat.items():
#     print(f"|  {i}     |   {j}$    |")
#     jammi += j
# print("sizdan", jammi, "$")
