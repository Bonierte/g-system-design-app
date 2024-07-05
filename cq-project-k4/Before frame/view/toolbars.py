from PyQt5 import QtWidgets

class ProjectToolbar(QtWidgets.QToolBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(60)
        self.setup_toolbar()

    def setup_toolbar(self):
        self.action_new = self.addAction('新建')
        self.action_open = self.addAction('打开')
        self.action_save = self.addAction('保存')
        self.action_save_as = self.addAction('另存为')

class ModelingToolbar(QtWidgets.QToolBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(60)
        self.setup_toolbar()

    def setup_toolbar(self):
        self.action_axle = self.addAction('轴')
        self.action_gear = self.addAction('齿轮')
        self.action_gearing = self.addAction('齿圈')
        self.action_box = self.addAction('箱体')

class AnalysisToolbar(QtWidgets.QToolBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(60)
        self.setup_toolbar()

    def setup_toolbar(self):
        self.action_efficiency = self.addAction('传递效率')
        self.action_contact = self.addAction('接触应力')
        self.action_curve = self.addAction('弯曲应力')
        self.action_life = self.addAction('寿命预估')

class ViewToolbar(QtWidgets.QToolBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(60)
        self.setup_toolbar()

    def setup_toolbar(self):
        # 设置视图工具栏的按钮和逻辑
        pass

class HelpToolbar(QtWidgets.QToolBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(60)
        self.setup_toolbar()

    def setup_toolbar(self):
        # 设置帮助工具栏的按钮和逻辑
        pass
