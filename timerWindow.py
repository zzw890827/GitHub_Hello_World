# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, QTimer


class TimerWindow(QWidget):
    before_close_signal = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.sec = 0
        self.setWindowTitle('倒计时')
        self.resize(200, 150)

        self.lcd = QLCDNumber(18, self)
        btn_1 = QPushButton(self, text='Test')
        btn_2 = QPushButton(self, text='Close')

        layout = QVBoxLayout(self)
        layout.addWidget(self.lcd)
        layout.addWidget(btn_1)
        layout.addWidget(btn_2)

        self.timer = QTimer()
        self.timer.timeout.connect(self._update)
        btn_1.clicked.connect(self.start_timer)
        btn_2.clicked.connect(self.stop_timer)

    def _update(self):
        self.sec += 1
        self.lcd.display(self.sec)

    def start_timer(self):
        self.timer.start(1000)

    def stop_timer(self):
        self.timer.stop()
        self.sec = 0
        self.before_close_signal.emit(self.lcd.value())
        self.close()

    def close_dialog(self):
        self.stop_timer()
