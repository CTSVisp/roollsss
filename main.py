import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox
from PyQt6.QtCore import Qt
import random


class DiceRollSimulator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Симуляция N количества бросков')
        self.setGeometry(500, 500, 400, 230)

        self.layout = QVBoxLayout()

        self.num_dice_label = QLabel('Сколько кубиков?')
        self.layout.addWidget(self.num_dice_label)
        self.num_dice_input = QLineEdit()
        self.layout.addWidget(self.num_dice_input)

        self.num_rolls_label = QLabel('Сколько бросков?')
        self.layout.addWidget(self.num_rolls_label)
        self.num_rolls_input = QLineEdit()
        self.layout.addWidget(self.num_rolls_input)

        self.simulate_button = QPushButton('Посчитать')
        self.simulate_button.clicked.connect(self.simulateDiceRoll)
        self.layout.addWidget(self.simulate_button)

        self.result_label = QLabel('')
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)

        self.num_dice_input.textChanged.connect(self.validateInput)
        self.num_rolls_input.textChanged.connect(self.validateInput)

    def validateInput(self):
        sender = self.sender()
        if sender.text() and not sender.text().isdigit():
            sender.clear()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setText("Для ввода поддерживаются только числа")
            msg.setWindowTitle("Неподходящие символы")
            msg.exec()

    def simulateDiceRoll(self):
        num_dice = int(self.num_dice_input.text())
        num_rolls = int(self.num_rolls_input.text())

        results = {}
        for _ in range(num_rolls):
            total = sum(random.randint(1, 6) for _ in range(num_dice))
            results[total] = results.get(total, 0) + 1
        output = ''
        for key in sorted(results.keys()):
            percentage = (results[key] / num_rolls) * 100
            output += f"Сумма чисел={key}: с шансом {percentage:.2f}%\n"
        self.result_label.setText(output)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    simulator = DiceRollSimulator()
    simulator.show()
    sys.exit(app.exec())
