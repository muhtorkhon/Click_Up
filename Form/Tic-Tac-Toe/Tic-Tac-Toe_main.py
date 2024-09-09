from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic-Tac-Toe")
        self.setFixedSize(300,350)
        
        self.v_main_lay = QVBoxLayout()
        self.grid_lay = QGridLayout()
        self.h_btn_lay = QHBoxLayout()
        
        self.sts_lbl = QLabel("Очередь игрока X")
        self.sts_lbl.setAlignment(Qt.AlignCenter)
        self.sts_lbl.setFixedHeight(40)
        self.sts_lbl.setStyleSheet("font-size:16px")
        self.v_main_lay.addWidget(self.sts_lbl)
        
        self.btns = []
        for i in range(3):
            row = []
            for j in range(3):
                btn = QPushButton("")
                btn.setFixedSize(70,70)
                btn.setStyleSheet("font-size: 20px") 
                btn.clicked.connect(lambda _, r=i,c=j: self.Handle_Click(r,c))       
                self.grid_lay.addWidget(btn,i,j)
                row.append(btn)
            self.btns.append(row)
        
        self.v_main_lay.addLayout(self.grid_lay)
            
        self.start_btn = QPushButton("Сброс", clicked = self.Start)
        self.h_btn_lay.addWidget(self.start_btn)
        
        self.exit_btn = QPushButton("Выход", clicked = exit)
        self.h_btn_lay.addWidget(self.exit_btn)
        
        self.v_main_lay.addLayout(self.h_btn_lay)
        
        self.setLayout(self.v_main_lay)    
        
        self.current_player = 'X'
        self.game_palyer_key = True  
    
    def Handle_Click(self, row, col):
        if self.game_palyer_key and self.btns[row][col].text() == "":
            self.btns[row][col].setText(self.current_player)
            if self.Check_Win():
                self.sts_lbl.setText(f"Игрок {self.current_player} победил!")
                self.game_palyer_key = False
            elif self.Check_Draw():
                self.sts_lbl.setText("Ничья")
                self.game_palyer_key = False
            else:
                if self.current_player == 'X':
                    self.current_player = 'O'
                else:
                    self.current_player = 'X'
                self.sts_lbl.setText(f"Очередь игрока {self.current_player}")    
            
    def Check_Win(self):
        for i in range(3):
            if self.btns[i][0].text() == self.btns[i][1].text() == self.btns[i][2].text() != "":
                return True
            if self.btns[0][i].text() == self.btns[1][i].text() == self.btns[2][i].text() != "":
                return True
        if self.btns[0][0].text() == self.btns[1][1].text() == self.btns[2][2].text() != "":
            return True
        if self.btns[0][2].text() == self.btns[1][1].text() == self.btns[2][0] != "":
            return True
        return False
               
    def Check_Draw(self):
        for i in self.btns:
            for j in i:
                if j.text() == "":
                    return False
        return True        
    
    def Start(self):
        self.current_player = "X"
        self.game_palyer_key = True
        self.sts_lbl.setText("Очередь игрока X")
        for i in self.btns:
            for j in i:
                j.setText("")

        
    
    
    
app = QApplication([])
win = MyWindow() 
win.show()
app.exec_()   