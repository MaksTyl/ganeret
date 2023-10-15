from PyQt5.QtWidgets import QApplication,QLabel,QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from random import randint

app = QApplication([])
win = QWidget()
win.resize(300,300)
win.move(100,100)
win.setWindowTitle("Loterey")

main_L = QVBoxLayout()

lbl_mes = QLabel("Press to start")
lbl_num1 = QLabel("?")
lbl_num2 = QLabel("?")
btn = QPushButton("Start")

main_L.addWidget(lbl_mes, alignment=Qt.AlignCenter)
main_L.addWidget(lbl_num1, alignment=Qt.AlignCenter)
main_L.addWidget(lbl_num2, alignment=Qt.AlignCenter)
main_L.addWidget(btn, alignment=Qt.AlignCenter)

def start():
    num1 = randint(0,9)
    num2 = randint(0,9)
    lbl_num1.setText(str(num1))
    lbl_num2.setText(str(num2))
    if num1==num2:
        lbl_num2.setText("Win!")
    else:
        lbl_num2.setText("Try again")

btn.clicked.connect(start)

win.setLayout(main_L)
win.show()
app.exec()