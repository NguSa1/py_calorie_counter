from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QPushButton, QLabel, QLineEdit, QDialog, QInputDialog
from openpyxl import load_workbook

from globals import get_global, update_global
from excel import excel_write_test, read_cell, write_today_date_to_excel, write_weight
from json_writer import json_reset, json_load


class CalorieTrackerGUI(QMainWindow):

    def __init__(self):
        super(CalorieTrackerGUI, self).__init__()

        # setting the widget
        win = QWidget(self)
        self.setCentralWidget(win)
        self.setWindowTitle("Calorie Tracker")

        # makes a grid layout and sets it to the widget
        grid = QGridLayout()
        win.setLayout(grid)

        # Buttons and Checkboxes etc.
        add_calories_button = QPushButton("Add calories")
        add_calories_button.clicked.connect(self.add_calories_button_clicked)

        self.calories_blank_line = QLineEdit()

        self.calories_left_label = QLabel("Calories left for Today: ")

        reset_button = QPushButton("Start of the day")
        reset_button.clicked.connect(self.start_day)

        note_today_weight_button = QPushButton("Enter today's weight")
        note_today_weight_button.clicked.connect(self.getdouble_weight)

        # grid; button placement
        row = 0
        grid.addWidget(QLabel("Calorie Goal: " + str(get_global("calorie_goal"))), row, 0, 1, 1)

        row += 1
        grid.addWidget(self.calories_blank_line, row, 0, 1, 1)
        grid.addWidget(add_calories_button, row, 1, 1, 1)

        row += 1
        grid.addWidget(self.calories_left_label, row, 0, 1, 1)

        row += 1
        grid.addWidget(self.note_today_weight_button, row, 0, 1, 2)

        row += 1
        grid.addWidget(self.reset_button, row, 1, 1, 1)

        self.show()

    def getdouble_weight(self):
        value, is_true = QInputDialog.getDouble(self, "integer input dialog", "enter a number")
        write_weight(value)

    def add_calories_button_clicked(self):
        if self.calories_blank_line.text() != '':
            arg = int(self.calories_blank_line.text())
            excel_write_test(arg)
            self.calories_blank_line.clear()
        if json_load() != 0:
            self.calories_left_label.setText("Calories left for Today: " +
                                             str(get_global("calorie_goal") - read_cell(json_load(), 2)))

    def start_day(self):
        self.calories_left_label.setText("Calories left for Today: " + str(get_global("calorie_goal")))
        write_today_date_to_excel()
        json_reset()
