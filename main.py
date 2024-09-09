from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from Payment_Click import Payment_
from Transfers_Click import Transfers_
from Cards_Click import Cards_
from Reports_Click import Reports_
from Main_services_Click import Main_services_
from Auto_Paymnet_Click import Auto_Payment_
from Settings_Click import Setting_

class ClickUp(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(1930,1000)
        self.setStyleSheet("background:#fff;font-size:20px")
        
        self.v_main_lay = QVBoxLayout()
        self.v_left_btn_lay = QVBoxLayout()
        self.h_up_btn_lay = QHBoxLayout()
        self.h_down_btn_lay = QHBoxLayout()
        self.list = QScrollArea()
        
        self.Upp_menu_btns()
        self.Left_menu_btns()
        self.Menu_click()     
    def Upp_menu_btns(self):
        
        self.up_menu_btn = QPushButton("Click", clicked = self.Menu_click)
        self.up_eye_btn = QPushButton("" , clicked = self.Eye_btn)
        self.up_eye_btn.setIcon(QIcon("images/eye.png"))
        self.up_amout_lbl = QLabel("   Umumiy balans\n   500000")
        self.up_amout_lbl.setStyleSheet("color:blue")
        self.up_search_edit = QLineEdit()
        self.up_search_edit.setPlaceholderText("search...")
        self.up_contact_center_lbl = QLabel("Kontakt markaz\n+998912310880")
        self.up_contact_center_lbl.setStyleSheet("color:blue")
        self.up_notification_btn = QPushButton("Notification",clicked = self.Notification)
        self.up_setting_btn = QPushButton("Settings",clicked = self.Settings)
                
        self.h_up_btn_lay.addWidget(self.up_menu_btn)
        self.h_up_btn_lay.addWidget(self.up_eye_btn)
        self.h_up_btn_lay.addWidget(self.up_amout_lbl)
        self.h_up_btn_lay.addStretch()
        self.h_up_btn_lay.addWidget(self.up_search_edit)
        self.h_up_btn_lay.addWidget(self.up_contact_center_lbl)
        self.h_up_btn_lay.addWidget(self.up_notification_btn)
        self.h_up_btn_lay.addWidget(self.up_setting_btn)
        
        self.v_main_lay.addLayout(self.h_up_btn_lay)
        self.setLayout(self.v_main_lay)    
        
    def Left_menu_btns(self):
        
        self.left_menu_btn = QPushButton("", clicked = self.Menu_click)
        self.left_menu_btn.setFixedSize(90,90)
        self.left_menu_btn.setIcon(QIcon("images/bosh.png"))
        self.left_menu_btn.setIconSize(self.left_menu_btn.size())

        self.left_payment_btn = QPushButton("", clicked = self.Payment)
        self.left_payment_btn.setFixedSize(90,90)
        self.left_payment_btn.setIcon(QIcon("images/tolov.png"))
        self.left_payment_btn.setIconSize(self.left_payment_btn.size())

        self.left_transfers_btn = QPushButton("", clicked = self.Transfers)
        self.left_transfers_btn.setFixedSize(90,90)
        self.left_transfers_btn.setIcon(QIcon("images/otkaz.png"))
        self.left_transfers_btn.setIconSize(self.left_transfers_btn.size())

        self.left_cards_btn = QPushButton("", clicked = self.Cards)
        self.left_cards_btn.setFixedSize(90,90)
        self.left_cards_btn.setIcon(QIcon("images/karta.png"))
        self.left_cards_btn.setIconSize(self.left_cards_btn.size())
        
        self.left_reports_btn = QPushButton("", clicked = self.Reports)
        self.left_reports_btn.setFixedSize(90,90)
        self.left_reports_btn.setIcon(QIcon("images/hisob.png"))
        self.left_reports_btn.setIconSize(self.left_reports_btn.size())

        self.left_main_services_btn = QPushButton("", clicked = self.Main_services)
        self.left_main_services_btn.setFixedSize(90,90)
        self.left_main_services_btn.setIcon(QIcon("images/servis"))
        self.left_main_services_btn.setIconSize(self.left_main_services_btn.size())


        self.left_auto_payments_btn = QPushButton("", clicked = self.Auto_Payments)
        self.left_auto_payments_btn.setFixedSize(90,90)
        self.left_auto_payments_btn.setIcon(QIcon("images/avtolov.png"))
        self.left_auto_payments_btn.setIconSize(self.left_auto_payments_btn.size())

        self.left_settings_btn = QPushButton("", clicked = self.Settings)
        self.left_settings_btn.setFixedSize(90,90)
        self.left_settings_btn.setIcon(QIcon("images/sozla.png"))
        self.left_settings_btn.setIconSize(self.left_settings_btn.size())
        
        self.v_left_btn_lay.addWidget(self.left_menu_btn)
        self.v_left_btn_lay.addWidget(self.left_payment_btn)
        self.v_left_btn_lay.addWidget(self.left_transfers_btn)
        self.v_left_btn_lay.addWidget(self.left_cards_btn)
        self.v_left_btn_lay.addWidget(self.left_reports_btn)
        self.v_left_btn_lay.addWidget(self.left_main_services_btn)
        self.v_left_btn_lay.addWidget(self.left_auto_payments_btn)
        self.v_left_btn_lay.addWidget(self.left_settings_btn)
        
        self.h_down_btn_lay.addLayout(self.v_left_btn_lay)
        self.h_down_btn_lay.addWidget(self.list)
          
        self.v_main_lay.addLayout(self.v_left_btn_lay)
        self.v_main_lay.addLayout(self.h_down_btn_lay)
        self.setLayout(self.v_main_lay)
        
    def Menu_click(self):
        self.v_mn_lyt = QVBoxLayout()

        minyus = QWidget()

        self.m_lts = ["images/menyu1.png","images/menyu2.png","images/menyu3.png"]

        for i in self.m_lts:
            self.m_lbl = QLabel()
            rsmm = QPixmap(i)
            self.m_lbl.setPixmap(rsmm)
            self.v_mn_lyt.addWidget(self.m_lbl)

        minyus.setLayout(self.v_mn_lyt)
        self.list.setWidget(minyus)
        
    def Payment(self):
        self.payment = Payment_()
        self.list.setWidget(self.payment)
    
    def Transfers(self):
        self.transfer = Transfers_()
        self.list.setWidget(self.transfer)
    
    def Cards(self):
        self.card = Cards_()
        self.list.setWidget(self.card)
    
    def Reports(self):
        self.report = Reports_()
        self.list.setWidget(self.report)
    
    def Main_services(self):
        self.main_service = Main_services_()
        self.list.setWidget(self.main_service)     
        
    def Auto_Payments(self):
        self.auto_payment = Auto_Payment_()
        self.list.setWidget(self.auto_payment)
        
        
    def Settings(self):
        self.setting = Setting_()
        self.list.setWidget(self.setting)     
    
 
 
        
    def Eye_btn(self):
        pass
        # if self.c % 2:
        #     self.up_eye_btn = QPushButton("" , clicked = self.Eye_btn)
        #     self.up_eye_btn.setIcon(QIcon("images/eye-crossed.png"))
        #     self.up_amout_lbl = QLabel("**************") 
        # else:
        #     self.up_eye_btn = QPushButton("" , clicked = self.Eye_btn)
        #     self.up_eye_btn.setIcon(QIcon("images/eye.png"))
        #     self.up_amout_lbl = QLabel("   Umumiy balans\n   500000") 
        # self.c += 1
    def Notification(self):
        pass
    
 
        
        
        
        
if __name__=="__main__":       
    app = QApplication([])
    win = ClickUp()
    win.show()
    app.exec_()        
        
        
        
        
        
        