import sqlite3


def create_db():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def products_1():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    products = [
        ("Сахар", 1.9, 25),
        ("Масло", 3.2, 10),
        ("Сыр", 4.5, 15)]
    cursor.executemany("INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)", products)
    conn.commit()
    conn.close()
    
    
def show_expensive_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE price > 2.0")
    products = cursor.fetchall()
    for product in products:
        product_id, name, price, quantity = product
        print(f"ID: {product_id}, Название: {name}, Цена: {price}, Количество: {quantity}")
    conn.close()    


def up_product():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET quantity = ? WHERE id = ?", (35, 3))
    conn.commit()
    conn.close()

def delete():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", (4,))
    conn.commit()
    conn.close()
    
    
if __name__ == "__main__":
    create_db()
    products_1()
    show_expensive_products()
    up_product()
    show_expensive_products()
    delete()
    show_expensive_products()