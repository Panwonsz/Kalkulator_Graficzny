from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QLineEdit, QGridLayout


class WidgetMaker:
    @staticmethod
    def create_button(text, bind_function=None):
        button = QPushButton(text)
        if bind_function:
            button.clicked.connect(bind_function)
        return button

    @staticmethod
    def create_output_line(is_readonly=0):
        line = QLineEdit("")
        line.setReadOnly(is_readonly)
        return line


class Calculator:
    def __init__(self):
        self.app = QApplication([])
        self.window = QWidget()
        self.layout = QGridLayout()
        self.output1 = WidgetMaker.create_output_line()
        self.output1_text = ""
        self.output2 = WidgetMaker.create_output_line(1)
        self.output2_text = ""
        self.buttons = {}
        self.set_buttons()
        self.set_layout()

    def button_clicked(self, text):
        self.output1_text += text
        self.output1.setText(self.output1_text)

    def set_layout(self):
        self.layout.addWidget(self.buttons['sin'], 1, 1)
        self.layout.addWidget(self.buttons['cos'], 2, 1)
        self.layout.addWidget(self.buttons['1'], 1, 2)
        self.layout.addWidget(self.buttons['2'], 1, 3)
        self.layout.addWidget(self.buttons['3'], 1, 4)
        self.layout.addWidget(self.buttons['4'], 2, 2)
        self.layout.addWidget(self.buttons['5'], 2, 3)
        self.layout.addWidget(self.buttons['6'], 2, 4)
        self.layout.addWidget(self.buttons['7'], 3, 2)
        self.layout.addWidget(self.buttons['8'], 3, 3)
        self.layout.addWidget(self.buttons['9'], 3, 4)
        self.layout.addWidget(self.buttons['0'], 4, 3)
        self.layout.addWidget(self.output1, 5, 5)
        self.layout.addWidget(self.output2, 6, 5)

    def set_buttons(self):
        self.buttons ={
            '1': WidgetMaker.create_button('1', lambda: self.button_clicked("1")),
            '2': WidgetMaker.create_button('2', lambda: self.button_clicked("2")),
            '3': WidgetMaker.create_button('3', lambda: self.button_clicked("3")),
            '4': WidgetMaker.create_button('4', lambda: self.button_clicked("4")),
            '5': WidgetMaker.create_button('5', lambda: self.button_clicked("5")),
            '6': WidgetMaker.create_button('6', lambda: self.button_clicked("6")),
            '7': WidgetMaker.create_button('7', lambda: self.button_clicked("7")),
            '8': WidgetMaker.create_button('8', lambda: self.button_clicked("8")),
            '9': WidgetMaker.create_button('9', lambda: self.button_clicked("9")),
            '0': WidgetMaker.create_button('0', lambda: self.button_clicked("0")),
            'sin': WidgetMaker.create_button('sin(x)', lambda: self.button_clicked("sin(x)")),
            'cos': WidgetMaker.create_button('cos(x)', lambda: self.button_clicked("cos(x)")),
        }

    def run(self):
        self.window.setLayout(self.layout)
        self.window.show()
        self.app.exec_()

app=Calculator()
app.run()
