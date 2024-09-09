from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random
from main import *
from Payment_Click import *
from payme_mobil import *
from Reports_Click import *
from Settings_Click import *
from Transfers_Click import *


class Login(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(1700,900)
        self.setStyleSheet("background:#fff;font-size:20px")

        self.h_lbl_lyt = QHBoxLayout()
        self.v_main_lyt = QVBoxLayout()
        self.v_asos_lyt = QVBoxLayout()
        self.rekursi()

    def rekursi(self):
        self.llbl = QLabel("Avtorizatsiyalash va ro'yxatdan o'tish bitta darchada")
        self.llbl.setStyleSheet("font-size:24px;color:rgb(51,51,51)")
        self.ledit = QLineEdit()
        self.ledit.setPlaceholderText("Telefon raqam")
        self.ledit.setStyleSheet("background:lightgray")

        self.cledit = QLineEdit()
        self.cledit.setPlaceholderText("Codni kiriting")
        self.cledit.setStyleSheet("background:lightgray")
        self.cledit.hide()

        self.lbtn = QPushButton("Kirish",clicked=self.kirish)
        self.lbtn.setStyleSheet("background:skyblue")

        self.klbtn = QPushButton("Kirish ",clicked=self.checkk)
        self.klbtn.setStyleSheet("background:skyblue")
        self.klbtn.hide()


        self.v_main_lyt.addWidget(self.llbl)
        self.v_main_lyt.addWidget(self.ledit)
        self.v_main_lyt.addWidget(self.cledit)
        self.v_main_lyt.addWidget(self.lbtn)
        self.v_main_lyt.addWidget(self.klbtn)

        self.h_lbl_lyt.addStretch()
        self.h_lbl_lyt.addLayout(self.v_main_lyt)
        self.h_lbl_lyt.addStretch()

        self.v_asos_lyt.addStretch()
        self.v_asos_lyt.addLayout(self.h_lbl_lyt)
        self.v_asos_lyt.addStretch()

        self.setLayout(self.v_asos_lyt)

    def kirish(self):
        self.ledit.hide()
        self.cledit.show()

        self.lbtn.hide()
        self.klbtn.show()


        self.rson = random.randint(100000, 999999)
        self.cledit.setText(f"{self.rson}")
        self.mgs = QMessageBox()
        self.mgs.move(300,400)
        self.mgs.setWindowTitle("Shaxsiy parol")
        self.mgs.setText(f"Parol\n{self.rson}")
        self.mgs.setIcon(QMessageBox.Information)
        self.mgs.exec_()

    def checkk(self):
        
        if str(self.rson) == self.cledit.text():
            self.main_l = ClickUp()
            self.hide()
            self.main_l.show()
     


if __name__=="__main__":
    app = QApplication([])
    win = Login()
    win.show()
    app.exec_()
