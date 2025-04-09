from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton,
    QTableWidget, QTableWidgetItem, QHBoxLayout
)
from PyQt6.QtCore import Qt

class BookApp(QWidget):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.setWindowTitle("Книги (PyQt6)")
        self.setGeometry(100, 100, 600, 400)
        self.layout = QVBoxLayout()
        
        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Заголовок")

        self.author_input = QLineEdit()
        self.author_input.setPlaceholderText("Автор")

        self.add_btn = QPushButton("Добавить книгу")
        self.add_btn.clicked.connect(self.add_book)
        
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Поиск по названию или автору")
        self.search_btn = QPushButton("Найти")
        self.search_btn.clicked.connect(self.search_book)
        
        self.refresh_btn = QPushButton("Показать все")
        self.refresh_btn.clicked.connect(self.load_book)
        
        self.book_table = QTableWidget()
        self.book_table.setColumnCount(3)
        self.book_table.setHorizontalHeaderLabels(["ID", "Название", "Автор"])
        self.book_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        
        self.delete_input = QLineEdit()
        self.delete_input.setPlaceholderText("ID для удаления")
        self.delete_btn = QPushButton("Удалить")
        self.delete_btn.clicked.connect(self.delete_book)
        
        self.layout.addWidget(QLabel("Добавить книгу:"))
        self.layout.addWidget(self.title_input)
        self.layout.addWidget(self.author_input)
        self.layout.addWidget(self.add_btn)

        self.layout.addWidget(QLabel("Поиск книги:"))
        search_layout = QHBoxLayout()
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_btn)
        search_layout.addWidget(self.refresh_btn)
        self.layout.addLayout(search_layout)

        self.layout.addWidget(self.book_table)

        self.layout.addWidget(QLabel("Удалить книгу по ID:"))
        delete_layout = QHBoxLayout()
        delete_layout.addWidget(self.delete_input)
        delete_layout.addWidget(self.delete_btn)
        self.layout.addLayout(delete_layout)

        self.setLayout(self.layout)
        self.load_book()


    def add_book(self):
        title = self.title_input.text()
        author = self.author_input.text()
        
        if title:
            self.db.add_book(title, author)
            self.load_book()
            self.title_input.clear()
            self.author_input.clear()


    def load_book(self):
        self.book_table.setRowCount(0)
        for row_data in self.db.get_all_book():
            row_number = self.book_table.rowCount()
            self.book_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.book_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def search_book(self):
        title = self.search_input.text()
        results = self.db.search_book(title)
        self.book_table.setRowCount(0)
        for row_data in results:
            row_number = self.book_table.rowCount()
            self.book_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.book_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def delete_book(self):
        try:
            book_id = int(self.delete_input.text())
            self.db.delete_book(book_id)
            self.load_book()
            self.delete_input.clear()
        except ValueError:
            pass