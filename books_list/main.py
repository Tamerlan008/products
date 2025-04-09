import sys
from PyQt6.QtWidgets import QApplication
import datebase
from ui import BookApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BookApp(datebase)
    window.show()
    sys.exit(app.exec())