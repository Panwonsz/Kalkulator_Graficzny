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


class Calculator:
    def __init__(self):
        self.app = QApplication([])
        self.window = QWidget()
        self.layout = QGridLayout()
        self.output1 = WidgetMaker.create_output_line()
        self.output1_text = ""
        self.output2 = WidgetMaker.create_output_line(1)
        self.output2_text = ""
        self.operation_active=0
        self.val1=0
        self.val2=0
        self.wynik=0
        self.oper="="
        self.edit_reset=False
        self.buttons = {}
        self.set_buttons()
        self.set_layout()

    def button_clicked_number(self, text):
        if ((self.operation_active==1) and self.edit_reset ) :  self.output1_text=""
        self.output1_text += text
        self.output1.setText(self.output1_text)
        self.edit_reset=False

    def button_clicked_clr(self, text):
        self.operation_active = 0
        self.oper="="
        self.output1_text = ""
        self.output2_text = ""
        self.output1.setText("")
        self.output2.setText("")

    def button_clicked_operation(self, text):
        #self.output2.setText(self.output1_text + text)
        if ( self.edit_reset) :
            self.output2.setText(str ( self.output1_text ) + self.oper + str ( self.output2_text ) + " = " + str(self.wynik) + "   :"+text)
            self.oper=text
        else :

            if ( self.operation_active == 0 ):
                self.output2.setText(str ( self.output1_text ) + text)
                self.oper=text
                self.operation_active+=1
                self.edit_reset=True
            elif (  self.operation_active == 1 ):
                self.val2=int(self.output1_text)
                self.wynik=int(self.val1)+int(self.output1_text)
                wynik_text=str(self.wynik)
                self.output2.setText(str ( self.val1 ) + self.oper + str ( self.val2 ) + " = " + wynik_text + "   :"+text)
                self.output1.setText( wynik_text  )
                self.val1=self.wynik
                self.output1_text = wynik_text
                self.edit_reset=True
                self.oper=text
                #self.operation_active+=1
                #self.operation_active=0

        #self.output2.setText(self.output1_text + text)
        #self.operation_active=True






    def set_layout(self):
        self.layout.addWidget(self.buttons['plus'], 7, 2)
        self.layout.addWidget(self.buttons['minus'], 7, 3)
        self.layout.addWidget(self.buttons['mnoz'], 7, 4)
        self.layout.addWidget(self.buttons['dziel'], 7, 5)
        self.layout.addWidget(self.buttons['eq'], 7, 6)
        self.layout.addWidget(self.buttons['pow'], 8, 4)
        self.layout.addWidget(self.buttons['sqrt'], 8, 5)
        self.layout.addWidget(self.buttons['sin'], 8, 2)
        self.layout.addWidget(self.buttons['cos'], 8, 3)
        self.layout.addWidget(self.buttons['('], 1, 5)
        self.layout.addWidget(self.buttons[')'], 2, 5)
        self.layout.addWidget(self.buttons['CLR'], 8, 0)

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
        self.layout.addWidget(self.output1, 1, 0)
        self.layout.addWidget(self.output2, 2, 0)

    def set_buttons(self):
        self.buttons ={
            '1': WidgetMaker.create_button('1', lambda: self.button_clicked_number("1")),
            '2': WidgetMaker.create_button('2', lambda: self.button_clicked_number("2")),
            '3': WidgetMaker.create_button('3', lambda: self.button_clicked_number("3")),
            '4': WidgetMaker.create_button('4', lambda: self.button_clicked_number("4")),
            '5': WidgetMaker.create_button('5', lambda: self.button_clicked_number("5")),
            '6': WidgetMaker.create_button('6', lambda: self.button_clicked_number("6")),
            '7': WidgetMaker.create_button('7', lambda: self.button_clicked_number("7")),
            '8': WidgetMaker.create_button('8', lambda: self.button_clicked_number("8")),
            '9': WidgetMaker.create_button('9', lambda: self.button_clicked_number("9")),
            '0': WidgetMaker.create_button('0', lambda: self.button_clicked_number("0")),
            'CLR': WidgetMaker.create_button('CLR', lambda: self.button_clicked_clr("clear")),
            'sin': WidgetMaker.create_button('sin(x)', lambda: self.button_clicked_operation("sin(")),
            'cos': WidgetMaker.create_button('cos(x)', lambda: self.button_clicked_operation("cos(")),
            'tan': WidgetMaker.create_button('tan', lambda: self.button_clicked_operation("tan(")),
            'ctan': WidgetMaker.create_button('ctan', lambda: self.button_clicked_operation("ctan(")),
            'plus': WidgetMaker.create_button('+', lambda: self.button_clicked_operation("+")),
            'pow': WidgetMaker.create_button('^', lambda: self.button_clicked_operation("^")),
            '(': WidgetMaker.create_button('(', lambda: self.button_clicked_operation("(")),
            ')': WidgetMaker.create_button(')', lambda: self.button_clicked_operation(")")),
            'sqrt': WidgetMaker.create_button('sqrt', lambda: self.button_clicked_operation("sqrt")),
            'minus': WidgetMaker.create_button('-', lambda: self.button_clicked_operation("-")),
            'mnoz': WidgetMaker.create_button('*', lambda: self.button_clicked_operation("*")),
            'dziel': WidgetMaker.create_button('/', lambda: self.button_clicked_operation("/")),
            'eq': WidgetMaker.create_button('=', lambda: self.button_clicked_operation("=")),


        }

    def run(self):
        self.window.setLayout(self.layout)
        self.window.show()
        self.app.exec_()

app=Calculator()
app.run()
