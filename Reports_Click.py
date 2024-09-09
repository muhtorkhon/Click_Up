from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Reports_(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(1700,900)
        self.setStyleSheet("backgraund:lightgray;font-size:20px")

        m_lay = QVBoxLayout()


        self.btn1 = QPushButton("2024 yil aprel")
        self.btn2 = QPushButton('2024 yil may')
        self.btn3 = QPushButton('2024 yil iyun')
        self.btn4 = QPushButton('2024 yil iyul')
        self.btn5 = QPushButton('2024 yil avgust')
        self.btn6 = QPushButton('2024 yil sentyabr')


        self.btn1.clicked.connect(lambda: self.BTN("2024 yil aprel"))
        self.btn2.clicked.connect(lambda: self.BTN("2024 yil may"))
        self.btn3.clicked.connect(lambda: self.BTN("2024 yil iyun"))
        self.btn4.clicked.connect(lambda: self.BTN("2024 yil iyul"))
        self.btn5.clicked.connect(lambda: self.BTN("2024 yil avgust"))
        self.btn6.clicked.connect(lambda: self.BTN("2024 yil sentyabr"))


        lstlar = QHBoxLayout()
        lst = [self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6]
        for i in lst:
            lstlar.addWidget(i)
            i.setStyleSheet("background:skyblue")
        m_lay.addLayout(lstlar)


        self.label = QLabel('Ushbu davr mobaynida hech qanday tranzaksiya yo\'q.')
        m_lay.addWidget(self.label)


        # image_label = QLabel(self)
        # pixmap = QPixmap("C:/path/to/your/image.png")  
        # image_label.setPixmap(pixmap)
        # image_label.setScaledContents(True)
        # m_lay.addWidget(image_label)

        button_push = QHBoxLayout()
        chiqish_btn = QPushButton("CHIQISH")
        chiqish_btn.clicked.connect(self.close)
        button_push.addWidget(chiqish_btn)
        m_lay.addLayout(button_push)

        self.setLayout(m_lay)

    def BTN(self, month):
        self.label.setText(f"Ma'lumot: {month} oyida tranzaksiyalar mavjud.")
        if month=="2024 yil sentyabr":
            self.label.setText(f"Ma'lumot: {month} ")






if __name__ == "__main__":
  app = QApplication([])
  win = Reports_()
  win.show()
  app.exec_()