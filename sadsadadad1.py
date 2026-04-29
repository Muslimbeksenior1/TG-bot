# 1
# from datetime import date

# a = int(input())
# b = int(input())

# yil = a - b
# print(yil)

# 2

# from datetime import date
# today = date.today()
# new_year = date(today.year + 1, 1, 1)

# days_left = (new_year - today).days

# print(days_left,'kun qoldi')

# 3
# from datetime import date, datetime
# today = datetime.now()
# masharipov = date()
# vaqt = today.time() # bu faqat hozir soat
# today2 = today - masharipov
# vaqt = today.hour
# print(today2+vaqt)

# 4

# import calendar
# from datetime import datetime

# sana = datetime(2026, 3, 6)
# oxirgi_kun = calendar.monthrange(sana.year, sana.month)[1]
# print(f"{oxirgi_kun}")

# 5
# from datetime import datetime
# import datetime


# bugun = datetime(2026, 3, 4)
# yangi_yil = datetime(2027, 1, 1)
# qolgan_kun = (yangi_yil - bugun).days
# print(f"{qolgan_kun} kun qoldi")