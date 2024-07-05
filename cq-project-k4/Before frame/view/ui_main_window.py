from PyQt5 import QtCore, QtWidgets
from .view_platform import ThreeDViewWidget
from .toolbars import ProjectToolbar, ModelingToolbar, AnalysisToolbar, ViewToolbar, HelpToolbar
from .menu_buttons import MenuButtons
from .Gear_set.gear import show_gear_creator_dialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        # 创建空白菜单栏
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1500, 35))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        # 在菜单栏中添加一个空白菜单
        self.menu_blank = QtWidgets.QMenu(" ")
        self.menubar.addMenu(self.menu_blank)

        # 创建菜单按钮
        self.menu_buttons = MenuButtons(self.menubar)
        self.menu_buttons.setup_menu_buttons()

        # 创建并添加工具栏
        self.toolbars = {
            'project': ProjectToolbar(MainWindow),
            'modeling': ModelingToolbar(MainWindow),
            'analysis': AnalysisToolbar(MainWindow),
            'view': ViewToolbar(MainWindow),
            'help': HelpToolbar(MainWindow)
        }
        for toolbar in self.toolbars.values():
            MainWindow.addToolBar(toolbar)
            toolbar.hide()

        # 默认显示“项目”工具栏
        self.toolbars['project'].show()

        # 连接菜单按钮的点击信号到switch_toolbar方法
        self.menu_buttons.button_file.clicked.connect(lambda: self.switch_toolbar('project'))
        self.menu_buttons.button_edit.clicked.connect(lambda: self.switch_toolbar('modeling'))
        self.menu_buttons.button_caculate.clicked.connect(lambda: self.switch_toolbar('analysis'))
        self.menu_buttons.button_window.clicked.connect(lambda: self.switch_toolbar('view'))
        self.menu_buttons.button_help.clicked.connect(lambda: self.switch_toolbar('help'))

        # 连接齿轮按钮的双击信号到齿轮功能
        self.toolbars['modeling'].action_gear.triggered.connect(show_gear_creator_dialog)

        # 创建内部窗口并设置位置和大小
        self.inner_window = QtWidgets.QWidget(parent=self.centralwidget)
        self.inner_window.setGeometry(QtCore.QRect(2, 5, 250, 400))
        self.inner_window.setObjectName("inner_window")
        self.inner_window.hide()  # 默认隐藏内部窗口

        # 创建一个标签作为内部窗口的标题
        self.inner_label = QtWidgets.QLabel("零件装配目录：", parent=self.inner_window)
        self.inner_label.setObjectName("inner_label")
        self.inner_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        # 连接按钮的点击信号到槽方法，新建按钮所链接
        self.toolbars['project'].action_new.triggered.connect(self.toggle_inner_window)

        # 添加 3D 视图部件
        self.three_d_view_widget = ThreeDViewWidget(self.centralwidget)
        self.three_d_view_widget.setGeometry(QtCore.QRect(253, 5, 1200, 600))
        self.three_d_view_widget.hide()  # 默认隐藏内部窗口

        self.retranslateUi(MainWindow)

    def toggle_inner_window(self):
        if self.inner_window.isVisible():
            self.inner_window.hide()
            self.three_d_view_widget.hide()  # 默认隐藏内部窗口
        else:
            self.inner_window.show()
            self.three_d_view_widget.show()  # 默认隐藏内部窗口

    def switch_toolbar(self, toolbar_name):
        # 隐藏所有工具栏
        for toolbar in self.toolbars.values():
            toolbar.hide()

        # 显示触发的工具栏
        if toolbar_name in self.toolbars:
            self.toolbars[toolbar_name].show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
