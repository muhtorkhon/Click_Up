from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from payme_mobil import *

class Payment_(QWidget):
  def __init__(self):
    super().__init__()
    self.resize(1700,900)
    self.setStyleSheet("background:#fff;font-size:20px")
    
    self.g_btn_lyt = QGridLayout()
    self.h_btn_lyt = QHBoxLayout()
    self.h_edit_lyt = QHBoxLayout()
    self.v_main_lyt = QVBoxLayout()

    self.btn_sara = QPushButton(" Saralangan", clicked=self.sara)
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
    self.btn_x_tolov.setStyleSheet("background:skyblue")
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

    self.btn_bell = QPushButton("",clicked=self.newx)
    self.btn_bell.setIcon(QIcon("images/bell.png"))
    self.btn_bell.setFixedSize(50,50)
  
    self.main_exit_btn = QPushButton("",clicked=self.hide)
    self.main_exit_btn.setIcon(QIcon("images/sign-out-alt.png"))
    self.main_exit_btn.setFixedSize(50,50)


    self.h_edit_lyt.addStretch()
    self.h_edit_lyt.addWidget(self.btn_search)
    self.h_edit_lyt.addWidget(self.edit)
    self.h_edit_lyt.addWidget(self.lbl)
    self.h_edit_lyt.addWidget(self.btn_bell)
    self.h_edit_lyt.addWidget(self.main_exit_btn)

    self.h_btn_lyt.addStretch()
    self.h_btn_lyt.addWidget(self.btn_x_tolov)
    self.h_btn_lyt.addWidget(self.btn_j_tolov)
    self.h_btn_lyt.addWidget(self.btn_katta_c)

    self.v_main_lyt.addLayout(self.h_edit_lyt)
    self.v_main_lyt.addLayout(self.h_btn_lyt)
    self.v_main_lyt.addLayout(self.g_btn_lyt)
    self.setLayout(self.v_main_lyt)
  

  def sara(self):
    QMessageBox.information(self, "Saralangan","Sizda hali tanlangan to'lovlar yo'q")
 

  def mobil(self):
    self.mob = Mobil()
    self.mob.show()

  def d_xizmat(self):
    self.scrol = QScrollArea()
    self.scrol.resize(1700,900)

    self.exti_btn = QPushButton("",clicked=self.scrol.hide)
    self.exti_btn.setFixedSize(50,50)
    self.exti_btn.setIcon(QIcon("images/sign-out-alt.png"))

    self.dra = QLabel("        ")

    self.h_btn_exit_lbl = QHBoxLayout()
    self.v_rasm_lyt = QVBoxLayout()
    asr = QWidget()

    self.h_btn_exit_lbl.addStretch()
    self.h_btn_exit_lbl.addWidget(self.exti_btn)
    self.h_btn_exit_lbl.addWidget(self.dra)
    self.v_rasm_lyt.addLayout(self.h_btn_exit_lbl)

    self.rasm_lts = ["images/davlat1.png","images/davlat2.png"]
    
    for i in self.rasm_lts:
      self.lbl_rasm = QLabel()
      pxmap = QPixmap(i)
      self.lbl_rasm.setPixmap(pxmap)
      self.lbl_rasm.setFixedSize(1700,900)
      self.v_rasm_lyt.addWidget(self.lbl_rasm)

    asr.setLayout(self.v_rasm_lyt)
    self.scrol.setWidget(asr)
    self.scrol.show()

  def komunal(self):
    self.k_scrol = QScrollArea()
    self.k_scrol.resize(1700,900)
    k_win = QWidget()

    self.k_exit_btn = QPushButton("",clicked=self.k_scrol.hide)
    self.k_exit_btn.setIcon(QIcon("images/sign-out-alt.png"))
    self.k_exit_btn.setFixedSize(50,50)

    self.pra = QLabel("        ")

    self.v_komunal_lyt = QVBoxLayout()
    self.h_k_exit_lyt = QHBoxLayout()

    self.h_k_exit_lyt.addStretch()
    self.h_k_exit_lyt.addWidget(self.k_exit_btn)
    self.h_k_exit_lyt.addWidget(self.pra)
  
    self.v_komunal_lyt.addLayout(self.h_k_exit_lyt)

    self.komunal_lts = ["images/komunal1.png","images/komunal2.png","images/komunal3.png"]

    for i in self.komunal_lts:
      self.kml = QLabel()
      px = QPixmap(i)
      self.kml.setPixmap(px)
      self.kml.setFixedSize(1700,900)
      self.v_komunal_lyt.addWidget(self.kml)

    k_win.setLayout(self.v_komunal_lyt)
    self.k_scrol.setWidget(k_win)
    self.k_scrol.show()

  def krs(self):
    pass

  def internet(self):
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
    QMessageBox.information(self,"Joylarda to'lov","Joylarda to'lov bo'limi yaratilmagan")

  def katta_c(self):
    self.btn_katta_c.setStyleSheet("background:skyblue")
    self.btn_j_tolov.setStyleSheet("background:white")
    self.btn_x_tolov.setStyleSheet("background:white")
    QMessageBox.information(self,"Katta cashbek","Katta Cashbek bo'limi yaratilmagan")

  def newx(self):
    QMessageBox.information(self,"Xabar","Yangi Xabar yo'q")

if __name__ == "__main__":
  app = QApplication([])
  win = Payment_()
  win.show()
  app.exec_()