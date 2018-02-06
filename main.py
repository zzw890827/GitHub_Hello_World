# -*- coding: utf-8 -*-
import sys

from view import View
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = View()
    ui.show()
    sys.exit(app.exec_())
