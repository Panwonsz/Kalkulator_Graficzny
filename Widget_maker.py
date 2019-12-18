from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QLineEdit, QGridLayout
from PyQt5.QtGui import QIntValidator ,  QDoubleValidator

class WidgetMaker:
    @staticmethod
    def create_button(text, bind_function=None):
        button = QPushButton(text)
        if bind_function:
            button.clicked.connect(bind_function)
        return button

    @staticmethod
    def create_output_line(is_readonly=0):
        line = QLineEdit("0")
        line.setReadOnly(is_readonly)
        line.setValidator(QDoubleValidator())
        return line
