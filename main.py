"""Module: main"""

import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import HexEditor

def main():
    app = QApplication(sys.argv)
    editor = HexEditor()
    editor.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

