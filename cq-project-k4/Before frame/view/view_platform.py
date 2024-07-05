#Before frame/view/view_platform.py
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from PyQt5.QtWidgets import QWidget
from OCC.Display.backend import load_backend

#from .Gear_set.gear import GearCreator  # 导入齿轮功能以连接信号

# 设置 pythonOCC 使用的后端为 QtBefore frame/view/view_platform.py
load_backend("qt-pyqt5")
import OCC.Display.qtDisplay as qtDisplay


class ThreeDViewWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.initUI()


    def initUI(self):
        self.canvas = qtDisplay.qtViewer3d(self)
        self.canvas.setFixedSize(1200, 600)  # 设置部件的固定大小为 1000x600 像素
        self.canvas.InitDriver()


        background_gradient_color1 = [206, 215, 226]
        background_gradient_color2 = [128, 128, 128]
        self.canvas._display.set_bg_gradient_color(background_gradient_color1, background_gradient_color2)

        self.display = self.canvas._display
        self.display.display_triedron()


 # 示例：显示一个立方体
        self.display_box()

    def display_box(self):
        box = BRepPrimAPI_MakeBox(100.0, 100.0, 100.0).Shape()
        ais_box = self.display.DisplayShape(box)
        self.display.FitAll()


    def display_shape(self, shape):
        """显示传递进来的几何体"""
        self.display.DisplayShape(shape, update=True)
        self.display.FitAll()

