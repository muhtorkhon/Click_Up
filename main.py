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
        
        self.v_main_lay = QVBoxLayout()
        self.v_left_btn_lay = QVBoxLayout()
        self.h_up_btn_lay = QHBoxLayout()
        self.h_down_btn_lay = QHBoxLayout()
        self.list = QListWidget()
        
        self.Upp_menu_btns() # Up btns
        self.Left_menu_btns() # Lest btns
              
    def Upp_menu_btns(self):
        
        self.up_menu_btn = QPushButton("Click", clicked = self.Menu_click)
        self.up_eye_btn = QPushButton("Eye" , clicked = self.Eye_btn)
        self.up_amout_lbl = QLabel("Amout")
        self.up_search_edit = QLineEdit()
        self.up_search_edit.setPlaceholderText("search...")
        self.up_contact_center_lbl = QLabel("+998712310880")
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
        
        self.left_menu_btn = QPushButton("Click" , clicked = self.Menu_click)
        self.left_payment_btn = QPushButton("Payment", clicked = self.Payment)
        self.left_transfers_btn = QPushButton("Transfers", clicked = self.Transfers)
        self.left_cards_btn = QPushButton("Cards", clicked = self.Cards)
        self.left_reports_btn = QPushButton("Reports", clicked = self.Reports)
        self.left_main_services_btn = QPushButton("Main.services", clicked = self.Main_services)
        self.left_auto_payments_btn = QPushButton("Auto payments", clicked = self.Auto_Payments)
        self.left_settings_btn = QPushButton("Settings", clicked = self.Settings)
        
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
        self.__init__()
        
    def Payment(self):
        self.payment = Payment_()
        self.payment.show()
    
    def Transfers(self):
        self.transfer = Transfers_()
        self.transfer.show()
    
    def Cards(self):
        self.card = Cards_()
        self.card.show()
    
    def Reports(self):
        self.report = Reports_()
        self.report.show()
    
    def Main_services(self):
        self.main_service = Main_services_()
        self.main_service.show()     
        
    def Auto_Payments(self):
        self.auto_payment = Auto_Payment_()
        self.auto_payment.show()
        
        
    def Settings(self):
        self.setting = Setting_()
        self.setting.show()      
    
 
 
        
    def Eye_btn(self):
        pass   
        
    def Notification(self):
        pass
    
 
        
        
        
        
       
app = QApplication([])
win = ClickUp()
win.show()
app.exec_()        
        
        
        
        
        
        