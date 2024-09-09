from PyQt5.QtWidgets import QApplication , QWidget , QLabel , QPushButton  , QLineEdit 
from PyQt5.QtGui import QIcon

# app = QApplication([]) # for applicatin    (default)
# win =  QWidget()  # for window    (default)

# win.move() # win.move(x,y) moves the window along x/y the coordinate axes

# win.setFixedSize() # (w,h) changes width and height 

# win.setGeometry() # (x,y,w,h) gets inside this 2 methods (setFixedSize()  move())

# win.setWindowTitle("Nosferatu Z0dd") # Naming the window 

# win.setWindowIcon(QIcon()) # QIcon(==>Path<==)  puts picture (Library =>PyQt5.QtGui =>QIqon) 

# --------------------------------------------------------------------------------- #

# lbl = QLabel("Nosferatu: ", win) # Naming lable

# lbl.move(20,100) # size of lable

# lbl.setStyleSheet("background-color:lightblue; color:red; font-size:20px")# UI decorations

# lbl.setText("Nigga") # chenged Text Library

# --------------------------------------------------------------------------------- #

# edit = QLineEdit(win)

# edit.setStyleSheet("background-color:lightblue; color:red; font-size:20px")#UI decorations
# edit.setPlaceholderText("Group name ...") # Placeholder text (transparent)

# --------------------------------------------------------------------------------- #

# btn = QPushButton("Submit",win)

# def forScreen():
  # txt = edit.text() # Writing text
  # lbl.setText(txt)  # changing lable text
  # lbl.adjustSize()  # for ...

# btn.clicked.connect(forScreen) # button commant 


# win.show() # just shows a window    (default)
# app.exec_() # keeps circulation  




