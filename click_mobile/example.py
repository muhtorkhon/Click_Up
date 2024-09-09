from PyQt5.QtWidgets import *
from slide_test import SlideWidget
from color_back import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 700)
        self.cashback = 0
        self.wallet = 1000000

        # Stack widgetni yaratish
        self.stacked_widget = QStackedWidget()
        self.main_page_widget = QWidget()
        self.xayriya_page = QWidget()

        self.main_page()  
        self.xayriya_setup()  

        # Sahifalarni stack widgetga qo'shish
        self.stacked_widget.addWidget(self.main_page_widget)
        self.stacked_widget.addWidget(self.xayriya_page)

        # Asosiy layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.stacked_widget)
        self.setLayout(main_layout)

    def main_page(self):
        self.gradient_widget = GradientWidget(self)
        self.gradient_widget.setGeometry(0, 0, 400, 700)
        self.gradient_widget.setStyleSheet("background: transparent;")

        self.main_lst_widget = QListWidget()
        self.main_lst_widget.setFixedHeight(90)
        self.main_lst_widget.setStyleSheet("background: transparent; border:none;")
        self.main_lst_widget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.v_widget = QVBoxLayout()
        self.h_status_bar = QHBoxLayout()
        self.h_balans_card = QHBoxLayout()
        self.h_pay_method = QHBoxLayout()
        self.h_services = QHBoxLayout()
        self.h_bottom_bar = QHBoxLayout()
        self.v_main = QVBoxLayout()

        self.search = QLineEdit()
        self.search.setFixedHeight(30)
        self.search.setFixedWidth(350)
        self.search.setPlaceholderText("Qidiruv")
        self.search.setStyleSheet("border-radius:10")
        self.balan_lbl = QLabel(f"{str(self.wallet)} so'm")
        self.balan_lbl.setStyleSheet("font-size:30px;")
        self.click_pass = QPushButton()
        self.click_pass.setIcon(QIcon('shtrix.png'))
        self.click_pass.setIconSize(QSize(60, 60))
        self.click_boom = QPushButton()
        self.click_boom.setIcon(QIcon('boom.jpg'))
        self.click_boom.setIconSize(QSize(60, 60))
        self.click_qr = QPushButton()
        self.click_qr.setIcon(QIcon('qr_2.jpg'))
        self.click_qr.setIconSize(QSize(90, 90))

        self.button_font(self.click_boom)
        self.button_font(self.click_pass)
        self.button_font(self.click_qr)

        self.adver_lbl = QLabel()
        self.service_lbl = QLabel("Xizmatlar")
        self.service_lbl.setStyleSheet("""font-size:15px;
                                       font:Arial""")
        self.adver_lbl.setStyleSheet("border-radius: 20px")
        image_adver = QPixmap("adver.jpg")
        image = image_adver.scaled(QSize(380, 170))
        self.cashback_btn = QPushButton("CASHBACK")
        self.adver_cashback_font(self.cashback_btn)
        self.cashback_btn.setIcon(QIcon('wallet.jpg'))
        self.cashback_btn.setIconSize(QSize(60, 60))
        self.adver_lbl.setPixmap(image)

        self.home_ser_btn = QPushButton()
        self.home_ser_btn.setIcon(QIcon('home.png'))
        self.home_ser_btn.setIconSize(QSize(60, 60))
        self.car_ser_btn = QPushButton()
        self.car_ser_btn.setIcon(QIcon('car.jpg'))
        self.car_ser_btn.setIconSize(QSize(80, 80))
        self.xayriya_btn = QPushButton()
        self.xayriya_btn.setIcon(QIcon('charity.jpg'))
        self.xayriya_btn.setIconSize(QSize(80, 80))
        self.xayriya_btn.clicked.connect(self.xayriya_next)
        self.kinoteatr_serv = QPushButton()
        self.kinoteatr_serv.setIcon(QIcon('cinema2.png'))
        self.kinoteatr_serv.setIconSize(QSize(90, 90))

        self.services_btn_font(self.home_ser_btn)
        self.services_btn_font(self.car_ser_btn)
        self.services_btn_font(self.xayriya_btn)
        self.services_btn_font(self.kinoteatr_serv)

        self.h_services.addWidget(self.home_ser_btn)
        self.h_services.addWidget(self.car_ser_btn)
        self.h_services.addWidget(self.xayriya_btn)
        self.h_services.addWidget(self.kinoteatr_serv)

        self.home = QPushButton("Asosiy")
        self.pay = QPushButton("To'lov")
        self.transactions = QPushButton("O'tkazma")
        self.monitoring = QPushButton("Hisobot")
        self.more = QPushButton("..", clicked=self.more_slide)

        self.h_status_bar.addWidget(self.search)
        self.bottom_button_font(self.home)
        self.bottom_button_font(self.pay)
        self.bottom_button_font(self.transactions)
        self.bottom_button_font(self.monitoring)
        self.bottom_button_font(self.more)

        self.h_balans_card.addWidget(self.balan_lbl)
        self.h_pay_method.addWidget(self.click_pass)
        self.h_pay_method.addWidget(self.click_boom)
        self.h_pay_method.addWidget(self.click_qr)

        self.h_bottom_bar.addWidget(self.home)
        self.h_bottom_bar.addWidget(self.transactions)
        self.h_bottom_bar.addWidget(self.monitoring)
        self.h_bottom_bar.addWidget(self.more)
        spacer = QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.v_main.addLayout(self.h_status_bar)
        self.v_main.addItem(spacer)
        self.v_main.addLayout(self.h_balans_card)
        self.v_main.addItem(spacer)
        self.h_balans_card.setAlignment(Qt.AlignCenter)
        self.v_main.addItem(spacer)
        self.v_main.addLayout(self.h_pay_method)
        self.v_widget.addWidget(self.main_lst_widget)
        self.v_main.addLayout(self.v_widget)
        scroll_area = QScrollArea(self)
        scroll_area.setStyleSheet("background-color:transparent;border:none")
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.addWidget(self.cashback_btn)
        scroll_layout.addItem(spacer)
        scroll_layout.addWidget(self.adver_lbl)
        scroll_layout.addWidget(self.service_lbl)
        scroll_layout.addLayout(self.h_services)
        scroll_area.setWidget(scroll_content)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setWidgetResizable(True)
        self.v_main.addWidget(scroll_area)
        self.v_main.setContentsMargins(0, 20, 0, 0)
        self.v_main.addLayout(self.h_bottom_bar)

        self.main_page_widget.setLayout(self.v_main)

        self.slide = SlideWidget(self)
        self.installEventFilter(self)

    def more_slide(self):
        self.slide.toggle()

    def button_font(self, btn):
        btn.setFixedSize(90, 90)
        btn.setStyleSheet("""
            border-radius: 20px;
            background-color: white;
        """)

    def bottom_button_font(self, btn):
        btn.setFixedSize(70, 70)
        btn.setStyleSheet("""
            border-radius: 20px;
            background-color: white;
        """)

    def adver_cashback_font(self, btn):
        btn.setFixedSize(380, 70)
        btn.setStyleSheet("""
            font:Arial;
            text-align:left;
            font-size:20px;
            border-radius: 20px;
            background-color: white;
        """)

    def services_btn_font(self, btn):
        btn.setFixedSize(80, 80)
        btn.setStyleSheet("""
            font:Arial;
            text-align:left;
            font-size:20px;
            border-radius: 20px;
            background-color: white;
        """)

    def xayriya_setup(self):
        layout = QVBoxLayout()
        self.h_btn = QHBoxLayout()
        self.summ = QLineEdit()
        self.combo = QComboBox()
        self.xayriya_lbl=QLabel()
        self.xayriya_lbl.hide()
        self.combo.setFixedHeight(50)
    
        lst_xayriya = ["Vaqf", "Ezgu maqsad", "Mehrli qo'llar"]
        self.combo.addItems(lst_xayriya)
    
        self.summ.setPlaceholderText("Qancha xayriya qilamiz")
        self.summ.setFixedHeight(50)
        layout.addWidget(self.combo)
        layout.addWidget(self.summ)
        layout.addWidget(self.xayriya_lbl)
        self.ok_btn = QPushButton("OK",clicked=self.ok_charity)
        self.exit_btn = QPushButton("EXIT",clicked=self.back)
    
        self.h_btn.addWidget(self.ok_btn)
        self.h_btn.addWidget(self.exit_btn)

        layout.addLayout(self.h_btn)
        
        self.xayriya_page.setLayout(layout)
    def xayriya_next(self):
        self.stacked_widget.setCurrentIndex(1)

    def ok_charity(self):
        if self.summ.text().isdigit() and int(self.summ.text()) > 0 and int(self.summ.text())<=self.wallet:
            amount = int(self.summ.text())
            self.xayriya_lbl.setText(f"Siz {amount} miqdorida xayriya qildingiz")
            self.xayriya_lbl.show()
            self.wallet -= amount
            self.balan_lbl.setText(f"{self.wallet} so'm")
        else:
            self.xayriya_lbl.setText("Summa noto'g'ri kiritildi yoki mablag' yetarli emas")
            self.xayriya_lbl.show()
    def back(self):
        self.stacked_widget.setCurrentIndex(0)


            


    

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
