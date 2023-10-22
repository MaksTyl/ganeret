from PyQt5.QtWidgets import (QApplication,QLabel,QRadioButton,
                            QHBoxLayout,QVBoxLayout, QWidget, QMessageBox)
from PyQt5.QtCore import Qt

WINSIZE = (600, 450)
TITLE = "TEST"
QW = "Яка тварина на планеті вважають безсмертною?"
ANSW = ["Макака", "Медуза", "Лев", "Дельфін"]

app = QApplication([])
win= QWidget()
win.resize(WINSIZE[0], WINSIZE[1])
win.setWindowTitle(TITLE)
win.move(600,200)

qw = QLabel(QW)
qw.setStyleSheet("color: red")
rbn_list= list()
for i in range(4):
    lbl = QRadioButton(ANSW[i])
    rbn_list.append(lbl)

lineh1 = QHBoxLayout()
lineh2 = QHBoxLayout()
lineh3 = QHBoxLayout()
main_line = QVBoxLayout()

lineh1.addWidget(qw, alignment=Qt.AlignCenter)
lineh2.addWidget(rbn_list[0], alignment=Qt.AlignCenter)
lineh2.addWidget(rbn_list[1], alignment=Qt.AlignCenter)
lineh3.addWidget(rbn_list[2], alignment=Qt.AlignCenter)
lineh3.addWidget(rbn_list[3], alignment=Qt.AlignCenter)
main_line.addLayout(lineh1)
main_line.addLayout(lineh2)
main_line.addLayout(lineh3)

def win_show():
    mes = QMessageBox()
    mes.setWindowTitle("win!")
    mes.setText("YOU WIN!")
    mes.show()
    mes.exec()
def lose_show():
    mes = QMessageBox()
    mes.setWindowTitle("lose!")
    mes.setText("YOU LOSE")
    mes.show()
    mes.exec()

rbn_list[0].clicked.connect(lose_show)
rbn_list[1].clicked.connect(win_show)



win.setLayout(main_line)
win.show()
app.exec()