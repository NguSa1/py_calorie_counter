from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QPushButton, QDialog, QLabel, QLineEdit
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

from excel import excel_write_test, read_cell, delete_cell
# from PyQt5.QtGui import QIcon

cell_var = "B2"
calorie_goal = 1600


class CalorieTrackerGUI(QMainWindow):

    def __init__(self):
        super(CalorieTrackerGUI, self).__init__()

        win = QWidget(self)
        self.setCentralWidget(win)
        self.setWindowTitle("Dinos Calorie-Tracker")

        # makes a grid layout and sets it to the widget
        grid = QGridLayout()
        win.setLayout(grid)

        # Buttons and Checkboxes etc.

        add_calories_button = QPushButton("Add calories")
        add_calories_button.clicked.connect(self.add_calories_button_clicked)
        add_calories_button.clicked.connect(excel_write_test)

        self.calories_blank_line = QLineEdit()

        self.calories_left_label = QLabel("Calories left for Today: ")

        self.reset_button = QPushButton("Reset Calories")
        self.reset_button.clicked.connect(self.reset)

        # grid; button placement
        row = 0
        grid.addWidget(QLabel("Calorie Goal: " + str(calorie_goal)), row, 0, 1, 1)

        row += 1
        grid.addWidget(self.calories_blank_line, row, 0, 1, 1)
        grid.addWidget(add_calories_button, row, 1, 1, 1)

        row += 1
        grid.addWidget(self.calories_left_label, row, 0, 1, 1)

        row += 1
        grid.addWidget(self.reset_button, row, 1, 1, 1)
        self.show()

    def add_calories_button_clicked(self):

        arg = int(self.calories_blank_line.text())
        excel_write_test(arg)
        self.calories_blank_line.clear()
        self.calories_left_label.setText("Calories left for Today: " + str(calorie_goal - read_cell(cell_var)))

    def reset(self):
        delete_cell(cell_var)
        self.calories_left_label.setText("Calories left for Today: " + str(calorie_goal))
