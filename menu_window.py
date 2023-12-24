from PyQt5.QtWidgets import *

import roma


def menu_window():
    window = QDialog()
    qest_lbl = QLabel("Ведіть запитаня")
    right_ans_lbl = QLabel("Ведіть правильну відповідь")
    right_ans_lb
    qest_edit = QLineEdit()
    qest_edit1 = QLineEdit()
    qest_edit2 = QLineEdit()
    qest_edit3 = QLineEdit()
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
    h3.addWidget()



    def add_quest_func():
        a ={
            "Запитаня": qest_edit.text(),
            "Правильна відповідь": qest_edit1.text(),
            "Неправилна відповідь 1": "",
            "Неправилна відповідь 2": "",
            "Неправилна відповідь 3": "",
        }
        roma.questons.append(a)
    main_line.addWidget(add_quest_btn)
    add_quest_btn.clicked.connect(add_quest_func)
    window.setLayout(main_line)

    main_line = QVBoxLayout()
    window.exec()

