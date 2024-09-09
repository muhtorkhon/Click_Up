from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Mobil(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(1700,900)
        self.setStyleSheet("background:#fff;font-size:20px")

        self.h_btn_lyt = QHBoxLayout()
        self.v_btn_lyt = QVBoxLayout()
        self.g_btn_lyt = QGridLayout()

        self.btn_beline = QPushButton("",clicked=self.beline)
        self.btn_beline.setIcon(QIcon("images/beline.png"))
        self.btn_beline.setIconSize(self.btn_beline.size())

        self.btn_usell = QPushButton("",clicked=self.usell)
        self.btn_usell.setIcon(QIcon("images/usell.png"))
        self.btn_usell.setIconSize(self.btn_usell.size())

        self.btn_humans = QPushButton("",clicked=self.humans)
        self.btn_humans.setIcon(QIcon("images/humans.png"))
        self.btn_humans.setIconSize(self.btn_humans.size())

        self.btn_mobiluz = QPushButton("",clicked=self.mobiluz)
        self.btn_mobiluz.setIcon(QIcon("images/mobiluz.png"))
        self.btn_mobiluz.setIconSize(self.btn_mobiluz.size())

        self.btn_perfectum = QPushButton("",clicked=self.perfectum)
        self.btn_perfectum.setIcon(QIcon("images/perfectum.png"))
        self.btn_perfectum.setIconSize(self.btn_perfectum.size())

        self.btn_oq = QPushButton("",clicked=self.oq)
        self.btn_oq.setIcon(QIcon("images/oq.png"))
        self.btn_oq.setIconSize(self.btn_oq.size())

        self.btn_uzmobile_c = QPushButton("",clicked=self.uzmobile_c)
        self.btn_uzmobile_c.setIcon(QIcon("images/uzmobilecdma.png"))
        self.btn_uzmobile_c.setIconSize(self.btn_uzmobile_c.size())

        self.btn_uzmobile_g = QPushButton("",clicked=self.uzmobile_g)
        self.btn_uzmobile_g.setIcon(QIcon("images/uzmobilegsm.png"))
        self.btn_uzmobile_g.setIconSize(self.btn_uzmobile_g.size())

        self.lts = [self.btn_beline, self.btn_humans, self.btn_mobiluz, self.btn_usell, self.btn_perfectum, self.btn_oq, self.btn_uzmobile_c, self.btn_uzmobile_g]

        index = 0
        for i in range(2):
            for j in range(4):
                self.g_btn_lyt.addWidget(self.lts[index],i,j)
                self.lts[index].setFixedSize(220,180)
                index += 1


        self.h_exit_btn = QHBoxLayout()

        self.exit_btn = QPushButton("",clicked=self.hide)
        self.exit_btn.setIcon(QIcon("images/sign-out-alt"))
        self.exit_btn.setFixedSize(50,50)

        self.h_exit_btn.addStretch()
        self.h_exit_btn.addWidget(self.exit_btn)

        self.v_btn_lyt.addLayout(self.h_exit_btn)
        self.v_btn_lyt.addLayout(self.g_btn_lyt)
        self.setLayout(self.v_btn_lyt)



    def beline(self):
        pass

    def usell(self):
        pass

    def mobiluz(self):
        pass

    def humans(self):
        pass

    def perfectum(self):
        pass

    def uzmobile_c(self):
        pass

    def uzmobile_g(self):
        pass

    def oq(self):
        pass




if __name__=="__main__":
    app = QApplication([])
    win = Mobil()
    win.show()
    app.exec_()


