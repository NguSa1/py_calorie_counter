import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from gui import CalorieTrackerGUI


def main():
    # run_tmtc_client(False)
    app = QApplication([])
    gui = CalorieTrackerGUI()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

