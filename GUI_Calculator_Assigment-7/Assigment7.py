
import sys
from functools import partial

from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, 
                             QVBoxLayout, QGridLayout, QLineEdit, QPushButton)
from PyQt5.QtCore import Qt

# ==========================================
# 1. THE MODEL (Logic)
# ==========================================
class CalculatorModel:
    """
    The Model handles the business logic. 
    It performs the math and doesn't know about the UI.
    """
    def evaluate_expression(self, expression):
        """
        Evaluates a mathematical string expression.
        """
        try:
            result = str(eval(expression, {}, {}))
            return result
        except ZeroDivisionError:
            return "Error"
        except Exception:
            return "Error"

# ==========================================
# 2. THE VIEW (GUI)
# ==========================================
class CalculatorView(QMainWindow):
    """
    The View handles the Graphical User Interface (GUI).
    It sets up the window, buttons, and display.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MVC Calculator")
        self.setFixedSize(350, 450)
        self.general_layout = QVBoxLayout()
        
        # Нащи виджет для центрального окна и устанавливаем ему наш общий лэйаут, который будет содержать дисплей и кнопки.
        self._central_widget = QWidget(self)
        self.setCentralWidget(self._central_widget)
        self._central_widget.setLayout(self.general_layout)
        
        # Создаем дисплей и кнопки
        self._create_display()
        self._create_buttons()
        self._apply_styles()

    def _create_display(self):
        """Create the input/output display line."""
        self.display = QLineEdit()
        self.display.setFixedHeight(50)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True) 
        self.general_layout.addWidget(self.display)

    def _create_buttons(self):
        """Create the grid of buttons."""
        self.buttons = {}
        buttons_layout = QGridLayout()
        
        # Тут я использовал словарь для хранения кнопок и их позиций, чтобы код был чище и легче поддерживался.
        button_map = {
            'C': (0, 0), '/': (0, 1), '*': (0, 2), '-': (0, 3),
            '7': (1, 0), '8': (1, 1), '9': (1, 2), '+': (1, 3),
            '4': (2, 0), '5': (2, 1), '6': (2, 2), 
            '1': (3, 0), '2': (3, 1), '3': (3, 2), '=': (2, 3), 
            '0': (4, 0), '.': (4, 1),
        }
        
        
        key_layout = [
            ['C', '/', '*', '-'],
            ['7', '8', '9', '+'],
            ['4', '5', '6', ''], 
            ['1', '2', '3', '='], 
            ['0', '.', '', '']
        ]
        
        
        buttons = {
            'C': (0, 0), '/': (0, 1), '*': (0, 2), '-': (0, 3),
            '7': (1, 0), '8': (1, 1), '9': (1, 2), '+': (1, 3),
            '4': (2, 0), '5': (2, 1), '6': (2, 2), 
            '1': (3, 0), '2': (3, 1), '3': (3, 2), '=': (2, 3),
            '0': (4, 0), '.': (4, 1)
        }

        for btn_text, pos in buttons.items():
            self.buttons[btn_text] = QPushButton(btn_text)
            self.buttons[btn_text].setFixedSize(60, 60)
            
            if btn_text == '=':
                self.buttons[btn_text].setFixedSize(60, 125) 
                buttons_layout.addWidget(self.buttons[btn_text], 2, 3, 2, 1)
            elif btn_text == '0':
                self.buttons[btn_text].setFixedSize(125, 60) 
                buttons_layout.addWidget(self.buttons[btn_text], 4, 0, 1, 2) 
            elif btn_text == '+':
                 self.buttons[btn_text].setFixedSize(60, 125) 
                 buttons_layout.addWidget(self.buttons[btn_text], 0, 3, 2, 1) 
            else:
                 
                 buttons_layout.addWidget(self.buttons[btn_text], pos[0], pos[1])

        
        
        self.buttons = {} 
        buttons_layout = QGridLayout()
        
        layout_map = [
            ['C', 0, 0], ['/', 0, 1], ['*', 0, 2], ['-', 0, 3],
            ['7', 1, 0], ['8', 1, 1], ['9', 1, 2], ['+', 1, 3],
            ['4', 2, 0], ['5', 2, 1], ['6', 2, 2], 
            ['1', 3, 0], ['2', 3, 1], ['3', 3, 2], ['=', 3, 3],
            ['0', 4, 0], ['.', 4, 1]
        ]
        # Тут я взял из stackoverflow идею с layout_map для более чистого кода, так как кнопок много и их расположение может быть неочевидным при прямом добавлении в код/
        for text, r, c in layout_map:
            btn = QPushButton(text)
            self.buttons[text] = btn
            if text == '0':
                buttons_layout.addWidget(btn, r, c, 1, 2) 
            elif text == '=':
                buttons_layout.addWidget(btn, r, c, 2, 1) 
            elif text == '.':
                 buttons_layout.addWidget(btn, r, c+1) 
            elif text == '+':
                 buttons_layout.addWidget(btn, r, c) 
            else:
                buttons_layout.addWidget(btn, r, c)
        
        self.general_layout.addLayout(buttons_layout)

# UI-UX Дизайн стиля для нашего калькулятора, чтобы он выглядел современно и привлекательно.
    def set_display_text(self, text):
        """Set the text of the display line."""
        self.display.setText(text)
        self.display.setFocus()

    def get_display_text(self):
        """Get the current text."""
        return self.display.text()

    def clear_display(self):
        """Clear the text."""
        self.set_display_text("")

    def _apply_styles(self):
        """Apply some CSS to make it look nice."""
        style = """
            QMainWindow {
                background-color: #2b2b2b;
            }
            QLineEdit {
                background-color: #3b3b3b;
                color: #ffffff;
                border: 1px solid #555;
                font-size: 24px;
                padding: 5px;
                border-radius: 5px;
            }
            QPushButton {
                background-color: #4a4a4a;
                color: white;
                font-size: 18px;
                border-radius: 5px;
                border: 1px solid #333;
                padding: 15px;
            }
            QPushButton:hover {
                background-color: #5a5a5a;
            }
            QPushButton:pressed {
                background-color: #3a3a3a;
            }
            /* Make operators a different color */
            QPushButton[text="/"], QPushButton[text="*"], 
            QPushButton[text="-"], QPushButton[text="+"], 
            QPushButton[text="="] {
                background-color: #ff9800;
                color: black;
                font-weight: bold;
            }
            QPushButton[text="="]:hover, QPushButton[text="+"]:hover {
                background-color: #ffb74d;
            }
            /* Make Clear button red-ish */
            QPushButton[text="C"] {
                background-color: #d32f2f;
                font-weight: bold;
            }
        """
        self.setStyleSheet(style)

# Контроллер для калькулятор это запус самого дисплея и логики, он же связывает их между собой.
class CalculatorController:
    """
    The Controller connects the View and the Model.
    It listens for events from the View and tells the Model what to do.
    """
    def __init__(self, model, view):
        self._model = model
        self._view = view
        self._connect_signals()

    def _calculate_result(self):
        """Get text from view, calculate via model, update view."""
        expression = self._view.get_display_text()
        result = self._model.evaluate_expression(expression)
        self._view.set_display_text(result)

    def _build_expression(self, sub_exp):
        """Add the pressed button text to the display."""
        if self._view.get_display_text() == "Error":
            self._view.clear_display()
        
        expression = self._view.get_display_text() + sub_exp
        self._view.set_display_text(expression)

    def _connect_signals(self):
        """Connect the View's buttons to the Controller's methods."""
        for btn_text, btn in self._view.buttons.items():
            if btn_text not in {'=', 'C'}:
                btn.clicked.connect(partial(self._build_expression, btn_text))
            
        self._view.buttons['='].clicked.connect(self._calculate_result)
        self._view.buttons['C'].clicked.connect(self._view.clear_display)
        
        self._view.display.returnPressed.connect(self._calculate_result)

# Тут наш запуск приложения вобщем это классно
def main():
    """Main function to run the application."""
    
    app = QApplication(sys.argv)

   
    view = CalculatorView()
    view.show()

    
    model = CalculatorModel()
    CalculatorController(model=model, view=view)

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
