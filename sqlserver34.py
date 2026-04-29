from sqlite3 import connect


con = connect('alldatabasess.db')

# def products(name,phone):
#     cursor = con.cursor()
#     cursor.execute("""UPDATE employees SET phone = 87 WHERE name = 'muslimbek';""",(name,phone))
#     con.commit()
#     return 'bajardim'
# for i in range(1):
#     name = input('ism kiriting - ')
#     phone = int(input('tel - '))        
# print(products(name,phone))

cursor = con.cursor()
cursor.execute("SELECT customer, FROM alldatabasess WHERE name = 'muslimbek';") 
con.commit()
print(cursor.fetchall())
