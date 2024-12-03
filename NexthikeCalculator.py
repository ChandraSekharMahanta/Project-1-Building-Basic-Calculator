import sys
import math
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QGridLayout, QVBoxLayout, QPushButton, QLineEdit
)
from PyQt5.QtCore import Qt


class ScientificCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nexthikes Scientific Calculator")
        self.setGeometry(100, 100, 600, 420)
        self.setStyleSheet("background-color: black;")
        self.initUI()

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setStyleSheet(
            "background-color: lightgray; font-size: 24px; padding: 10px; font-weight: bold;"
        )
        self.main_layout.addWidget(self.display)

        self.grid_layout = QGridLayout()
        self.main_layout.addLayout(self.grid_layout)

        buttons = [
            '(', ')', 'C', '←', '%',
            '7', '8', '9', '/', 'sqrt',
            '4', '5', '6', '*', '^',
            '1', '2', '3', '-', '10^',
            '0', '.', '00', '+', '=',
            'sin', 'cos', 'tan', 'log', 'ln'
        ]

        positions = [(i, j) for i in range(6) for j in range(5)]
        for position, text in zip(positions, buttons):
            button = QPushButton(text)
            button.setStyleSheet(
                """
                QPushButton {
            background-color: #2c3e50;
            color: white;
            font-size: 18px;
            font-weight: bold;
            padding: 10px;
            border: 2px solid #34495e;
            border-radius: 5px;
            box-shadow: 3px 3px 5px #1a252f; /* Add shadow for 3D effect */
        }
        QPushButton:pressed {
            background-color: #34495e;
            box-shadow: inset 3px 3px 5px #1a252f; /* Inset shadow for pressed effect */
        }
                """
            )
            button.clicked.connect(self.on_click)
            self.grid_layout.addWidget(button, *position)

    def on_click(self):
        sender = self.sender().text()

        if sender == "=":
            try:
                expression = self.display.text()
                expression = expression.replace('sqrt', 'math.sqrt')
                expression = expression.replace('^', '**')
                expression = expression.replace('sin', 'math.sin(math.radians')
                expression = expression.replace('cos', 'math.cos(math.radians')
                expression = expression.replace('tan', 'math.tan(math.radians')
                expression = expression.replace('log', 'math.log10')
                expression = expression.replace('ln', 'math.log')
                result = eval(expression + ')') if 'math.radians' in expression else eval(expression)
                self.display.setText(str(result))
            except Exception:
                self.display.setText("Error")
        elif sender == "C":
            self.display.clear()
        elif sender == "←":
            self.display.setText(self.display.text()[:-1])
        else:
            self.display.setText(self.display.text() + sender)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = ScientificCalculator()
    calculator.show()
    sys.exit(app.exec_())
