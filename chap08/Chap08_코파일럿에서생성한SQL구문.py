#Chap08_코파일럿에서생성한SQL구문.py 
import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect('products.db')

# 테이블 생성
conn.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        productID INTEGER PRIMARY KEY,
        productName TEXT,
        productPrice TEXT
    );
''')

# 데이터 삽입
def insert_product(productID, productName, productPrice):
    conn.execute('INSERT INTO Products (productID, productName, productPrice) VALUES (?, ?, ?)',
                 (productID, productName, productPrice))
    conn.commit()

# 데이터 조회
def select_products():
    cursor = conn.execute('SELECT * FROM Products')
    for row in cursor:
        print(row)

# 데이터 업데이트
def update_product_price(productID, newPrice):
    conn.execute('UPDATE Products SET productPrice = ? WHERE productID = ?', (newPrice, productID))
    conn.commit()

# 데이터 삭제
def delete_product(productID):
    conn.execute('DELETE FROM Products WHERE productID = ?', (productID,))
    conn.commit()

# 예시 데이터 삽입
insert_product(1, 'Laptop', '1000')
insert_product(2, 'Phone', '500')

# 데이터 조회
select_products()

# 데이터 업데이트
update_product_price(1, '1200')

# 데이터 삭제
delete_product(2)

# 연결 종료
conn.close()
