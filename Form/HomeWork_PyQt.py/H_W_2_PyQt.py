from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QHBoxLayout, QPushButton, QLabel


class TicTacToeGame(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic-Tac-Toe")
        self.setFixedSize(300, 350)

        self.v_layout = QVBoxLayout()
        self.grid_layout = QGridLayout()
        self.h_layout = QHBoxLayout()

        self.status_label = QLabel("Player X's Turn")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setFixedHeight(50)
        self.status_label.setStyleSheet("font-size: 16px;")
        self.v_layout.addWidget(self.status_label)

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = QPushButton("")
                button.setFixedSize(80, 80)
                button.setStyleSheet("font-size: 24px;")
                button.clicked.connect(lambda _, r=i, c=j: self.handle_click(r, c))
                self.grid_layout.addWidget(button, i, j)
                row.append(button)
            self.buttons.append(row)

        self.v_layout.addLayout(self.grid_layout)

        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self.reset_game)
        self.h_layout.addWidget(self.reset_button)

        self.exit_button = QPushButton("Exit")
        self.exit_button.clicked.connect(self.close)
        self.h_layout.addWidget(self.exit_button)

        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)

        self.current_player = 'X'
        self.game_active = True

    def handle_click(self, row, col):
        if self.game_active and self.buttons[row][col].text() == "":
            self.buttons[row][col].setText(self.current_player)
            if self.check_winner():
                self.status_label.setText(f"Player {self.current_player} wins!")
                self.game_active = False
            elif self.check_draw():
                self.status_label.setText("It's a draw!")
                self.game_active = False
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.status_label.setText(f"Player {self.current_player}'s Turn")

    def check_winner(self):
        for i in range(3):
            if self.buttons[i][0].text() == self.buttons[i][1].text() == self.buttons[i][2].text() != "":
                return True
            if self.buttons[0][i].text() == self.buttons[1][i].text() == self.buttons[2][i].text() != "":
                return True
        if self.buttons[0][0].text() == self.buttons[1][1].text() == self.buttons[2][2].text() != "":
            return True
        if self.buttons[0][2].text() == self.buttons[1][1].text() == self.buttons[2][0].text() != "":
            return True
        return False

    def check_draw(self):
        for row in self.buttons:
            for button in row:
                if button.text() == "":
                    return False
        return True

    def reset_game(self):
        self.current_player = 'X'
        self.game_active = True
        self.status_label.setText("Player X's Turn")
        for row in self.buttons:
            for button in row:
                button.setText("")


if __name__ == "__main__":
    app = QApplication([])
    window = TicTacToeGame()
    window.show()
    app.exec_()

