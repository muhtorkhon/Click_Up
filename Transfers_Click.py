import json
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class Transfers_(QWidget):
    def __init__(self) -> None:
        super().__init__()
        # while True:
        #     if self.check():
        #         break
        self.setFixedSize(500,400)
        self.setStyleSheet("font-size:20px")
        self.setWindowTitle("Transfers")
        self.setWindowIcon(QIcon("Click_Up/images/exchange-alt (1).png"))
        self.main_ver = QVBoxLayout()
        self.lay = QHBoxLayout()
        # line edit
        self.card_number = QLineEdit()
        self.card_number.setPlaceholderText("Card number....")
        self.card_number.setClearButtonEnabled(True)
        regex = QRegExp("^\\d{0,16}$")
        validator = QRegExpValidator(regex, self.card_number)
        self.card_number.setValidator(validator)
        # search btn
        self.search_btn = QPushButton(clicked=self.search)
        self.search_btn.setIcon(QIcon("Click_Up/images/search.png"))
        # self.search_btn.setText("\n\nSearch")
        # info btn
        self.info_lbl = QLabel("Enter the full card / wallet / phone number of the \nrecipient")
        self.info_lbl.setAlignment(Qt.AlignCenter)
        self.info_btn = QPushButton(clicked=self.transfer)
        self.info_btn.setIcon(QIcon("click_up.png"))
        self.info_btn.setStyleSheet("color: blue;")
        self.info_btn.hide()
        self.lay.addWidget(self.card_number)
        self.lay.addWidget(self.search_btn)
        self.main_ver.addLayout(self.lay)
        self.main_ver.addWidget(self.info_lbl)
        self.main_ver.addWidget(self.info_btn)
        # self.main_ver.addStretch(2)
        self.setLayout(self.main_ver)
        self.my_card = QLabel("0000000000000000")
    
    def search(self):
        try:
            with open("data.json") as f:
                self.data = json.load(f)
            if len(self.card_number.text()) == 16:
                if self.card_number.text() in self.data:
                    self.info_lbl.hide()
                    self.info_btn.show()
                    text_value = ' '.join(str(j) for i, j in list(self.data[self.card_number.text()].items())[:3])
                    
                    self.info_btn.setText(text_value)
                    self.info_btn.setStyleSheet("background-color:lightblack;color:blue")
            elif len(self.card_number.text()) == 12:
                for i in self.data:
                    # print(True)
                    # print(type(self.data[i]))
                    if int(self.card_number.text()) == self.data[i]["number"]:
                        print("12")
                        self.info_lbl.hide()
                        self.info_btn.show()
                        count = 0
                        text_value = "  "
                        print(list(self.data[i].items())[1])
                        for j in list(self.data[i].items()):
                            text_value += str(j[1])
                            text_value += " "
                            count += 1
                            if count == 3:
                                break
                        
                        # print(text_value)
                        self.info_btn.setText(text_value)
                        self.info_btn.setStyleSheet("background-color:lightblack;color:blue")
                        break
            else:
                self.info_lbl.show()
                self.info_btn.hide()
        
        except:
            pass
    def transfer(self):
        self.hide()
        self.h_tr1_lay = QHBoxLayout()
        self.h_tr2_lay = QHBoxLayout()
        self.input_sum = QLineEdit()
        self.info = QLabel()
        self.info.setText(self.info_btn.text())
        self.input_sum.setValidator(QIntValidator(0,100_000_000))
        self.input_sum.setPlaceholderText("Qancha pul tashlamoqchisiz...")
        self.back_btn = QPushButton(clicked=self.back)
        self.send_btn = QPushButton(clicked=self.send_money)
        self.money_info = QLabel()
        self.back_btn.setIcon(QIcon("back_icon.png"))
        self.send_btn.setIcon(QIcon("send_icon.png"))
        self.card_number.hide()
        self.search_btn.hide()
        self.info_btn.hide()
        self.info_lbl.hide()

        self.h_tr1_lay.addWidget(self.back_btn)
        self.h_tr1_lay.addWidget(self.info)

        self.h_tr2_lay.addWidget(self.input_sum)
        self.h_tr2_lay.addWidget(self.send_btn)

        self.main_ver.addLayout(self.h_tr1_lay)
        self.main_ver.addWidget(self.money_info)
        self.money_info.hide()
        self.main_ver.setAlignment(self.h_tr1_lay, Qt.AlignTop)
        self.main_ver.addLayout(self.h_tr2_lay)

        self.setLayout(self.main_ver)
        self.show()


    def back(self):
        self.back_btn.hide()
        self.input_sum.hide()
        self.info.hide()
        self.send_btn.hide()
        self.info_btn.show()
        self.card_number.show()
        self.search_btn.show()
        # self.info_lbl.show()
    
    def send_money(self):
        if self.data[self.my_card.text()]["SUM"]>=self.data[self.card_number.text()]["SUM"]:
            self.data[self.my_card.text()]["SUM"] -= int(self.input_sum.text())
            self.data[self.card_number.text()]["SUM"] += int(self.input_sum.text())
            
            with open("data.json","w") as f:
                json.dump(self.data,f,indent=4)
            self.money_info.setText("Succesfull!!!")
            self.money_info.setStyleSheet("color:green")
            self.money_info.show()
        else:
            self.money_info.setText("You don't have this money")
            self.money_info.setStyleSheet("color:red")
            self.money_info.show()
        
    # def check(self):
    #     winx = QWidget()
    #     winx.setStyleSheet("font:20px")
    #     self.main = QVBoxLayout()
    #     self.my_card = QLineEdit()
    #     self.my_card.setPlaceholderText("Your card number...")
    #     self.tel_num =  QLineEdit()
    #     self.submit_btn = QPushButton("Submit")
    #     self.tel_num.setPlaceholderText("Phone number")
    #     reg_ex = QRegExp("^\\998\\s?\\d{2}\\s?\\d{3}\\s?\\d{2}\\s?\\d{2}$")
    #     validator = QRegExpValidator(reg_ex, self.tel_num)
    #     self.m_y = QLineEdit()
    #     self.m_y.setPlaceholderText("MM/YY")
    #     reg_ex = QRegExp("^(0[1-9]|1[0-2])/([0-9]{2})$")
    #     validator = QRegExpValidator(reg_ex, self.m_y)
    #     self.m_y.setValidator(validator)
    #     self.main.addWidget(self.my_card)
    #     self.main.addWidget(self.tel_num)
    #     self.main.addWidget(self.submit_btn)
    #     winx.setLayout(self.main)
    #     with open("data.json") as f:
    #         self.data = json.load(f)
    #     # self.submit_btn.clicked.connect(self.returnx)
    #     winx.show()
    #     app.exec_()
        # if self.submit_btn.clicked.connect(self.returnx):
        #     self.show()
        #     winx.hide()
        # else:
        #     print("kajbkasbc")
        
    # def returnx(self):
    #     if self.my_card.text() in self.data:
    #         print("hvschva")
    #         for i in self.data:
    #             if self.data[i]["number"] == int(self.tel_num.text()):
    #                 return True
    #     else:
    #         return False
 
        
        
        
        
if __name__ == "__main__":
        app = QApplication([])
        win = Transfers_()
        win.show()
        app.exec_()