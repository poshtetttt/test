from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

def show_winner():
    number = randint(0, 99)
    winner.setText(str(number))
    text.setText('Победитель:')

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Определитель победителя')
button = QPushButton('Сгенерировать')
text = QLabel('Нажми, чтобы узнать победителя')
winner = QLabel('?')

line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(button, alignment = Qt.AlignCenter)
main_win.setLayout(line)



main_win.show()
app.exec_()
