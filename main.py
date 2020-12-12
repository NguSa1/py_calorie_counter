import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from gui import CalorieTrackerGUI
from excel import excel_exist
b = 0


def main():

    excel_exist()
    app = QApplication([])
    gui = CalorieTrackerGUI()
    sys.exit(app.exec_())


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(error)
