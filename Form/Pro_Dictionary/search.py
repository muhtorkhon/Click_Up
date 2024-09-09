from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from menu import MyWindow

class SearchWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("font-size:20px")
        self.setWindowTitle("Search")
        self.main = QVBoxLayout()
        self.h_rad = QHBoxLayout()
        self.h_line_btn = QHBoxLayout()
        
        self.rad_en = QRadioButton("English")
        self.rad_uz = QRadioButton("Uzbek")
        self.line = QLineEdit()
        self.btn_search = QPushButton("Search", clicked=self.search)
        self.lbl = QLabel()
        self.lbl.setAlignment(Qt.AlignCenter)
        self.menu = QPushButton("Menu",clicked = self.hide)
        
        self.h_rad.addWidget(self.rad_en)
        self.h_rad.addWidget(self.rad_uz)
        self.h_line_btn.addWidget(self.line)
        self.h_line_btn.addWidget(self.btn_search)
        self.main.addLayout(self.h_rad)
        self.main.addLayout(self.h_line_btn)
        self.main.addWidget(self.lbl)
        self.main.addWidget(self.menu)
        self.setLayout(self.main)
    
    def search(self):
        with open("lugat.txt","r") as f:
            x = False
            self.data = f.read().split("\n")[:-1]
            for i in range(len(self.data)):
                save = self.data[i].split("--->")
                # print(save)
                self.data[i] = save
            # print(self.data)
            if self.rad_en.isChecked():
                for i in range(len(self.data)):
                    if self.line.text() == self.data[i][0]:
                        self.lbl.setText(self.data[i][1])
                        x = True
                if not x:
                    self.lbl.setText("Not founded")
            elif self.rad_uz.isChecked():
                for i in range(len(self.data)):
                    if self.line.text() == self.data[i][1]:
                        self.lbl.setText(self.data[i][0])
                        x = True
                if not x:
                    self.lbl.setText("Not founded")
            else:
                self.lbl.setText("Change languege")
            f.seek(0)
            
                

if __name__ == "__main__":
    app = QApplication([])
    win = MyWindow()
    win.show()
    app.exec_()