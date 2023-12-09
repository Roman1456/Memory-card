from PyQt5.QtWidgets import *

app = QApplication([])

window = QWidget()
window.resize(700,500)

menu_btn = QPushButton("Меню")
grou_box = QGroupBox("Вікно")
spin_box = QSpinBox()


window.show()
app.exec()






