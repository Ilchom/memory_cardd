from random import *
from PyQt5.QtCore  import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QMessageBox, QListWidget, QGroupBox, QButtonGroup

class Question():
    def __init__(self, qust, r_answer, answ1, answ2, ansv3):
        self.qust = qust
        self.r_answer = r_answer
        self.wrong1 = answ1
        self.wrong2 = answ2
        self.wrong3 = ansv3

def showquestion():
    RadioGroupBox.show()
    AnswGroupBox.hide()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    otvet1.setChecked(False)
    otvet2.setChecked(False)
    otvet3.setChecked(False)
    otvet4.setChecked(False)
    RadioGroup.setExclusive(True)

    
def showresult():
    RadioGroupBox.hide()
    AnswGroupBox.show()
    button.setText('Следующий вопрос')

def clicc_OK():
    if button.text() == 'Ответить':
        chec_answer()
    else:
        next_question()
def show_correct(res):
    lb_Quest1.setText(res)
    showresult()
def chec_answer():
    global score
    global lose
    if spisok[0].isChecked():
        show_correct('Правильно')
        score += 1
    else:
        if spisok[1].isChecked() or spisok[2].isChecked() or spisok[3].isChecked():
            show_correct('WRONG')
        lose += 1
    if len(question_list) == 0:
        print('Правильных ответоов:', score)
        print('Неправильных ответов:', lose)

def next_question():
    global d
    d = randint(0, len(question_list) - 1)
    q = question_list[d]
    ask(q)
    question_list.remove(question_list[d])
    
        
    



app  = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory card')
RadioGroupBox = QGroupBox('Варианты ответов')
question = QLabel('вопрос')
button = QPushButton('Ответить')
otvet1 = QRadioButton('ответ1')
otvet2 = QRadioButton('ответ2')
otvet3 = QRadioButton('ответ3')
otvet4 = QRadioButton('ответ4')

layout_ans1 = QVBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()

spisok = [otvet1, otvet2, otvet3, otvet4]
def ask(q: Question):
    shuffle(spisok)
    spisok[0].setText(q.r_answer)
    spisok[1].setText(q.wrong1)
    spisok[2].setText(q.wrong2)
    spisok[3].setText(q.wrong3)
    question.setText(q.qust)
    lb_Quest2.setText(q.r_answer)
    showquestion()


layout_ans2.addWidget(otvet1)
layout_ans2.addWidget(otvet2)
layout_ans3.addWidget(otvet3)
layout_ans3.addWidget(otvet4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

AnswGroupBox = QGroupBox('результаты')
lb_Quest1 = QLabel('правильно/ неправильно')
lb_Quest2 = QLabel('правильноый ответ')
v_line = QVBoxLayout()
v_line.addWidget(lb_Quest1)
v_line.addWidget(lb_Quest2)

RadioGroupBox.setLayout(layout_ans1)
AnswGroupBox.hide()
AnswGroupBox.setLayout(v_line)

aaa = QVBoxLayout()
aaa.addWidget(question)
aaa.addWidget(RadioGroupBox)
aaa.addWidget(AnswGroupBox)
aaa.addWidget(button)

RadioGroup = QButtonGroup()
RadioGroup.addButton(otvet1)
RadioGroup.addButton(otvet2)
RadioGroup.addButton(otvet3)
RadioGroup.addButton(otvet4)

RadioGroup.setExclusive(False)
otvet1.setChecked(False)
otvet2.setChecked(False)
otvet3.setChecked(False)
otvet4.setChecked(False)
RadioGroup.setExclusive(True)

q = Question('ыфвтфдывтфоывтофыты?', "апролоаапаваааааааааааааааааааааааа", "фыаф", "фывывффывфывфыы", "фывфывфыв")

ask(q)

question_list = []
q1 = Question('В 1900 году был открыт очередной астероид, который получил название Матезида. В честь чего его назвали?', 'Богиня', 'Наука', 'Созвездие', 'Растение')
question_list.append(q1)
q2 = Question('Какая кошка самая большая на планете?', "Тигр", 'Лев', 'гепард', 'леопард')
question_list.append(q2)
q3 = Question('Какое сухопутное животное может открыть рот максимально широко?', 'бегемот', 'Крокодил', 'Бабуин', 'лев')
question_list.append(q3)
q4 = Question('Какое животное самое крупное на Земле?', 'Синий кит', 'Бегемот', 'Жираф', 'анаконда')
question_list.append(q4)
q5 = Question('Какое млекопитающее умеет летать?', 'Летучая мышь', 'Белка-летяга', 'Белоголовый орлан', 'Колуго')
question_list.append(q5)
q6 = Question('Как называется животное, которое употребляет в пищу растения и мясо?', 'Всеядное животное', 'Травоядное', 'Плотоядное', 'не придумал')
question_list.append(q6)
q7 = Question('Почему каланы («морские выдры») держатся за руки?', 'Чтобы они не уплывали, когда спят', 'любят друг друга', 'наделаи наручники', 'Потому что они играют')
question_list.append(q7)
q8 = Question('Как отличить насекомое от паука?', 'Все вышеперечисленные факты', 'У насекомых шесть ног, у пауков – восемь', 'У насекомых могут быть крылья, у пауков они отсутствуют', 'У насекомых три части тела, у пауков – две')
question_list.append(q8)
q9 = Question('Чем утконос отличается от других млекопитающих?', 'Откладывает яйца', 'Крякает, как утка', 'Ковыляет', 'Строит гнезда')
question_list.append(q9)
q10 = Question('На какой позиции находится марс от солнца', '4', '2', '1', '3')
question_list.append(q10)

main_win.cur_question = -1
d = 0
score = 0
lose = 0

button.clicked.connect(clicc_OK)
next_question()
main_win.setLayout(aaa)
main_win.show()
app.exec_()