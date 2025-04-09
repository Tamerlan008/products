import sqlite3

def books():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL

        );
    """)
    conn.commit()
    return conn

def add_book(title, author):
    conn = books()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
    conn.commit()
    conn.close()

def get_all_book():
    conn = books()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    result = cursor.fetchall()
    conn.close()
    return result

def search_book(title):
    conn = books()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE author LIKE ?", ('%' + title + '%',))
    result = cursor.fetchall()
    conn.close()
    return result

def delete_book(book_id):
    conn = books()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()
