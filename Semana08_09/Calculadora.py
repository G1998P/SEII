import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculadora')
        self.setLayout(qtw.QVBoxLayout())
        self.keypad()
        self.temp_nums = []
        self.fin_nums = []
        self.show()

    def keypad(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())

        # Botões
        self.equation_field = qtw.QLineEdit()
        self.result_field = qtw.QLineEdit()
        self.result_field.setText('0')
        btn_result = qtw.QPushButton('=', clicked = self.func_result)
        btn_del = qtw.QPushButton('DEL', clicked = self.del_calc)
        btn_clear = qtw.QPushButton('AC', clicked = self.clear_calc)
        btn_9 = qtw.QPushButton('9', clicked = lambda:self.num_press('9'))
        btn_8 = qtw.QPushButton('8', clicked = lambda:self.num_press('8'))
        btn_7 = qtw.QPushButton('7', clicked = lambda:self.num_press('7'))
        btn_6 = qtw.QPushButton('6', clicked = lambda:self.num_press('6'))
        btn_5 = qtw.QPushButton('5', clicked = lambda:self.num_press('5'))
        btn_4 = qtw.QPushButton('4', clicked = lambda:self.num_press('4'))
        btn_3 = qtw.QPushButton('3', clicked = lambda:self.num_press('3'))
        btn_2 = qtw.QPushButton('2', clicked = lambda:self.num_press('2'))
        btn_1 = qtw.QPushButton('1', clicked = lambda:self.num_press('1'))
        btn_0 = qtw.QPushButton('0', clicked = lambda:self.num_press('0'))
        btn_dot = qtw.QPushButton('.', clicked = lambda:self.num_press('.'))
        btn_plus = qtw.QPushButton('+', clicked = lambda:self.func_press('+'))
        btn_mins = qtw.QPushButton('-', clicked = lambda:self.func_press('-'))
        btn_mult = qtw.QPushButton('x', clicked = lambda:self.func_press('*'))
        btn_divd = qtw.QPushButton('÷', clicked = lambda:self.func_press('/'))
        btn_par_l = qtw.QPushButton('(', clicked = lambda:self.func_press('('))
        btn_par_d = qtw.QPushButton(')', clicked = lambda:self.func_press(')'))

        # Style
        btn_result.setStyleSheet(
            'background: #1a4cf1;'
            'color: white;'
        )
        btn_del.setStyleSheet(
            'background: #b4b4b4'
        )
        btn_clear.setStyleSheet(
            'background: #b4b4b4'
        )
        btn_plus.setStyleSheet(
            'background: #b4b4b4'
        )
        btn_mins.setStyleSheet(
            'background: #b4b4b4'
        )
        btn_mult.setStyleSheet(
            'background: #b4b4b4'
        )
        btn_divd.setStyleSheet(
            'background: #b4b4b4'
        )
        btn_par_l.setStyleSheet(
            'background: #b4b4b4'
        )    
        btn_par_d.setStyleSheet(
            'background: #b4b4b4'
        ) 
        # Adicionando os botões ao layout
        container.layout().addWidget(self.equation_field,0,0,1,4)
        container.layout().addWidget(self.result_field,1,0,1,4)
        container.layout().addWidget(btn_par_l,2,0)
        container.layout().addWidget(btn_par_d,2,1)
        container.layout().addWidget(btn_del,2,2)
        container.layout().addWidget(btn_clear,2,3)
        container.layout().addWidget(btn_9,3,0)
        container.layout().addWidget(btn_8,3,1)
        container.layout().addWidget(btn_7,3,2)
        container.layout().addWidget(btn_divd,3,3)
        container.layout().addWidget(btn_6,4,0)
        container.layout().addWidget(btn_5,4,1)
        container.layout().addWidget(btn_4,4,2)
        container.layout().addWidget(btn_mult,4,3)
        container.layout().addWidget(btn_3,5,0)
        container.layout().addWidget(btn_2,5,1)
        container.layout().addWidget(btn_1,5,2)
        container.layout().addWidget(btn_mins,5,3)
        container.layout().addWidget(btn_0,6,0)
        container.layout().addWidget(btn_dot,6,1)
        container.layout().addWidget(btn_result,6,2)
        container.layout().addWidget(btn_plus,6,3)
        self.layout().addWidget(container)

    def num_press(self,key_number):
        self.temp_nums.append(key_number)
        temp_string = ''.join(self.temp_nums)
        if self.fin_nums:
            self.equation_field.setText(''.join(self.fin_nums)+temp_string)
        else:
             self.equation_field.setText(temp_string)

    def func_press(self, operator):
            temp_string = ''.join(self.temp_nums)
            self.fin_nums.append(temp_string)
            self.fin_nums.append(operator)
            self.temp_nums = []
            self.equation_field.setText(''.join(self.fin_nums))


    def func_result(self):
        try:
            fin_string = ''.join(self.fin_nums) + ''.join(self.temp_nums)
            result_field = eval(fin_string)
            self.result_field.setText(str(result_field))
        except Exception as ex:
            template = "{0}:{1}"
            message = template.format(type(ex).__name__, ex.args[0])
            self.result_field.setText(message)

    def del_calc(self):
        try:
            if self.temp_nums:
                self.temp_nums.pop()
                self.equation_field.setText(''.join(self.fin_nums) +''.join(self.temp_nums))
            else:
                self.fin_nums.pop()
                self.equation_field.setText(''.join(self.fin_nums))
        except:
            self.equation_field.clear()
    
    def clear_calc(self):
        self.temp_nums = []
        self.fin_nums = []
        self.equation_field.clear()
        self.result_field.setText('0')

if __name__ == '__main__':
	app = qtw.QApplication([])
	mw = MainWindow()
	app.setStyle(qtw.QStyleFactory.create('Fusion'))
	app.exec_()
