from psycopg2 import connect,Error

try:
    con = connect(
        user="postgres",
        password="pass",
        host="localhost",
        port="5432",
        database="hospital12"
    )
    print("Ulanish muvaffaqiyatli!")
except Exception as e:
    print(f"Xatolik yuz berdi: {e}")
cursor = con.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS hospital (
        id INTEGER PRIMARY KEY,
        name TEXT,
        address TEXT
    )
""")

con.commit()
print("bajardim")
