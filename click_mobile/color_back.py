from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QListWidget
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from PyQt5.QtGui import QLinearGradient, QBrush, QColor, QPalette, QPainter

class GradientWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(400, 700)
        self.original_color = QColor("#01b5ff")
        self.target_color = QColor("white")
        self.gradient = QLinearGradient(0, 0, 0, self.height())
        self.gradient.setColorAt(0, self.original_color)
        self.gradient.setColorAt(1, self.target_color)

    def set_gradient(self, start_color, end_color):
        self.gradient.setColorAt(0, start_color)
        self.gradient.setColorAt(1, end_color)
        self.update()  # Update the widget to apply the gradient

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QBrush(self.gradient))
        painter.drawRect(self.rect())

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400, 700)

        # Create and configure the main layout
        self.main_layout = QVBoxLayout(self)
        
        # Create and configure the gradient widget
        self.gradient_widget = GradientWidget(self)
        self.gradient_widget.setGeometry(0, 0, 400, 700)  # Position and size of gradient widget
        self.gradient_widget.setStyleSheet("background: transparent;")

        # Create and configure the slide widget
        self.slide = QWidget(self)
        self.slide.setGeometry(0, 0, 200, 700)  # Position and size of slide widget
        self.slide.setStyleSheet("background-color: lightgray;")
        self.slide.hide()  # Initially hidden

        # Create other widge
if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
