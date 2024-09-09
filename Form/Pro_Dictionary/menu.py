from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("font-size:20px")
        self.h_main_lay = QHBoxLayout()
        self.v_btn_lay = QVBoxLayout()

        self.add_btn = QPushButton("ADD", clicked=self.Add)
        self.search_btn = QPushButton("SEARCH", clicked=self.Search)
        self.list_btn = QPushButton("LIST", clicked=self.List)
        self.exit_btn = QPushButton("EXIT", clicked=self.exit_app)

        self.v_btn_lay.addWidget(self.add_btn)
        self.v_btn_lay.addWidget(self.search_btn)
        self.v_btn_lay.addWidget(self.list_btn)
        self.v_btn_lay.addWidget(self.exit_btn)

        self.h_main_lay.addStretch()
        self.h_main_lay.addLayout(self.v_btn_lay)
        self.h_main_lay.addStretch()

        self.setLayout(self.h_main_lay)
    
    def Add(self):
        from add import AddWindow  
        self.add_window = AddWindow()
        self.add_window.show()

    def Search(self):
        from search import SearchWindow
        self.search_window = SearchWindow()
        self.search_window.show()  

    def List(self):
        from list import ListWindow
        self.listWindow = ListWindow()
        self.listWindow.show()
        
    def exit_app(self):
        QApplication.quit()  
        
if __name__ == "__main__":
    app = QApplication([])
    win = MyWindow()
    win.show()
    app.exec_()        
