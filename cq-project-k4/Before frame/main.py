#Before frame/main.py
import sys
from PyQt5 import QtWidgets
from view.ui_main_window import Ui_MainWindow
from view.utils import load_stylesheet


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # 加载并应用样式表
    menu_stylesheet = load_stylesheet("view/style_qss/meau_style.qss")
    toolbar_stylesheet = load_stylesheet("view/style_qss/toolbars.qss")
    app.setStyleSheet(menu_stylesheet + toolbar_stylesheet)


    MainWindow.show()
    sys.exit(app.exec())