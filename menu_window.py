from PyQt5.QtWidgets import *

import roma


def menu_window():
    window = QDialog()
    qest_lbl = QLabel("Ведіть запитаня")
    right_ans_lbl = QLabel("Ведіть правильну відповідь")
    light_ans_lbl = QLabel("Ведіть неправильну відповідь")
    light_ans_lbl1 = QLabel("Ведіть неправильну відповідь")
    light_ans_lbl2 = QLabel("Ведіть неправильну відповідь")
    qest_edit = QLineEdit()
    qest_edit1 = QLineEdit()
    qest_edit2 = QLineEdit()
    qest_edit3 = QLineEdit()
    qest_edit4 = QLineEdit()
    add_quest_btn = QPushButton("Добавити запитаня")
    main_line = QVBoxLayout()
    h1 = QHBoxLayout()
    h1.addWidget(qest_lbl)
    h1.addWidget(qest_edit)
    main_line.addLayout(h1)

    h2 = QHBoxLayout()
    h2.addWidget(right_ans_lbl)
    h2.addWidget(qest_edit1)
    main_line.addLayout(h2)

    h3 = QHBoxLayout()
    h3.addWidget(light_ans_lbl)
    h3.addWidget(qest_edit2)
    main_line.addLayout(h3)

    h4 = QHBoxLayout()
    h4.addWidget(light_ans_lbl1)
    h4.addWidget(qest_edit3)
    main_line.addLayout(h4)

    h5 = QHBoxLayout()
    h5.addWidget(light_ans_lbl2)
    h5.addWidget(qest_edit4)
    main_line.addLayout(h5)

    def add_quest_func():
        a ={
            "Запитаня": qest_edit.text(),
            "Правильна відповідь": qest_edit1.text(),
            "Неправилна відповідь 1": qest_edit2.text(),
            "Неправилна відповідь 2": qest_edit3.text(),
            "Неправилна відповідь 3": qest_edit4.text(),
        }
        roma.questons.append(a)
    main_line.addWidget(add_quest_btn)
    add_quest_btn.clicked.connect(add_quest_func)
    window.setLayout(main_line)

    main_line = QVBoxLayout()
    window.exec()

