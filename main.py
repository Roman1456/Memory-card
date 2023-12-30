import random

from PyQt5.QtWidgets import *

import roma
import menu_window
import bublig
app = QApplication([])

window = QWidget()
window.resize(700,500)

menu_btn = QPushButton("Меню")
change_btn = QPushButton("Змінити")
next_quest_btn = QPushButton("Наступне запитаня")
grou_box = QGroupBox("Варіанти відповідей")
spin_box = QSpinBox()
qesting_lbl = QLabel("Яблуко")
answer1_btn = QRadioButton("Bu4rlding")
answer2_btn = QRadioButton("home")
answer3_btn = QRadioButton("applicate")
answer4_btn = QRadioButton("apple")
resulat_lbl = QLabel("Результат")
resulat_lbl.hide()

answer = [answer1_btn,answer2_btn,answer3_btn,answer4_btn]
random.shuffle(answer)

vidpovist_btn = QPushButton("Відповісти")

mine_line = QVBoxLayout()

h1 = QHBoxLayout()
h1.addWidget(menu_btn)
h1.addWidget(change_btn)
h1.addStretch(1)
mine_line.addLayout(h1)
mine_line.addWidget(qesting_lbl)

group_line = QVBoxLayout()

group_line.addWidget(answer[0])
group_line.addWidget(answer[1])
group_line.addWidget(answer[2])
group_line.addWidget(answer[3])
group_line.addWidget(resulat_lbl)
grou_box.setLayout(group_line)


mine_line.addWidget(grou_box)
mine_line.addWidget(vidpovist_btn)
mine_line.addWidget(next_quest_btn)
window.setLayout(mine_line)

def set_questons():
    num = roma.questons_number
    qesting_lbl.setText(roma.questons[num]["Запитаня"])
    answer[0].setText(roma.questons[num]["Правильна відповідь"])
    answer[1].setText(roma.questons[num]["Неправилна відповідь 1"])
    answer[2].setText(roma.questons[num]["Неправилна відповідь 2"])
    answer[3].setText(roma.questons[num]["Неправилна відповідь 3"])
set_questons()

def answer_click():
    if answer[0].isChecked():
        resulat_lbl.setText("Правильно")


    else:
        resulat_lbl.setText("Неправильно")
    resulat_lbl.show()
    answer[0].hide()
    answer[1].hide()
    answer[2].hide()
    answer[3].hide()


def next_quest_func():
    roma.questons_number+=1
    set_questons()

def menu_show():
    window.hide()
    menu_window.menu_window()
    window.show()

def change_show():
    window.hide()
    bublig.chank_window()
    window.show()
    set_questons()

menu_btn.clicked.connect(menu_show)
change_btn.clicked.connect(change_show)
vidpovist_btn.clicked.connect(answer_click)
next_quest_btn.clicked.connect(next_quest_func)
window.show()
app.exec()






