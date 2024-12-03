import sys
import math
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QGridLayout, QVBoxLayout, QWidget, QPushButton, QLineEdit
)
from PyQt5.QtCore import Qt


class ScientificCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scientific Calculator")
        self.setGeometry(100, 100, 400, 500)
        self.initUI()

    def initUI(self):
        # Main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        # Display
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setStyleSheet("font-size: 24px; padding: 10px;")
        self.main_layout.addWidget(self.display)

        # Button grid layout
        self.grid_layout = QGridLayout()
        self.main_layout.addLayout(self.grid_layout)

        # Buttons
        buttons = [
            '7', '8', '9', '/', 'sin',
            '4', '5', '6', '*', 'cos',
            '1', '2', '3', '-', 'tan',
            '0', '.', '=', '+', 'C',
            'log', 'sqrt', '(', ')', 'pi'
        ]

        # Add buttons to grid
        positions = [(i, j) for i in range(6) for j in range(5)]
        for position, text in zip(positions, buttons):
            button = QPushButton(text)
            button.setStyleSheet("font-size: 18px; padding: 15px;")
            button.clicked.connect(self.on_click)
            self.grid_layout.addWidget(button, *position)

    def on_click(self):
        sender = self.sender().text()
        if sender == "=":
            try:
                expression = self.display.text()
                # Replace custom constants
                expression = expression.replace('pi', str(math.pi))
                result = eval(expression)
                self.display.setText(str(result))
            except Exception:
                self.display.setText("Error")
        elif sender == "C":
            self.display.clear()
        elif sender == "sin":
            try:
                value = eval(self.display.text())
                self.display.setText(str(math.sin(math.radians(value))))
            except Exception:
                self.display.setText("Error")
        elif sender == "cos":
            try:
                value = eval(self.display.text())
                self.display.setText(str(math.cos(math.radians(value))))
            except Exception:
                self.display.setText("Error")
        elif sender == "tan":
            try:
                value = eval(self.display.text())
                self.display.setText(str(math.tan(math.radians(value))))
            except Exception:
                self.display.setText("Error")
        elif sender == "log":
            try:
                value = eval(self.display.text())
                self.display.setText(str(math.log10(value)))
            except Exception:
                self.display.setText("Error")
        elif sender == "sqrt":
            try:
                value = eval(self.display.text())
                self.display.setText(str(math.sqrt(value)))
            except Exception:
                self.display.setText("Error")
        else:
            # Append button text to the display
            self.display.setText(self.display.text() + sender)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = ScientificCalculator()
    calculator.show()
    sys.exit(app.exec_())
