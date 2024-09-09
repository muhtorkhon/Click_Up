from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QLineEdit,QComboBox
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QMessageBox, QCheckBox, QRadioButton

""" 1 lesson"""

# At lesson 1  Introduction
"""
class MyWindow(QWidget):
  def __init__(self):
    super().__init__()
    
    self.blue_btn = QPushButton("Blue", self)
    self.blue_btn.move(50,50)
    self.blue_btn.clicked.connect(self.Blue)
    
    self.red_btn = QPushButton("Red", self)
    self.red_btn.move(50,100)
    self.red_btn.clicked.connect(self.Red)
    
    self.dark_btn = QPushButton("Dark", self)
    self.dark_btn.move(50,150)
    self.dark_btn.clicked.connect(self.Dark)

  def Blue(self):
    self.setStyleSheet("background:blue")
  
  def Red(self):
    self.setStyleSheet("background:red")
  
  def Dark(self):
    self.setStyleSheet("background:lightblack")

app = QApplication([])
win = MyWindow()

win.show()
app.exec_()

"""

# At lesson 2    Write in file
"""
class MyWindow(QWidget):
  def __init__(self):
    super().__init__()
    self.setFixedSize(400,400)
    self.setStyleSheet("font-size:20px")
    
    self.Name_lbl = QLabel("Name",self)
    self.Name_lbl.move(30,100)
    
    self.Age_lbl = QLabel("Age",self)
    self.Age_lbl.move(30,200)
    
    
    self.Name_edit = QLineEdit(self)
    self.Name_edit.move(100,100)
    self.Name_edit.setPlaceholderText("...")
    
    self.Age_edit = QLineEdit(self)
    self.Age_edit.move(100,200)
    self.Age_edit.setPlaceholderText("...")
    
    
    self.btn = QPushButton("Submit",self)
    self.btn.move(120,250)
    self.btn.clicked.connect(self.Submit)
    
  def Submit(self):
    f = open("User.txt", "a")  
    f.write(f"{self.Name_edit.text()} {self.Age_edit.text()}")
    self.Name_edit.clear()
    self.Age_edit.clear()
    
    f.close()

app = QApplication([])
win = MyWindow()

win.show()
app.exec_()
"""

# At lesson 3  like colculator
"""
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(300,250)

        self.lamp = False
        self.chiqorcha = True

        self.miqdor = 0

        self.lbl = QLabel(self)
        self.lbl.setStyleSheet("font-size:20px")
        self.move(10,100)

        self.reset_btn = QPushButton("R",self)
        self.reset_btn.move(10, 200)
        self.reset_btn.clicked.connect(self.Reset)

        self.add_btn = QPushButton("+", self)
        self.add_btn.move(105,200)
        self.add_btn.clicked.connect(self.Add)

        self.light_btn = QPushButton("M", self)
        self.light_btn.move(105,150)
        self.light_btn.clicked.connect(self.Light)

        self.on_off_btn = QPushButton("ON", self)
        self.on_off_btn.move(205,200)
        self.on_off_btn.clicked.connect(self.OO)

    def Reset(self):
        if self.lamp:
            self.lbl.setText('0')
            self.miqdor=0

    def Add(self):
        if self.lamp:
            self.lbl.setText(f"{int(self.lbl.text())+1}")
            self.lbl.adjustSize()
            self.miqdor = int(self.lbl.text())

    def OO(self):
        if self.lamp:
            self.on_off_btn.setText("ON")
            self.lamp = False
            self.lbl.setText("")
        else:
            self.on_off_btn.setText("OFF")
            self.lamp = True
            self.lbl.setText(f"{self.miqdor}")
        self.lbl.adjustSize()

    def Light(self):
        if self.chiqorcha:
            self.setStyleSheet("background:white")
            self.chiqorcha = False
        else:
            self.setStyleSheet("background:lightgreen")
            self.chiqorcha = True

        

app = QApplication([])
win = MyWindow()
win.show()
app.exec_()

"""

#  H/W  Calculator with layout
"""
class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 300)
        self.setStyleSheet("font-size:20px")
        
        self.create_interface()

    def create_interface(self):
        # Main layout
        self.v_main_layout = QVBoxLayout() # main vertical

        # edit_display for the calculator
        self.edit_display = QLineEdit()
        self.edit_display.setReadOnly(True)
        self.edit_display.setFixedHeight(35)
        self.edit_display.setAlignment(Qt.AlignRight)
        self.edit_display.setStyleSheet("font-size: 24px;")
        self.v_main_layout.addWidget(self.edit_display)

        # Buttons layout
        v_buttons_layout = QVBoxLayout()

        # Row 1
        row1 = QHBoxLayout()
        self.create_button(row1, "7")
        self.create_button(row1, "8")
        self.create_button(row1, "9")
        self.create_button(row1, "/")
        v_buttons_layout.addLayout(row1)

        # Row 2
        row2 = QHBoxLayout()
        self.create_button(row2, "4")
        self.create_button(row2, "5")
        self.create_button(row2, "6")
        self.create_button(row2, "*")
        v_buttons_layout.addLayout(row2)

        # Row 3
        row3 = QHBoxLayout()
        self.create_button(row3, "1")
        self.create_button(row3, "2")
        self.create_button(row3, "3")
        self.create_button(row3, "-")
        v_buttons_layout.addLayout(row3)

        # Row 4
        row4 = QHBoxLayout()
        self.create_button(row4, "0")
        self.create_button(row4, "C")
        self.create_button(row4, "=")
        self.create_button(row4, "+")
        v_buttons_layout.addLayout(row4)

        # Adding button layout to the main layout
        self.v_main_layout.addLayout(v_buttons_layout)

        # Set the layout to the window
        self.setLayout(self.v_main_layout)

    def create_button(self, layout, text):
        button = QPushButton(text)
        button.setFixedSize(60, 40)
        button.clicked.connect(lambda: self.on_button_click(text))
        layout.addWidget(button)

    def on_button_click(self, text):
        current_text = self.edit_display.text()

        if text == "C":
            self.edit_display.clear()
        elif text == "=":
            try:
                # result = str(eval(current_text))
                self.edit_display.setText(str(eval(current_text)))
            except:
                self.edit_display.setText("Error")
        else:
            self.edit_display.setText(current_text + text)


if __name__ == "__main__":
    app = QApplication([])
    calculator = Calculator()
    calculator.show()
    app.exec_()
"""

""" 2 lesson """

# At lesson 1 ==> Layout
"""
class MyWindow(QWidget):
  def __init__(self):
    super().__init__()
    
    self.main_lay =QVBoxLayout()
    
    self.btn1 = QPushButton("Ok")
    self.btn2 = QPushButton("Back")
    self.btn3 = QPushButton("No")
    
    self.edit1 = QLineEdit()
    self.edit2 = QLineEdit()
    self.edit3 = QLineEdit()


    self.vertical_btn_lay = QVBoxLayout()
    self.vertical_btn_lay.addWidget(self.edit1)
    self.vertical_btn_lay.addWidget(self.edit2)
    self.vertical_btn_lay.addWidget(self.edit3)
    
    # self.setLayout(self.vertical_btn_lay)
    
    self.horozontal_btn_lay = QHBoxLayout()
    self.horozontal_btn_lay.addStretch()
    self.horozontal_btn_lay.addWidget(self.btn1)
    self.horozontal_btn_lay.addWidget(self.btn2)
    self.horozontal_btn_lay.addWidget(self.btn3)
    self.horozontal_btn_lay.addStretch()
    
    # self.setLayout(self.horozontal_btn_lay)
    
    self.main_lay.addLayout(self.vertical_btn_lay)
    self.main_lay.addLayout(self.horozontal_btn_lay)
    
    self.setLayout(self.main_lay)
    
    
    
app = QApplication([]) 
win = MyWindow()
win.show()
app.exec_()
"""

# At lesson 2 ==> QMessageBox
"""
class Mywindow(QWidget):
  def __init__(self):
    super().__init__()
    self.btn = QPushButton("Do not Button",self)
    self.btn.clicked.connect(self.NotButton)
    
    
  def NotButton(self):
    self.massage = QMessageBox()
    self.massage.setWindowTitle("Warning")
    self.massage.setText("ERROR")
    self.massage.setIcon(QMessageBox.Critical) #Information #Question #Warning
    self.massage.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Ok | QMessageBox.Cancel )
    self.massage.buttonClicked.connect(self.MSG_Function)
    
    self.massage.exec_()
    
  def MSG_Function(self, btn):
    if btn.text() == "&Yes":
      self.setStyleSheet("background:lightblue")
    elif btn.text() == "&No":
      self.setStyleSheet("background:red")        
    elif btn.text() == "OK":
      self.setStyleSheet("background:orange")  
    elif btn.text() == "Cancel":
      self.setStyleSheet("background:gray")  
    
       
app = QApplication([])
win = Mywindow()
win.show()
app.exec_()
"""

# At lesson 3 ==> QCheckBox
"""

class Mywindow(QWidget):
  def __init__(self):
    super().__init__()
    self.setStyleSheet("font-size:20px")
    self.setFixedSize(300,280)
    
    self.vertical_Main_lay = QVBoxLayout()
    self.horisont_lbl_lay = QHBoxLayout()
    self.horisontal_btn_lay = QHBoxLayout()
    
    self.lbl = QLabel("Welcome to INDEX")
    
    self.c1 = QCheckBox("BMW -> $100000")
    self.c2 = QCheckBox("Mercides -> $200000")
    self.c3 = QCheckBox("Nissan -> $350000")
    self.c4 = QCheckBox("Camaro -> $250000")
    self.c5 = QCheckBox("Volkswagen ->$50000")
    self.lst = [self.c1 , self.c2 , self.c3 , self.c4 , self.c5]
    
    self.ok_btn = QPushButton("OK")
    self.ok_btn.clicked.connect(self.Ok)
    
    self.buy_btn = QPushButton("Buy")
    self.buy_btn.clicked.connect(self.Buy)
    self.buy_btn.hide()
    
    self.back_btn = QPushButton("Back")
    self.back_btn.clicked.connect(self.Back)
    self.back_btn.hide()
    
    self.exit_btn = QPushButton("Exit")
    self.exit_btn.clicked.connect(exit)
    
    self.horisontal_btn_lay.addStretch()
    self.horisont_lbl_lay.addWidget(self.lbl)
    self.horisontal_btn_lay.addStretch()
    
    self.horisontal_btn_lay.addWidget(self.ok_btn)
    self.horisontal_btn_lay.addWidget(self.back_btn)
    self.horisontal_btn_lay.addWidget(self.buy_btn)
    self.horisontal_btn_lay.addWidget(self.exit_btn)
    
    self.vertical_Main_lay.addLayout(self.horisont_lbl_lay)
    for i in self.lst:
      i.setStyleSheet("background:lightgray")
      self.vertical_Main_lay.addWidget(i)
    self.vertical_Main_lay.addLayout(self.horisontal_btn_lay)
    
    self.setLayout(self.vertical_Main_lay)
  
  
  def Buy(self):
    self.hide()
    self.message = QMessageBox()
    self.message.setIcon(QMessageBox.Information)
    self.message.setText("Congratulation")
    self.message.setStyleSheet("background:lightblue")
    self.message.buttonClicked.connect(self.Return)
    self.message.exec_()
  
  
  def Return(self, btn):
    self.show()
    self.Back()
    for i in self.lst:
      i.setChecked(0)
       
       
  def Ok(self):
    self.ok_btn.hide()
    self.buy_btn.show()
    self.back_btn.show()
    sum = 0
    for i in self.lst:
      if i.isChecked():
        sum += int(i.text().split("$")[-1]) 
      else:
        i.hide()
    self.lbl.setText(f"${sum}")
    
    
  def Back(self):
    self.lbl.setText("Welcome to INDEX")
    self.ok_btn.show()
    self.back_btn.hide()
    self.buy_btn.hide()
    
    for i in self.lst:
      i.show()
       
app = QApplication([])
win = Mywindow()
win.show()
app.exec_()

"""

# At lesson 4 ==> QRadioButton
"""
class MyWindow(QWidget):
  def  __init__(self):
    super().__init__()
    self.setStyleSheet("font-size:20px")
    
    self.vertical_main_lay = QVBoxLayout()
    
    self.lbl = QLabel("Which club is the best?")
    
    self.r1 = QRadioButton("Real Madrid")
    self.r2 = QRadioButton("Barcelona")
    self.r3 = QRadioButton("MC")
    self.r4 = QRadioButton("MU")
    self.r5 = QRadioButton("Bavaria")
    self.lst = [self.r1, self.r2, self.r3, self.r4, self.r5,]
    
    self.btn = QPushButton("Check" , clicked  = self.Check)
    # self.btn.clicked.connect(self.Check)

    self.vertical_main_lay.addWidget(self.lbl)  
    for i in self.lst:
      self.vertical_main_lay.addWidget(i)  
    self.vertical_main_lay.addWidget(self.btn)  
      
    self.setLayout(self.vertical_main_lay)  
      
  def Check(self):
    if self.r1.isChecked():
      self.r1.setStyleSheet("background:lightgreen")
    else:
      for i in self.lst:
        i.setEnabled(False) # one chance to buttton
        i.setStyleSheet("background:red")
      self.r3.setStyleSheet("background:lightgreen")    


app = QApplication([])
win = MyWindow()
win.show()
app.exec_()

"""

# At lesson 5 ==> QComboBox
"""
class MyWindow(QWidget):
  def __init__(self):
    super().__init__()
    self.setStyleSheet("font-size:20px")
    self.vertical_main_lay = QVBoxLayout()
    
    self.lbl = QLabel("Which direction do you want to choose ?")
    
    self.cmb = QComboBox()
    self.lst = ["Foundation","C#","C++","C","Java","Python"]
    self.cmb.addItems(self.lst)
    # self.cmb.addItem("Foundation") # gets only one string
    # self.cmb.addItems(["C#","C++","C","Java","Python"]) # gets list
    self.cmb.activated[str].connect(self.Finish)
    
    
    self.vertical_main_lay.addWidget(self.lbl)
    self.vertical_main_lay.addWidget(self.cmb)
    
    self.setLayout(self.vertical_main_lay)
  
  
  def Finish(self,data):
      indx = self.lst.index(data)
      self.lst.pop(indx)
      self.cmb.removeItem(indx)
      
      
      
app = QApplication([])
win = MyWindow()
win.show()
app.exec_()

"""


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.V_main_lay = QVBoxLayout()
        
        
        
    





if __name__ == "__main__":
    app = QApplication([])
    win = MyWindow()
    win.show()
    app.exec_()




#97.122.09.05
#97.744.57.56 Error
#97.420.47.71