from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QPushButton, QLabel, QLineEdit
from globals import get_global, update_global
from excel import excel_write_test, read_cell, write_today_date_to_excel

calorie_goal = 1600


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

        self.reset_button = QPushButton("Start of the day")
        self.reset_button.clicked.connect(self.start_day)

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
        if self.calories_blank_line.text() != '':
            arg = int(self.calories_blank_line.text())
            excel_write_test(arg)
            self.calories_blank_line.clear()
        if get_global("target_row") != 0:
            self.calories_left_label.setText("Calories left for Today: " +
                                             str(calorie_goal - read_cell(get_global("target_row"), 2)))

    def start_day(self):
        self.calories_left_label.setText("Calories left for Today: " + str(calorie_goal))
        write_today_date_to_excel()
        update_global("target_row", 0)
