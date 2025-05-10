import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow
from logic import VotingApp

class MainApp(QMainWindow):
    '''main app window that loads the gui and connects logic'''
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(440, 320)

        #connectlogic
        self.logic = VotingApp(self.ui)
        self.ui.messageLabel.setText("ready to vote!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
