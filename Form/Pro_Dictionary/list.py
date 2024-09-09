from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from menu import MyWindow

class ListWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("font-size:20px")
        self.setWindowTitle("Dictionary")
        self.lay = QVBoxLayout()
        self.menu = QPushButton("MENU",clicked=self.hide)
        self.en_uz = QLabel("English   -   Uzbek")
        with open("lugat.txt","r") as f:
            self.data = f.read().split("\n")
        print(self.data)  
        for i in range(len(self.data)):
            self.data[i] = self.data[i].split('--->')
        print(self.data)
        self.ls = QListWidget()
        for i in self.data:
            if len(i)==2:
                self.ls.addItem(f"{i[0]} \t   {i[1]}")
        self.ls.sortItems(Qt.AscendingOrder)    
        self.lay.addWidget(self.en_uz)
        self.lay.addWidget(self.ls)
        self.lay.addWidget(self.menu)
        self.setLayout(self.lay)



if __name__ == "__main__":
    app = QApplication([])
    win = MyWindow()
    win.show()
    app.exec_()
    
    
    
    