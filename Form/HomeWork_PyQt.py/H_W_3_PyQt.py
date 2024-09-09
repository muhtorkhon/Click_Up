from random import shuffle

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(220,300)

        self.v_main_lay = QVBoxLayout()
        self.grid_lay = QGridLayout()
        self.h_btn_lay = QHBoxLayout()

        self.btn1 = QPushButton("1", clicked=lambda: self.Btn(self.btn1))
        self.btn2 = QPushButton("2", clicked=lambda: self.Btn(self.btn2))
        self.btn3 = QPushButton("3", clicked=lambda: self.Btn(self.btn3))
        self.btn4 = QPushButton("4", clicked=lambda: self.Btn(self.btn4))
        self.btn5 = QPushButton("5", clicked=lambda: self.Btn(self.btn5))
        self.btn6 = QPushButton("6", clicked=lambda: self.Btn(self.btn6))
        self.btn7 = QPushButton("7", clicked=lambda: self.Btn(self.btn7))
        self.btn8 = QPushButton("8", clicked=lambda: self.Btn(self.btn8))
        self.btn9 = QPushButton("9", clicked=lambda: self.Btn(self.btn9))
        self.btn10 = QPushButton("10", clicked=lambda: self.Btn(self.btn10))
        self.btn11 = QPushButton("11", clicked=lambda: self.Btn(self.btn11))
        self.btn12 = QPushButton("12", clicked=lambda: self.Btn(self.btn12))
        self.btn13 = QPushButton("13", clicked=lambda: self.Btn(self.btn13))
        self.btn14 = QPushButton("14", clicked=lambda: self.Btn(self.btn14))
        self.btn15 = QPushButton("15", clicked=lambda: self.Btn(self.btn15))
        self.btn16 = QPushButton("", clicked=lambda:   self.Btn(self.btn16))

        self.lst = [self.btn1,self.btn2,self.btn3,self.btn4,self.btn5,self.btn6,
                    self.btn7,self.btn8,self.btn9,self.btn10,self.btn11,self.btn12,
                    self.btn13,self.btn14,self.btn15 ,self.btn16]
          
        self.lbl_counter = 0
        self.lbl = QLabel("")
        self.lbl.setAlignment(Qt.AlignCenter)

        self.start_btn = QPushButton("START", clicked=self.Start)

        self.finish_btn = QPushButton("FINISH", clicked=self.Finish)
        self.finish_btn.hide()

        self.exit_btn = QPushButton("EXIT", clicked=exit)

        index = 0
        for i in range(4):
            for j in range(4):
                self.grid_lay.addWidget(self.lst[index], i, j)
                self.lst[index].setFixedSize(50,50)
                self.lst[index].setStyleSheet("font-size:20px")
                self.lst[index].setEnabled(False)
                index+=1

        self.h_btn_lay.addWidget(self.start_btn)
        self.h_btn_lay.addWidget(self.finish_btn)
        self.h_btn_lay.addWidget(self.exit_btn)

        self.v_main_lay.addLayout(self.grid_lay)
        self.v_main_lay.addWidget(self.lbl)
        self.v_main_lay.addLayout(self.h_btn_lay)

        self.setLayout(self.v_main_lay)

    def Start(self):
        self.start_btn.hide()
        self.exit_btn.hide()
        self.finish_btn.show()

        sonlar = [i.text() for i in self.lst]
        shuffle(sonlar)

        for index, btn in enumerate(self.lst):
            btn.setText(sonlar[index])
            btn.setEnabled(True)

        self.lbl.setText(str(self.lbl_counter))

    def Finish(self):
        self.finish_btn.hide()
        self.start_btn.show()
        self.exit_btn.show()

        for i in self.lst:
            i.setEnabled(False)

        for i in range(15):
            self.lst[i].setText(f"{i+1}")
        self.lst[-1].setText("")

        self.lbl_counter = 0
        self.lbl.setText("")

    def Btn(self, btn):
        if btn.text():
            if btn == self.btn1:
                if self.btn2.text() == "":
                    self.btn2.setText(self.btn1.text())
                    self.btn1.setText("")
                    self.lbl_counter+=1
                elif self.btn5.text() == "":
                    self.btn5.setText(self.btn1.text())
                    self.btn1.setText("")
                    self.lbl_counter+=1
            elif btn == self.btn13:
                if self.btn9.text() == "":
                    self.btn9.setText(self.btn13.text())
                    self.btn13.setText("")
                    self.lbl_counter+=1
                elif self.btn14.text() == "":
                    self.btn14.setText(self.btn13.text())
                    self.btn13.setText("")
                    self.lbl_counter+=1
            elif btn == self.btn16:
                if self.btn12.text() == "":
                    self.btn12.setText(self.btn16.text())
                    self.btn16.setText("")
                    self.lbl_counter+=1
                elif self.btn15.text() == "":
                    self.btn15.setText(self.btn16.text())
                    self.btn16.setText("")
                    self.lbl_counter+=1
            elif btn == self.btn4:
                if self.btn3.text() == "":
                    self.btn3.setText(self.btn4.text())
                    self.btn4.setText("")
                    self.lbl_counter+=1
                elif self.btn8.text() == "":
                    self.btn8.setText(self.btn4.text())
                    self.btn4.setText("")
                    self.lbl_counter+=1
            elif btn == self.btn2:
                if self.btn3.text() == "":
                    self.btn3.setText(self.btn2.text())
                    self.btn2.setText("")
                    self.lbl_counter+=1
                elif self.btn6.text() == "":
                    self.btn6.setText(self.btn2.text())
                    self.btn2.setText("")
                    self.lbl_counter+=1
                elif self.btn1.text() == "":
                    self.btn1.setText(self.btn2.text())
                    self.btn2.setText("")
                    self.lbl_counter+=1
            elif btn == self.btn3:
                if self.btn2.text() == "":
                    self.btn2.setText(self.btn3.text())
                    self.btn3.setText("")
                    self.lbl_counter+=1
                elif self.btn4.text() == "":
                    self.btn4.setText(self.btn3.text())
                    self.btn3.setText("")
                    self.lbl_counter+=1
                elif self.btn7.text() == "":
                    self.btn7.setText(self.btn3.text())
                    self.btn3.setText("")
                    self.lbl_counter+=1
            elif btn == self.btn8:
                if self.btn4.text() == "":
                    self.btn4.setText(self.btn8.text())
                    self.btn8.setText("")
                    self.lbl_counter+=1
                elif self.btn7.text() == "":
                    self.btn7.setText(self.btn8.text())
                    self.btn8.setText("")
                    self.lbl_counter+=1
                elif self.btn12.text() == "":
                    self.btn12.setText(self.btn8.text())
                    self.btn8.setText("")
                    self.lbl_counter+=1
            elif btn == self.btn12:
                if self.btn11.text() == "":
                    self.btn11.setText(self.btn12.text())
                    self.btn12.setText("")
                    self.lbl_counter+=1
                elif self.btn8.text() == "":
                    self.btn8.setText(self.btn12.text())
                    self.btn12.setText("")
                    self.lbl_counter+=1
                elif self.btn16.text() == "":
                    self.btn16.setText(self.btn12.text())
                    self.btn12.setText("")
                    self.lbl_counter+=1
            elif btn == self.btn15:
                if self.btn11.text() == "":
                    self.btn11.setText(self.btn15.text())
                    self.btn15.setText("")
                    self.lbl_counter+=1
                elif self.btn14.text() == "":
                    self.btn14.setText(self.btn15.text())
                    self.btn15.setText("")
                    self.lbl_counter+=1
                elif self.btn16.text() == "":
                    self.btn16.setText(self.btn15.text())
                    self.btn15.setText("")
                    self.lbl_counter+=1
            elif btn == self.btn14:
                if self.btn13.text() == "":
                    self.btn13.setText(self.btn14.text())
                    self.btn14.setText("")
                    self.lbl_counter+=1
                elif self.btn10.text() == "":
                    self.btn10.setText(self.btn14.text())
                    self.btn14.setText("")
                    self.lbl_counter+=1
                elif self.btn15.text() == "":
                    self.btn15.setText(self.btn14.text())
                    self.btn14.setText("")
                    self.lbl_counter+=1
            elif btn == self.btn9:
                if self.btn5.text() == "":
                    self.btn5.setText(self.btn9.text())
                    self.btn9.setText("")
                    self.lbl_counter+=1
                elif self.btn10.text() == "":
                    self.btn10.setText(self.btn9.text())
                    self.btn9.setText("")
                    self.lbl_counter+=1
                elif self.btn13.text() == "":
                    self.btn13.setText(self.btn9.text())
                    self.btn9.setText("")
                    self.lbl_counter+=1
            elif btn == self.btn5:
                if self.btn1.text() == "":
                    self.btn1.setText(self.btn5.text())
                    self.btn5.setText("")
                    self.lbl_counter+=1
                elif self.btn6.text() == "":
                    self.btn6.setText(self.btn5.text())
                    self.btn5.setText("")
                    self.lbl_counter+=1
                elif self.btn9.text() == "":
                    self.btn9.setText(self.btn5.text())
                    self.btn5.setText("")
                    self.lbl_counter+=1
            elif btn == self.btn6:
                if self.btn2.text() == "":
                    self.btn2.setText(self.btn6.text())
                    self.btn6.setText("")
                    self.lbl_counter+=1
                elif self.btn5.text() == "":
                    self.btn5.setText(self.btn6.text())
                    self.btn6.setText("")
                    self.lbl_counter+=1
                elif self.btn7.text() == "":
                    self.btn7.setText(self.btn6.text())
                    self.btn6.setText("")
                    self.lbl_counter+=1
                elif self.btn10.text() == "":
                    self.btn10.setText(self.btn6.text())
                    self.btn6.setText("")
                    self.lbl_counter+=1
            elif btn == self.btn7:
                if self.btn3.text() == "":
                    self.btn3.setText(self.btn7.text())
                    self.btn7.setText("")
                    self.lbl_counter+=1
                elif self.btn8.text() == "":
                    self.btn8.setText(self.btn7.text())
                    self.btn7.setText("")
                    self.lbl_counter+=1
                elif self.btn6.text() == "":
                    self.btn6.setText(self.btn7.text())
                    self.btn7.setText("")
                    self.lbl_counter+=1
                elif self.btn11.text() == "":
                    self.btn11.setText(self.btn7.text())
                    self.btn7.setText("")
                    self.lbl_counter+=1
            elif btn == self.btn10:
                if self.btn11.text() == "":
                    self.btn11.setText(self.btn10.text())
                    self.btn10.setText("")
                    self.lbl_counter+=1
                elif self.btn9.text() == "":
                    self.btn9.setText(self.btn10.text())
                    self.btn10.setText("")
                    self.lbl_counter+=1
                elif self.btn6.text() == "":
                    self.btn6.setText(self.btn10.text())
                    self.btn10.setText("")
                    self.lbl_counter+=1
                elif self.btn14.text() == "":
                    self.btn14.setText(self.btn10.text())
                    self.btn10.setText("")
                    self.lbl_counter+=1
            elif btn == self.btn11:
                if self.btn10.text() == "":
                    self.btn10.setText(self.btn11.text())
                    self.btn11.setText("")
                    self.lbl_counter+=1
                elif self.btn12.text() == "":
                    self.btn12.setText(self.btn11.text())
                    self.btn11.setText("")
                    self.lbl_counter+=1
                elif self.btn7.text() == "":
                    self.btn7.setText(self.btn11.text())
                    self.btn11.setText("")
                    self.lbl_counter+=1
                elif self.btn15.text() == "":
                    self.btn15.setText(self.btn11.text())
                    self.btn11.setText("")
                    self.lbl_counter+=1
            self.lbl.setText(f"{self.lbl_counter}")
            self.Check()

    def Check(self):
        tekshiruv = [str(i+1) for i in range(15)] 
        tekshiruv.append("")

        haqiqiy = [i.text() for i in self.lst]

        if tekshiruv==haqiqiy:
            self.Finish()
            self.msg = QMessageBox()
            self.msg.setStyleSheet("background-color:lightgreen")
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setText("Congratulations")
            self.msg.exec_()

app = QApplication([])
win = MyWindow()
win.show()
app.exec_()