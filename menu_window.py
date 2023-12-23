from PyQt5.QtWidgets import *

import roma


def menu_window():
    window = QDialog()
    qest_lbl = QLabel("Ведіть запитаня")
    right_ans_lbl = QLabel("Ведіть правильну відповідь")
    qest_edit = QLineEdit()
    right_ans_edit = QLineEdit()
    add_quest_btn = QPushButton("Добавити запитаня")
    main_line = QVBoxLayout()
    h1 = QHBoxLayout()
    h1.addWidget(qest_lbl)
    h1.addWidget(qest_edit)
    main_line.addLayout(h1)

    def add_quest_func():
        a ={
            "Запитаня": qest_edit.text(),
            "Правильна відповідь": "",
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

