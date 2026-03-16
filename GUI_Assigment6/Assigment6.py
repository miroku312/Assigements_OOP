import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QPlainTextEdit, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt6 import uic


class SimpleApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Clean Python GUI")
        self.resize(400, 300)  # Тут наш дизай котором ты братан можешь настроить setFixedSize(400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget) # Эта строка устанавливает центральный виджет для нашего главного окна. 

        layout = QVBoxLayout(central_widget) # Эта строка создаёт вертикальный макет нашего центрального виджета. 

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.info_label = QLabel("My name is AlaToo:")
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Type here...")

        self.action_button = QPushButton("Submit")
        self.result_label = QLabel("") # Тут мы получаем наши результаты

        layout.addWidget(self.info_label)  #1
        layout.addWidget(self.name_input)   #2
        layout.addWidget(self.action_button)  #3
        layout.addWidget(self.result_label)   #4 Эта строка добавляет виджеты в вертикальный макет, который мы создали ранее.

        layout.addStretch() 

        self.action_button.clicked.connect(self.on_button_click) # Добовляем кнопке действие при нажатии

        self.name_input.returnPressed.connect(self.action_button.click)
        
    def on_button_click(self):
        """
        Logic to handle the button click event.
        """
        user_text = self.name_input.text()

        if user_text:
            self.result_label.setText(f"Салам Алйкум, {user_text}! Чё как там. ")
            self.result_label.setStyleSheet("color: green; font-weight: bold;")
        else:
            self.result_label.setText("Напишут тут чё-то.")
            self.result_label.setStyleSheet("color: red;")

if __name__ == "__main__": # Тут мы проверяем, что этот файл запускается как основная программа, а не импортируется как модуль.
    app = QApplication(sys.argv)

    # И так понятно что тут мы создаем само окно приложения :P
    window = SimpleApp()
    window.show()

    # Запускаем Бисмиля.
    sys.exit(app.exec())