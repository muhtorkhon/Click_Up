import random
import json
from PyQt5.QtWidgets import *
from slide_test import SlideWidget
from color_back import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 700)
        with open("balans.txt", "r") as file:
            data = json.load(file)
            for key, value in data.items():
                for inner_key, inner_value in value.items():
                    if inner_key=="MABLAG'":
                        self.wallet=float(inner_value)
                    if inner_key=="CASHBACK":
                        self.cashback=float(inner_value)                        
        self.stacked_widget = QStackedWidget()
        self.main_page_widget = QWidget()
        self.xayriya_page = QWidget()
        self.ticket_page=QWidget()
        self.car_page=QWidget()
        self.xarajatlar_page=QWidget()
        self.utkazma_page=QWidget()

        self.main_page()  
        self.xayriya_setup()
        self.ticket()
        self.car()
        self.xarajatlar()
        self.transactions_menu()  

        self.stacked_widget.addWidget(self.main_page_widget)
        self.stacked_widget.addWidget(self.xayriya_page)
        self.stacked_widget.addWidget(self.ticket_page)
        self.stacked_widget.addWidget(self.car_page)
        self.stacked_widget.addWidget(self.xarajatlar_page)
        self.stacked_widget.addWidget(self.utkazma_page)

        
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.stacked_widget)
        
        self.setLayout(main_layout)
        self.slide = SlideWidget(self)
    
    def main_page(self):
        self.push_count=0
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

        self.hide_balans=QPushButton(clicked=self.hide_balance)
        self.hide_balans.setIcon(QIcon('hide_balans.png'))
        self.hide_balans.setIconSize(QSize(30, 30))
        self.hide_balans.setFixedSize(30,30)
        self.hide_balans.setStyleSheet("background-color:transparent")
        

        self.click_pass = QPushButton()
        self.click_pass.setIcon(QIcon('shtrix.png'))
        self.click_pass.setIconSize(QSize(60, 60))
        self.click_boom = QPushButton()
        self.click_boom.setIcon(QIcon('boom.jpg'))
        self.click_boom.setIconSize(QSize(60, 60))
        self.click_qr = QPushButton()
        self.click_qr.setIcon(QIcon('qr_2.jpg'))
        self.click_qr.setIconSize(QSize(70, 70))

        self.button_font(self.click_boom)
        self.button_font(self.click_pass)
        self.button_font(self.click_qr)

        self.adver_lbl = QLabel()
        self.service_lbl = QLabel("Xizmatlar")
        self.service_lbl.setStyleSheet("""font-size:22px;
                                          font:Arial""")
        self.adver_lbl.setStyleSheet("border-radius: 20px")
        image_adver = QPixmap("adver.jpg")
        image = image_adver.scaled(QSize(380, 170))
        self.cashback_btn = QPushButton(f"CASHBACK           {self.cashback} so'm")
        self.adver_cashback_font(self.cashback_btn)
        self.cashback_btn.setIcon(QIcon('wallet.jpg'))
        self.cashback_btn.setIconSize(QSize(60, 60))
        self.adver_lbl.setPixmap(image)

        self.home_ser_btn = QPushButton()
        self.home_ser_btn.setIcon(QIcon('home3.jpg'))
        self.home_ser_btn.setIconSize(QSize(90, 80))
        self.home_ser_btn.setStyleSheet("background-color:transparent;")
        
        self.car_ser_btn = QPushButton(clicked=self.car_next)
        self.car_ser_btn.setIcon(QIcon('car.jpg'))
        self.car_ser_btn.setIconSize(QSize(80, 80))
        self.xayriya_btn = QPushButton()
        self.xayriya_btn.setIcon(QIcon('charity.jpg'))
        self.xayriya_btn.setIconSize(QSize(80, 80))
        self.xayriya_btn.clicked.connect(self.xayriya_next)
        self.kinoteatr_serv = QPushButton(clicked=self.ticket_next)
        self.kinoteatr_serv.setIcon(QIcon('cinema5.png'))
        self.kinoteatr_serv.setIconSize(QSize(70, 70))

        self.services_btn_font(self.home_ser_btn)
        self.services_btn_font(self.car_ser_btn)
        self.services_btn_font(self.xayriya_btn)
        self.services_btn_font(self.kinoteatr_serv)

        self.h_services.addWidget(self.home_ser_btn)
        self.h_services.addWidget(self.car_ser_btn)
        self.h_services.addWidget(self.xayriya_btn)
        self.h_services.addWidget(self.kinoteatr_serv)

        self.home = QPushButton()
        self.home.setIcon(QIcon("click_logo.jpg"))
        self.home.setIconSize(QSize(60, 60))
        self.pay = QPushButton()
        self.pay.setIcon(QIcon("transactions.jpg"))
        self.pay.setIconSize(QSize(40, 40))
        self.transactions = QPushButton(clicked=self.transactions_next)
        self.transactions.setIcon(QIcon("transactions.jpg"))
        self.transactions.setIconSize(QSize(50, 50))

        self.monitoring = QPushButton(clicked=self.xarajatlar_next)
        self.monitoring.setIcon(QIcon("hisobot.png"))
        self.monitoring.setIconSize(QSize(80, 80))
        self.more = QPushButton(clicked=self.more_slide)
        self.more.setIcon(QIcon("more.png"))
        self.more.setIconSize(QSize(35, 35))

        self.h_status_bar.addWidget(self.search)
        self.bottom_button_font(self.home)
        self.bottom_button_font(self.pay)
        self.bottom_button_font(self.transactions)
        self.bottom_button_font(self.monitoring)
        self.bottom_button_font(self.more)

        self.h_balans_card.addWidget(self.balan_lbl)
        self.h_balans_card.addWidget(self.hide_balans)
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
        self.xayriya_lbl.setStyleSheet("font-size:20px")
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

    def hide_balance(self):
        if self.push_count%2==0:
                balance_text = self.balan_lbl.text().replace(" ", "")[:-3]  
                masked_balance = ''.join(['*' for _ in balance_text]) + " so'm" 
                self.balan_lbl.setText(masked_balance)
                self.push_count+=1
        else:
            self.balan_lbl.setText(f"{str(self.wallet)} so'm")
            self.push_count+=1
    def xayriya_next(self):
        self.stacked_widget.setCurrentIndex(1)

    def ok_charity(self):
        with open("balans.txt", "r") as file:
            data = json.load(file)
            for key, value in data.items():
                for inner_key, inner_value in value.items():
                    if inner_key == "MABLAG'":
                        self.wallet = float(inner_value)
                    if inner_key == "CASHBACK":
                        self.cashback = float(inner_value)
            self.wallet -= self.summ_ticket
            self.balan_lbl.setText(f"{self.wallet} so'm")
            if self.summ.text().isdigit() and int(self.summ.text()) > 0 and int(self.summ.text())<=self.wallet:
                amount = int(self.summ.text())
                self.xayriya_lbl.setText(f"Siz {amount} miqdorida xayriya qildingiz")
                self.xayriya_lbl.show()
                self.wallet -= amount
                self.balan_lbl.setText(f"{self.wallet} so'm")
            else:
                self.xayriya_lbl.setText("""Summa noto'g'ri kiritildi""")
                self.xayriya_lbl.show()
            data[key]["MABLAG'"] = self.wallet
            data[key]['XAYRIYA'] = data[key]['XAYRIYA'] +amount
        with open("balans.txt", "w") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    
    def ticket(self):
        self.lst_checkboxes = []
        self.checked_count_label=QLabel("0")
        self.checked_count_label.setStyleSheet("font-size:20px;color:grey")
        self.count = 1
        layout = QVBoxLayout()
        h_buttn=QHBoxLayout()
        self.combo_ticket = QComboBox()
        lst_movies = ["Forsaj", "Baron", "Avatar", "Kalmar o'yini", "Cho'qintirgan ota"]
        self.combo_ticket.addItems(lst_movies)
        self.combo_ticket.currentIndexChanged.connect(self.shuffle_and_update)
        layout.addWidget(self.combo_ticket)
        layout.addWidget(self.checked_count_label)
        self.place = QGridLayout()
        for i in range(1,11):
            for j in range(1,11):
                check_box = QCheckBox(f"{self.count}")
                check_box.stateChanged.connect(self.update_checked_count)
                self.lst_checkboxes.append(check_box)
                self.count += 1
        layout.addLayout(self.place)
        self.ok_tck=QPushButton("Xarid qilish", clicked=self.ticket_xarid)
        self.exit_tck=QPushButton("Orqaga",clicked=self.back)
        h_buttn.addWidget(self.ok_tck)
        h_buttn.addWidget(self.exit_tck)
        layout.addLayout(h_buttn)
        self.ticket_page.setLayout(layout)


        self.shuffle_and_update()

    def shuffle_and_update(self):
        for checkbox in self.lst_checkboxes:
            checkbox.setChecked(False)
        random.shuffle(self.lst_checkboxes)
        disabled_count = int(len(self.lst_checkboxes) * 0.4)
        for check_box in self.lst_checkboxes:
            check_box.setEnabled(True)  
        for check_box in self.lst_checkboxes[:disabled_count]:
            check_box.setEnabled(False) 

        for i in reversed(range(self.place.count())):
            self.place.itemAt(i).widget().setParent(None)
        self.lst_checkboxes.sort(key=lambda x: int(x.text()))
        count = 0
        for i in range(1,11):
            for j in range(1,11):
                self.place.addWidget(self.lst_checkboxes[count], i, j)
                count += 1
        self.update_checked_count()

    def update_checked_count(self):
        ticket_price=50000
        self.checked_count = sum(1 for checkbox in self.lst_checkboxes if checkbox.isChecked())
        self.summ_ticket=ticket_price*self.checked_count
        if self.summ_ticket<=self.wallet:
            self.checked_count_label.setText(f"{self.checked_count} dona bilet narxi:->  {self.summ_ticket} so'm")
        else:
            self.checked_count_label.setText(f"{self.summ_ticket} so'mga {self.wallet} so'm mablag' yetarli emas")
            for checkbox in self.lst_checkboxes:
                checkbox.setEnabled(False)
    def ticket_next(self):
        self.stacked_widget.setCurrentIndex(2)

    

    def ticket_xarid(self):
        with open("balans.txt", "r") as file:
            data = json.load(file)
            for key, value in data.items():
                for inner_key, inner_value in value.items():
                    if inner_key == "MABLAG'":
                        self.wallet = float(inner_value)
                    if inner_key == "CASHBACK":
                        self.cashback = float(inner_value)
            self.wallet -= self.summ_ticket
            cashback = self.summ_ticket // 100
            self.cashback += cashback
            self.balan_lbl.setText(f"{self.wallet} so'm")
            self.cashback_btn.setText(f"CASHBACK   {self.cashback} so'm")
            self.checked_count_label.setText(f"{self.summ_ticket} so'm || Cashback: {cashback}")

            data[key]["MABLAG'"] = self.wallet
            data[key]['CHIPTA XARIDI'] = data[key]['CHIPTA XARIDI']+self.summ_ticket
            data[key]['CASHBACK'] = self.cashback

        with open("balans.txt", "w") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def car(self):
        scroll_area = QScrollArea(self)
        scroll_area.setStyleSheet("background-color:transparent;border:none")
        scroll_area.setFixedHeight(400)
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        lst_car_widget = QListWidget()
        lst_car_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.exist_car = QLabel("Mavjud mashinalar")
        self.refresh_btn=QPushButton("REFRESH")
        self.exist_car.setStyleSheet("font-size:20px")
        scroll_layout.addWidget(self.exist_car)
        self.procces_lbl=QLabel()
        self.procces_lbl.hide()
        self.add_car_btn = QPushButton("Mashina qo'shish")
        self.add_car_btn.setFixedHeight(30)
        self.add_car_btn.clicked.connect(self.add_car)
        
        self.exit_car = QPushButton("EXIT",clicked=self.back)
        self.exit_car.setFixedHeight(30)
        self.who_car=QLineEdit()
        self.who_car.setPlaceholderText("Kimning mashinasi: ")
        self.who_car.setFixedHeight(30)
        self.new_car_model=QLineEdit()
        self.new_car_model.setPlaceholderText("Modeli: ")
        self.new_car_model.setFixedHeight(30)
        self.new_car_number=QLineEdit()
        self.new_car_number.setPlaceholderText("Avtomobil raqami: ")
        self.new_car_number.setFixedHeight(30)
        self.ok_add_car_btn=QPushButton("OK")
        self.new_car_number.hide()
        self.who_car.hide()
        self.new_car_model.hide()
        with open("avto.txt", "r") as file:
            data = json.load(file)
        for key, values in data.items():
            car_item = QListWidgetItem(f"{key}:")
            lst_car_widget.addItem(car_item) 
            for k, v in values.items():
                car_info_item = QListWidgetItem(f"{k}: {v}")
                lst_car_widget.addItem(car_info_item)
            spacer_widget = QWidget()
            spacer_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  
            lst_car_widget.addItem(QListWidgetItem()) 
        scroll_area.setWidget(scroll_content)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setWidgetResizable(True)
        scroll_layout.addWidget(lst_car_widget) 
        main_layout = QVBoxLayout(self)
        
        main_layout.addWidget(scroll_area)
        main_layout.addWidget(self.who_car)
        main_layout.addWidget(self.new_car_model)
        main_layout.addWidget(self.new_car_number)
        main_layout.addWidget(self.procces_lbl)
        main_layout.addWidget(self.add_car_btn)
        main_layout.addWidget(self.exit_car)
        self.car_page.setLayout(main_layout)
     
    def add_car(self):
        self.who_car.show()
        self.new_car_model.show()
        self.new_car_number.show()
        self.add_car_btn.clicked.connect(self.car_format)

    def car_format(self):
        who = self.who_car.text()
        model = self.new_car_model.text()
        number = self.new_car_number.text()
        new_data = {
            who: {  
                "MODEL": model,
                "AVTOMASHINA RAQAMI": number,
                "JARIMA": "JARIMA MAVJUD EMAS"
            }
        }    
        try:
            with open("avto.txt", "r") as file:
                try:
                    data = json.load(file)
                except (json.JSONDecodeError, ValueError):
                    data = {}  
        except FileNotFoundError:
            data = {} 
        data.update(new_data) 
        with open("avto.txt", "w") as file:
            json.dump(data, file, indent=4)
        self.procces_lbl.setText("Avtomobil muvaffaqiyatli qo'shildi")
        self.procces_lbl.show()
        self.who_car.clear()
        self.new_car_model.clear()
        self.new_car_number.clear()

    def refresh(self):
        self.car()

    def car_next(self):
        self.stacked_widget.setCurrentIndex(3)
    def xarajatlar(self):
        layout=QVBoxLayout()
        self.exit_xarajat=QPushButton("EXIT",clicked=self.back)
        self.xarajat_lbl=QLabel("XARAJATLAR")
        with open("balans.txt", "r") as file:
            data = json.load(file)
            for key, value in data.items():
                for inner_key, inner_value in value.items():
                    label = QLabel(f"{inner_key} : {inner_value}")
                    label.setStyleSheet("font-size:20px")
                    layout.addWidget(label)  
        layout.addWidget(self.exit_xarajat)
        self.xarajatlar_page.setLayout(layout)

    def xarajatlar_next(self):
        self.stacked_widget.setCurrentIndex(4)



    def transactions_menu(self):
        layout = QVBoxLayout()
        self.trn_lbl = QLabel("PUL O'TKAZISH")
        self.trn_space_lbl=QLabel("")
        self.succes_trn_lbl=QLabel()
        self.succes_trn_lbl.setStyleSheet("font-size:16px")
        self.trn_space_lbl.setFixedHeight(300)
        self.trn_lbl.setStyleSheet("font-size:20px")
        self.trn_edit = QLineEdit()
        self.trn_edit.setFixedHeight(80)
        self.trn_edit_whom = QLineEdit()
        self.trn_edit_whom.setFixedHeight(80)
        self.trn_edit_whom.setPlaceholderText("KARTA RAQAMINI KIRITING")
        self.trn_edit_whom.setStyleSheet("font-size:20px;background-color:transparent;border:none")
        self.trn_edit.setPlaceholderText("MABLAG'NI KIRITING")
        self.trn_edit.setStyleSheet("font-size:20px;background-color:transparent;border:none")
        self.h_trn_btn = QHBoxLayout()
        self.trn_ok_btn = QPushButton("TASDIQLASH",clicked=self.check_trn)
        self.trn_ok_btn.setFixedHeight(50)
        self.trn_exit_btn = QPushButton("EXIT",clicked=self.back)
        self.trn_exit_btn.setFixedHeight(50)
        self.h_trn_btn.addWidget(self.trn_ok_btn)
        self.h_trn_btn.addWidget(self.trn_exit_btn)
        layout.addWidget(self.trn_lbl)
        layout.addWidget(self.trn_edit_whom)
        layout.addWidget(self.trn_edit)
        layout.addWidget(self.succes_trn_lbl)
        layout.addWidget(self.trn_space_lbl)
        layout.addLayout(self.h_trn_btn)
        self.utkazma_page.setLayout(layout)

    def check_trn(self): 
        with open("balans.txt", "r") as file:
            cashback=0
            data = json.load(file)
            for key, value in data.items():
                for inner_key, inner_value in value.items():
                    if inner_key == "MABLAG'":
                        self.wallet = float(inner_value)
                    if inner_key == "CASHBACK":
                        self.cashback = float(inner_value)
            if len(self.trn_edit_whom.text())==16 and self.trn_edit_whom.text().startswith("8600") or self.trn_edit_whom.text().startswith("9860"):
                if self.trn_edit.text().isdigit() and int(self.trn_edit.text()) > 0 and int(self.trn_edit.text())<=self.wallet:
                    amount =float(self.trn_edit.text())
                    cashback=cashback+amount//200
                    self.wallet -= amount
                    self.cashback+=cashback
                    data[key]["MABLAG'"] = self.wallet
                    data[key]["KARTA O'TKAZMALARI"] = data[key]["KARTA O'TKAZMALARI"]+ amount
                    data[key]["CASHBACK"] = self.cashback
                    self.succes_trn_lbl.setText(f"PUL KO'CHIRILDI || {cashback} so'm CASHBACK")
                    self.balan_lbl.setText(f"{self.wallet} so'm")
                else:
                    self.succes_trn_lbl.setText("MABLAG' NOTOG'RI KIRITILDI")
            else:
                self.succes_trn_lbl.setText("KARTANI RAQAMI XATO")
        with open("balans.txt", "w") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


    def transactions_next(self):
        self.stacked_widget.setCurrentIndex(5)



    def back(self):
        self.succes_trn_lbl.clear()
        self.trn_edit_whom.clear()
        self.trn_edit.clear()
        self.procces_lbl.setText("")
        self.new_car_model.hide()
        self.new_car_number.hide()
        self.who_car.hide()
        self.xayriya_lbl.clear()
        self.stacked_widget.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
