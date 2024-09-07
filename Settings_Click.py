from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Setting_(QWidget):
  def __init__(self) -> None:
    super().__init__()



if __name__ == "__main__":
  app = QApplication([])
  win = Setting_()
  win.show()
  app.exec_()