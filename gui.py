from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QPushButton, QLabel, QLineEdit, QInputDialog
from openpyxl import load_workbook

from globals import get_global
from excel import read_cell, write_today_date_to_excel, write_weight, check_today_row, excel_write
from json_writer import json_load


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

        if read_cell(json_load(), 2) is not None:
            self.calories_left_label = QLabel("Calories left for Today: " +
                                              str(get_global("calorie_goal") - read_cell(json_load(), 2)))
        else:
            self.calories_left_label = QLabel("Calories left for Today: " +
                                              str(get_global("calorie_goal")))

        reset_button = QPushButton("Start of the day")
        reset_button.clicked.connect(self.start_day)

        note_today_weight_button = QPushButton("Enter today's weight")
        note_today_weight_button.clicked.connect(self.get_weight)

        # grid; button placement
        row = 0
        grid.addWidget(QLabel("Calorie Goal: " + str(get_global("calorie_goal"))), row, 0, 1, 1)

        row += 1
        grid.addWidget(self.calories_blank_line, row, 0, 1, 1)
        grid.addWidget(add_calories_button, row, 1, 1, 1)

        row += 1
        grid.addWidget(self.calories_left_label, row, 0, 1, 1)

        row += 1
        grid.addWidget(note_today_weight_button, row, 0, 1, 2)

        row += 1
        grid.addWidget(reset_button, row, 1, 1, 1)

        self.show()

    def get_weight(self):
        value, is_true = QInputDialog.getDouble(self, "integer input dialog", "enter a number")
        write_weight(value)

    def add_calories_button_clicked(self):
        if self.calories_blank_line.text() != '':
            calories_add = int(self.calories_blank_line.text())
            excel_write(calories_add)
            self.calories_blank_line.clear()
        if json_load() != 0:
            self.calories_left_label.setText("Calories left for Today: " +
                                             str(get_global("calorie_goal") - read_cell(json_load(), 2)))

    def start_day(self):
        # write_today_date_to_excel()
        if write_today_date_to_excel():
            self.calories_left_label.setText("Calories left for Today: " + str(get_global("calorie_goal")))

        # json_reset()
        book = load_workbook("diet_diary.xlsx")
        sheet = book.active
        a = 2
        check_today_row(sheet, a)
