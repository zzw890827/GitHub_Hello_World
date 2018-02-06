# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from dialog import Ui_DialogWindow
from timerWindow import TimerWindow


class View(QtWidgets.QMainWindow, Ui_DialogWindow):
    def __init__(self):
        super(View, self).__init__()
        self.setupUi(self)
        self.title = QtCore.QCoreApplication.translate('Input Dialog', 'Input Dialog')
        self.input_int.clicked.connect(self.btn_clicked_input_int)
        self.input_float.clicked.connect(self.btn_clicked_input_float)
        self.input_txt.clicked.connect(self.btn_clicked_input_txt)
        self.input_article.clicked.connect(self.btn_clicked_input_article)
        self.input_option.clicked.connect(self.btn_clicked_input_option)
        self.msg_info.clicked.connect(self.btn_clicked_msg_info)
        self.msg_qa.clicked.connect(self.btn_clicked_msg_qa)
        self.msg_warning.clicked.connect(self.btn_clicked_msg_warning)
        self.msg_dangerous.clicked.connect(self.btn_clicked_msg_dangerous)
        self.msg_about.clicked.connect(self.btn_clicked_msg_about)
        self.file_folder.clicked.connect(self.btn_clicked_file_folder)
        self.file_file.clicked.connect(self.btn_clicked_file_file)
        self.file_files.clicked.connect(self.btn_clicked_file_files)
        self.file_save.clicked.connect(self.btn_clicked_save)
        self.file_other.clicked.connect(self.btn_clicked_save)
        self.color.clicked.connect(self.btn_clicked_color)
        self.font.clicked.connect(self.btn_clicked_font)
        self.customize.clicked.connect(self.btn_clicked_customize)
        self.timer_window = TimerWindow()

    def btn_clicked_input_int(self):
        value, ok = QInputDialog.getInt(self, self.title, 'Input one integer number: ', 37, -10000, 10000, 2)
        print(value, ok)

    def btn_clicked_input_float(self):
        value, ok = QInputDialog.getDouble(self, self.title, 'Input one double number: ', 37.56, -100, 100, 2)
        print(value, ok)

    def btn_clicked_input_txt(self):
        value, ok = QInputDialog.getText(self, self.title, 'Input one word', QLineEdit.Normal, 'QianBaoBao')
        print(value, ok)

    def btn_clicked_input_article(self):
        value, ok = QInputDialog.getMultiLineText(self, self.title, 'Input a sentence', '骞宝宝:\n我超爱你！')
        print(value, ok)

    def btn_clicked_input_option(self):
        items = ['Spring', 'Summer', 'Fall', 'Winter']
        value, ok = QInputDialog.getItem(self, self.title, 'Select one season: ', items, 1, False)
        print(value, ok)

    def btn_clicked_msg_info(self):
        msg = QMessageBox.information(self, self.title, '骞宝宝:\n我超爱你！', QMessageBox.Yes | QMessageBox.No)
        print(msg)

    def btn_clicked_msg_qa(self):
        msg = QMessageBox.question(self, self.title, '我爱骞宝宝吗？', QMessageBox.Yes | QMessageBox.No)
        print(msg)

    def btn_clicked_msg_warning(self):
        msg = QMessageBox.warning(self, self.title, '不爱骞宝宝是要被杀掉的哦！', QMessageBox.Yes | QMessageBox.No)
        print(msg)

    def btn_clicked_msg_dangerous(self):
        msg = QMessageBox.critical(self, self.title, '受死吧！！！！！！！', QMessageBox.Yes | QMessageBox.No)
        print(msg)

    def btn_clicked_msg_about(self):
        QMessageBox.about(self, self.title, '由于没有爱骞宝宝\n此人已死，有事烧纸')

    def btn_clicked_file_folder(self):
        _dir = QFileDialog.getExistingDirectory(self, '选取文件夹', 'C:/')
        print(_dir)

    def btn_clicked_file_file(self):
        _file, _type = QFileDialog.getOpenFileName(self, '选取文件夹', 'E:/', 'csv Files (*.csv)')
        print(_file, _type)

    def btn_clicked_file_files(self):
        files, ok = QFileDialog.getOpenFileNames(self, '多文件选择', 'E:/', 'csv Files (*.csv)')
        print(files, ok)

    def btn_clicked_save(self):
        _file, ok = QFileDialog.getSaveFileName(self, '文件保存', 'E:/', 'Text Files (*.txt)')
        print(_file, ok)

    def btn_clicked_color(self):
        color = QColorDialog.getColor(Qt.green, self, '选择颜色')
        print(color.getRgb())

    @staticmethod
    def btn_clicked_font():
        font, ok = QFontDialog.getFont()
        print(font, ok)

    def btn_clicked_customize(self):
        self.timer_window.show()
