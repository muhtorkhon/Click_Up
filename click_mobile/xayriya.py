from PyQt5.QtWidgets import *
class Xayriya(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 700)
        self.stacked_widget = QStackedWidget()

        # Xayriya sahifasini yaratish
        self.xayriya_page = Xayriya()

        # QStackedWidgetga qo'shish
        self.stacked_widget.addWidget(self.xayriya_page)

        # O'zgaruvchini qo'shish
        self.stacked_widget.addWidget(self)  # Asosiy sahifa

        # O'zgaruvchilarni yaratish va layoutni sozlash
        # ...

    def charity(self):
        self.stacked_widget.setCurrentWidget(self.xayriya_page)
