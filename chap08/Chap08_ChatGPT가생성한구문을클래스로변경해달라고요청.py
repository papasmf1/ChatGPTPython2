#Chap08_ChatGPT가생성한구문을클래스로변경해달라고요청.py
import sqlite3

class Products:
    def __init__(self, db_name='products.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            productID INTEGER PRIMARY KEY AUTOINCREMENT,
            productName TEXT NOT NULL,
            productPrice TEXT NOT NULL
        )
        ''')
        self.conn.commit()

    def insert_product(self, name, price):
        self.cursor.execute('''
        INSERT INTO Products (productName, productPrice)
        VALUES (?, ?)
        ''', (name, price))
        self.conn.commit()

    def update_product(self, product_id, name, price):
        self.cursor.execute('''
        UPDATE Products
        SET productName = ?, productPrice = ?
        WHERE productID = ?
        ''', (name, price, product_id))
        self.conn.commit()

    def delete_product(self, product_id):
        self.cursor.execute('''
        DELETE FROM Products
        WHERE productID = ?
        ''', (product_id,))
        self.conn.commit()

    def select_products(self):
        self.cursor.execute('SELECT * FROM Products')
        rows = self.cursor.fetchall()
        return rows

    def close(self):
        self.conn.close()

# 테스트 코드
if __name__ == "__main__":
    products = Products()

    # 10개의 제품 데이터 삽입
    product_list = [
        ('Apple', '1.00'),
        ('Banana', '0.50'),
        ('Cherry', '2.00'),
        ('Date', '3.00'),
        ('Elderberry', '4.00'),
        ('Fig', '2.50'),
        ('Grape', '1.50'),
        ('Honeydew', '3.50'),
        ('Indian Fig', '5.00'),
        ('Jackfruit', '6.00')
    ]

    for name, price in product_list:
        products.insert_product(name, price)

    # 데이터 업데이트
    products.update_product(1, 'Apple', '1.20')
    products.update_product(5, 'Elderberry', '4.50')

    # 데이터 삭제
    products.delete_product(2)  # Banana 삭제
    products.delete_product(7)  # Grape 삭제

    # 데이터 선택 및 출력
    all_products = products.select_products()
    for product in all_products:
        print(product)

    # 데이터베이스 연결 종료
    products.close()
