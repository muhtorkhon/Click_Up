from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Main_services_(QWidget):
  def __init__(self) -> None:
    super().__init__()



if __name__ == "__main__":
  app = QApplication([])
  win = Main_services_()
  win.show()
  app.exec_()