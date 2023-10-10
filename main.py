from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from random import randint

app = QApplication([])
win = QWidget()
win.resize(400,400)
win.setWindowTitle("Generator")
mainLine = QVBoxLayout()

lbl = QLabel("Generaye number of winner")
lblWin = QLabel("?")
btn = QPushButton("Generate wiiner")

mainLine.addWidget(lbl, alignment=Qt.AlignCenter)
mainLine.addWidget(lblWin, alignment=Qt.AlignCenter)
mainLine.addWidget(btn, alignment=Qt.AlignCenter)

def winnerShow():
    num = randint(1,1000)
    lbl.setText("Winner")
    lblWin.setText(str(num))

btn.clicked.connect(winnerShow)

win.setLayout(mainLine)
win.show()
app.exec()