# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox, QLabel, QPushButton, QMessageBox, QDialog

# class MenuCategoryWindow(QDialog):
#     def __init__(self, category_name, items, parent=None):
#         super().__init__(parent)
#         self.setWindowTitle(category_name)
#         self.setGeometry(150, 150, 300, 300)

#         self.layout = QVBoxLayout()

#         self.checkboxes = {}
#         for item, price in items.items():
#             checkbox = QCheckBox(f"{item} ({price} UZS)")
#             self.layout.addWidget(checkbox)
#             self.checkboxes[checkbox] = price

#         self.back_button = QPushButton("Back")
#         self.back_button.clicked.connect(self.close)
#         self.layout.addWidget(self.back_button)

#         self.setLayout(self.layout)

# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Restaurant Menu")
#         self.setGeometry(100, 100, 400, 400)

#         self.layout = QVBoxLayout()

#         self.first_courses = {
#             "Plov": 15000,
#             "Shurva": 12000,
#             "Samsa": 8000,
#             "Lagman": 14000,
#             "Manti": 13000
#         }
#         self.first_course_button = QPushButton("First Courses")
#         self.first_course_button.clicked.connect(lambda: self.open_menu_category("First Courses", self.first_courses))
#         self.layout.addWidget(self.first_course_button)

#         self.second_courses = {
#             "Shashlik": 20000,
#             "Kebab": 18000,
#             "Chicken": 15000,
#             "Beef Steak": 25000,
#             "Qiyma": 17000
#         }
#         self.second_course_button = QPushButton("Second Courses")
#         self.second_course_button.clicked.connect(lambda: self.open_menu_category("Second Courses", self.second_courses))
#         self.layout.addWidget(self.second_course_button)

#         self.drinks = {
#             "Tea": 5000,
#             "Cola": 8000,
#             "Juice": 10000,
#             "Water": 2000,
#             "Coffee": 9000
#         }
#         self.drink_button = QPushButton("Drinks")
#         self.drink_button.clicked.connect(lambda: self.open_menu_category("Drinks", self.drinks))
#         self.layout.addWidget(self.drink_button)

#         self.desserts = {
#             "Cake": 12000,
#             "Ice Cream": 10000,
#             "Pie": 15000,
#             "Pudding": 9000,
#             "Strawberry Shake": 11000
#         }
#         self.dessert_button = QPushButton("Desserts")
#         self.dessert_button.clicked.connect(lambda: self.open_menu_category("Desserts", self.desserts))
#         self.layout.addWidget(self.dessert_button)

#         self.check_button = QPushButton("Show Check")
#         self.check_button.clicked.connect(self.show_check)
#         self.layout.addWidget(self.check_button)

#         self.setLayout(self.layout)

#         self.selected_items = {
#             "First Courses": [],
#             "Second Courses": [],
#             "Drinks": [],
#             "Desserts": []
#         }

#     def open_menu_category(self, category_name, items):
#         self.menu_category_window = MenuCategoryWindow(category_name, items)
#         self.menu_category_window.exec_()

#         selected = []
#         for checkbox, price in self.menu_category_window.checkboxes.items():
#             if checkbox.isChecked():
#                 selected.append((checkbox.text(), price))
#         self.selected_items[category_name] = selected

#     def show_check(self):
#         check = QMessageBox()
#         check.setWindowTitle("Check")
        
#         check_text = "Check:\n\n"
        
#         check_text += "First Courses:\n"
#         check_text += self.get_selected_items_text("First Courses")
        
#         check_text += "\nSecond Courses:\n"
#         check_text += self.get_selected_items_text("Second Courses")
        
#         check_text += "\nDrinks:\n"
#         check_text += self.get_selected_items_text("Drinks")
        
#         check_text += "\nDesserts:\n"
#         check_text += self.get_selected_items_text("Desserts")
        
#         check.setText(check_text)
#         check.exec_()

#     def get_selected_items_text(self, category_name):
#         selected_items_text = ""
#         for item, price in self.selected_items[category_name]:
#             selected_items_text += f"{item}\n"
#         if not selected_items_text:
#             selected_items_text = "Nothing selected\n"
#         return selected_items_text


# app = QApplication([])
# win = MyWindow()
# win.show()
# app.exec_()

