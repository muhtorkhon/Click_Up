from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class SlideWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        if parent:
            self.setGeometry(-200, 0, 200, parent.height())  
        else:
            self.setGeometry(-200, 0, 200, 600)  

        self.setStyleSheet("background-color: #e2e4f0;")

        layout = QVBoxLayout(self)
        self.image=QLabel()
        image=QPixmap("slide_bar.jpg")
        scaled_pixmap = image.scaled(280, 600, Qt.KeepAspectRatio)
        self.image.setPixmap(scaled_pixmap) 
        layout.addWidget(self.image)
        self.setLayout(layout)

    def toggle(self):
        if self.geometry().x() < 0:
            self.slide_out()
        else:
            self.slide_in()

    def slide_in(self):
        animation = QPropertyAnimation(self, b"geometry")
        animation.setDuration(500)
        animation.setStartValue(QRect(-200, 0, 200, self.parent().height()))
        animation.setEndValue(QRect(0, 0, 200, self.parent().height()))
        animation.start()

    def slide_out(self):
        animation = QPropertyAnimation(self, b"geometry")
        animation.setDuration(500)
        animation.setStartValue(QRect(0, 0, 200, self.parent().height()))
        animation.setEndValue(QRect(-200, 0, 200, self.parent().height()))
        animation.start()

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            if not self.geometry().contains(self.mapFromGlobal(event.globalPos())):
                self.slide_in()
