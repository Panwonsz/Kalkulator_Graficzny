from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QLineEdit, QGridLayout
###############################################################


def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec_()


def button_clicked(x):
    l1.setText(x)
    l2.setText(x)
    l2.setReadOnly(1)


##############################################################
app = QApplication([])
#app.setStyleSheet("QPushButton { margin: 100px; }")
#app.setStyleSheet("QPushButton { margin: 10ex; }")
#app.setStyleSheet("QPushButton { margin-left: 20px; }")
#app.setStyleSheet("QPushButton { margin-right: 40px; margin-left: 20px; }")
window = QWidget()
bsin = QPushButton('sin(x)')
bcos = QPushButton('cos(x)')
Top = QPushButton('Top')
Bottom = QPushButton('Bottom')
bn1 = QPushButton('1')
bn2 = QPushButton('2')
bn3 = QPushButton('3')
bn4 = QPushButton('4')
bn5 = QPushButton('5')
bn6 = QPushButton('6')
bn7 = QPushButton('7')
bn8 = QPushButton('8')
bn9 = QPushButton('9')
bn0 = QPushButton('0')
l1 = QLineEdit("")
l2 = QLineEdit("")
bsin.clicked.connect(on_button_clicked)
bcos.clicked.connect(on_button_clicked)
Top.clicked.connect(lambda: button_clicked("TOP"))
Bottom.clicked.connect(lambda: button_clicked("BOTTOM"))
bn1.clicked.connect(lambda: button_clicked("1"))
bn2.clicked.connect(lambda: button_clicked("2"))
bn3.clicked.connect(lambda: button_clicked("3"))
bn4.clicked.connect(lambda: button_clicked("4"))
bn5.clicked.connect(lambda: button_clicked("5"))
bn6.clicked.connect(lambda: button_clicked("6"))
bn7.clicked.connect(lambda: button_clicked("7"))
bn8.clicked.connect(lambda: button_clicked("8"))
bn9.clicked.connect(lambda: button_clicked("9"))
bn0.clicked.connect(lambda: button_clicked("0"))
layout = QGridLayout()
layout.addWidget(Top,1,0)
layout.addWidget(Bottom,2,0)
layout.addWidget(bsin,1,1)
layout.addWidget(bcos,2,1)
layout.addWidget(bn1,1,2)
layout.addWidget(bn2,1,3)
layout.addWidget(bn3,1,4)
layout.addWidget(bn4,2,2)
layout.addWidget(bn5,2,3)
layout.addWidget(bn6,2,4)
layout.addWidget(bn7,3,2)
layout.addWidget(bn8,3,3)
layout.addWidget(bn9,3,4)
layout.addWidget(bn0,4,3)
layout.addWidget(l1,5,5)
layout.addWidget(l2,6,5)
window.setLayout(layout)
window.show()
app.exec_()