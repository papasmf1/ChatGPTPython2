#Chap08_ChatGPT가생성한SQL구문.py
import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect('products.db')
cursor = conn.cursor()

# Products 테이블 생성
cursor.execute('''
CREATE TABLE IF NOT EXISTS Products (
    productID INTEGER PRIMARY KEY AUTOINCREMENT,
    productName TEXT NOT NULL,
    productPrice TEXT NOT NULL
)
''')

# 데이터 삽입 함수
def insert_product(name, price):
    cursor.execute('''
    INSERT INTO Products (productName, productPrice)
    VALUES (?, ?)
    ''', (name, price))
    conn.commit()

# 데이터 업데이트 함수
def update_product(product_id, name, price):
    cursor.execute('''
    UPDATE Products
    SET productName = ?, productPrice = ?
    WHERE productID = ?
    ''', (name, price, product_id))
    conn.commit()

# 데이터 삭제 함수
def delete_product(product_id):
    cursor.execute('''
    DELETE FROM Products
    WHERE productID = ?
    ''', (product_id,))
    conn.commit()

# 데이터 선택 함수
def select_products():
    cursor.execute('SELECT * FROM Products')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# 사용 예시
insert_product('Apple', '1.00')
insert_product('Banana', '0.50')
update_product(1, 'Apple', '1.20')
delete_product(2)
select_products()

# 데이터베이스 연결 종료
conn.close()
