import sys
import json
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from FlashTraderGui import FlashTraderMain

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Platform of main window
    mainWindow = FlashTraderMain()
    mainWindow.show()

    sys.exit(app.exec_())