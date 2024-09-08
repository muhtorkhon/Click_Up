from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Payment_(QWidget):
  def __init__(self) -> None:
    super().__init__()
    self.resize(1700,900)
    self.setStyleSheet("background:#aaa;font-size:20px")
    
    self.g_btn_lyt = QGridLayout()
    self.h_btn_lyt = QHBoxLayout()
    self.h_edit_lyt = QHBoxLayout()
    self.v_main_lyt = QVBoxLayout()

    self.btn_sara = QPushButton(" Saralangan",clicked=self.sara)
    self.btn_sara.setIcon(QIcon("images/star.png"))

    self.btn_mobil = QPushButton(" Mobil opertor",clicked=self.mobil)
    self.btn_mobil.setIcon(QIcon("images/tablet.png"))

    self.btn_d_xizmat = QPushButton(" Davlat xizmatlari",clicked=self.d_xizmat)
    self.btn_d_xizmat.setIcon(QIcon("images/bank.png"))

    self.btn_komunal = QPushButton(" Komunal tolovlar",clicked=self.komunal)
    self.btn_komunal.setIcon(QIcon("images/home-location-alt.png"))

    self.btn_krs = QPushButton(" Kredit so'ndirish",clicked=self.krs)
    self.btn_krs.setIcon(QIcon("images/percentage.png"))

    self.btn_internet = QPushButton(" Internet provayderlar",clicked=self.internet)
    self.btn_internet.setIcon(QIcon("images/wifi.png"))

    self.btn_soliq = QPushButton(" Soliqlar",clicked=self.soliq)
    self.btn_soliq.setIcon(QIcon("images/summary-check.png"))

    self.btn_inter_xizmat = QPushButton(" Internet xizmatlari",clicked=self.inter_xizmat)
    self.btn_inter_xizmat.setIcon(QIcon("images/site.png"))

    self.btn_tv = QPushButton(" Telvidenie",clicked=self.tv)
    self.btn_tv.setIcon(QIcon("images/tv-retro.png"))

    self.btn_xosting = QPushButton(" Xosting va domenlar",clicked=self.xosting)
    self.btn_xosting.setIcon(QIcon("images/cloud.png"))

    self.btn_telefon = QPushButton(" Telefoniya",clicked=self.telefon)
    self.btn_telefon.setIcon(QIcon("images/phone-flip.png"))

    self.btn_dam = QPushButton(" Ko'ngilochar va dam olish",clicked=self.dam_olish)
    self.btn_dam.setIcon(QIcon("images/ferris-wheel.png"))

    self.btn_sugurta = QPushButton(" Sug'urta",clicked=self.sugurta)
    self.btn_sugurta.setIcon(QIcon("images/octagon-check.png"))

    self.btn_xayriya = QPushButton(" Xayriya",clicked=self.xayriya)
    self.btn_xayriya.setIcon(QIcon("images/heart.png"))

    self.btn_talim = QPushButton(" Ta'lim",clicked=self.talim)
    self.btn_talim.setIcon(QIcon("images/book-bookmark.png"))

    self.btn_sogliq = QPushButton(" Sog'liq",clicked=self.sogliq)
    self.btn_sogliq.setIcon(QIcon("images/medicine.png"))

    self.btn_trasport_a = QPushButton(" Transport va avtoturargoh",clicked=self.transport_t)
    self.btn_trasport_a.setIcon(QIcon("images/subway.png"))

    self.btn_taxi = QPushButton(" Taksi",clicked=self.taxi)
    self.btn_taxi.setIcon(QIcon("images/taxi.png"))

    self.btn_hisob_r = QPushButton(" Hisob raqamiga to'lov",clicked=self.hisob_r)
    self.btn_hisob_r.setIcon(QIcon("images/digital-payment.png"))

    self.btn_inter_top = QPushButton(" Internet-to'plamlar",clicked=self.inter_top)
    self.btn_inter_top.setIcon(QIcon("images/mobile-4g.png"))

    self.lts = [self.btn_sara, self.btn_mobil, self.btn_d_xizmat, self.btn_komunal, self.btn_krs, self.btn_internet, self.btn_soliq, self.btn_inter_xizmat, self.btn_tv, self.btn_xosting, self.btn_telefon, self.btn_dam, self.btn_sugurta, self.btn_xayriya, self.btn_talim, self.btn_sogliq, self.btn_trasport_a, self.btn_taxi, self.btn_hisob_r, self.btn_inter_top]

    index = 0
    for i in range(5):
      for j in range(4):
        self.g_btn_lyt.addWidget(self.lts[index],i,j)
        self.lts[index].setStyleSheet("background:lightgray;color:blue")
        self.lts[index].setFixedSize(300,100)
        index += 1

    self.btn_x_tolov = QPushButton("Xizmatlarga to'lov",clicked=self.x_tolov)
    self.btn_x_tolov.setFixedSize(280,60)

    self.btn_j_tolov = QPushButton("Joylarda to'lov",clicked=self.j_tolov)
    self.btn_j_tolov.setFixedSize(280,60)

    self.btn_katta_c = QPushButton("Katta cashback",clicked=self.katta_c)
    self.btn_katta_c.setFixedSize(280,60)

    self.btn_search = QPushButton()
    self.btn_search.setStyleSheet("background:lightgray")
    self.btn_search.setFixedSize(50,50)
    self.btn_search.setIcon(QIcon("images/search.png"))

    self.edit = QLineEdit()
    self.edit.setStyleSheet("background:lightgray")
    self.edit.setPlaceholderText("Qidiruv")
    self.edit.setFixedSize(220,50)

    self.lbl = QLabel("Kontakt markaz\n+99871 231 08 80 ")
    self.lbl.setFixedSize(220,50)
    self.lbl.setStyleSheet("color:blue")

    self.btn_bell = QPushButton()
    self.btn_bell.setIcon(QIcon("images/bell.png"))
    self.btn_bell.setFixedSize(50,50)

    self.h_edit_lyt.addStretch()
    self.h_edit_lyt.addWidget(self.btn_search)
    self.h_edit_lyt.addWidget(self.edit)
    self.h_edit_lyt.addWidget(self.lbl)
    self.h_edit_lyt.addWidget(self.btn_bell)

    self.h_btn_lyt.addStretch()
    self.h_btn_lyt.addWidget(self.btn_x_tolov)
    self.h_btn_lyt.addWidget(self.btn_j_tolov)
    self.h_btn_lyt.addWidget(self.btn_katta_c)

    self.v_main_lyt.addLayout(self.h_edit_lyt)
    self.v_main_lyt.addLayout(self.h_btn_lyt)
    self.v_main_lyt.addLayout(self.g_btn_lyt)
    self.setLayout(self.v_main_lyt)
  

  def sara(self):
    pass

  def mobil(self):
    pass

  def d_xizmat(self):
    pass

  def komunal(self):
    pass

  def krs(self):
    pass

  def internet(self):
    pass

  def sara(self):
    pass

  def soliq(self):
    pass

  def inter_xizmat(self):
    pass

  def tv(self):
    pass

  def xosting(self):
    pass

  def telefon(self):
    pass

  def dam_olish(self):
    pass

  def sugurta(self):
    pass

  def xayriya(self):
    pass

  def talim(self):
    pass

  def sogliq(self):
    pass

  def transport_t(self):
    pass

  def taxi(self):
    pass

  def hisob_r(self):
    pass

  def inter_top(self):
    pass




  def x_tolov(self):
    self.btn_x_tolov.setStyleSheet("background:skyblue")
    self.btn_j_tolov.setStyleSheet("background:white")
    self.btn_katta_c.setStyleSheet("background:white")
  def j_tolov(self):
    self.btn_j_tolov.setStyleSheet("background:skyblue")
    self.btn_x_tolov.setStyleSheet("background:white")
    self.btn_katta_c.setStyleSheet("background:white")

  def katta_c(self):
    self.btn_katta_c.setStyleSheet("background:skyblue")
    self.btn_j_tolov.setStyleSheet("background:white")
    self.btn_x_tolov.setStyleSheet("background:white")


if __name__ == "__main__":
  app = QApplication([])
  win = Payment_()
  win.show()
  app.exec_()