from PyQt5 import QtWidgets, QtCore

class MenuButtons:
    def __init__(self, menubar):
        self.menubar = menubar

    def setup_menu_buttons(self):
        self.button_file = QtWidgets.QPushButton("项目", parent=self.menubar)
        self.button_file.setGeometry(QtCore.QRect(5, 0, 60, 28))

        self.button_edit = QtWidgets.QPushButton("建模", parent=self.menubar)
        self.button_edit.setGeometry(QtCore.QRect(68, 0, 60, 28))

        self.button_caculate = QtWidgets.QPushButton("计算分析", parent=self.menubar)
        self.button_caculate.setGeometry(QtCore.QRect(145, 0, 60, 28))

        self.button_window = QtWidgets.QPushButton("视图", parent=self.menubar)
        self.button_window.setGeometry(QtCore.QRect(218, 0, 60, 28))

        self.button_help = QtWidgets.QPushButton("帮助", parent=self.menubar)
        self.button_help.setGeometry(QtCore.QRect(285, 0, 60, 28))
