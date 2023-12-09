import random

from PyQt5.QtWidgets import *

app = QApplication([])

window = QWidget()
window.resize(700,500)

menu_btn = QPushButton("Меню")
grou_box = QGroupBox("Варіанти відповідей")
spin_box = QSpinBox()
qesting_lbl = QLabel("Яблуко")
answer1_btn = QRadioButton("Bu4rlding")
answer2_btn = QRadioButton("home")
answer3_btn = QRadioButton("applicate")
answer4_btn = QRadioButton("apple")

answer = [answer1_btn,answer2_btn,answer3_btn,answer4_btn]
random.shuffle(answer)

vidpovist_btn = QPushButton("Відповісти")

mine_line = QVBoxLayout()

h1 = QHBoxLayout()
h1.addWidget(menu_btn)
h1.addStretch(1)
mine_line.addLayout(h1)
mine_line.addWidget(qesting_lbl)

group_line = QVBoxLayout()
group_line.addWidget(answer[0])
group_line.addWidget(answer[1])
group_line.addWidget(answer[2])
group_line.addWidget(answer[3])
grou_box.setLayout(group_line)

mine_line.addWidget(grou_box)

window.setLayout(mine_line)
window.show()
app.exec()






