from OCC.Display.SimpleGui import init_display
from traits.api import Float, Int, Button, HasTraits
from traitsui.api import View, Item, HGroup, VGroup, Group
from . import pygear  # 使用相对导入

from PyQt5.QtWidgets import QApplication
import sys
from ..view_platform import ThreeDViewWidget  # 确保 view_platform 可以正确导入


class GearCreator(HasTraits):
    m_n = Float(10.0, label='模数')
    z = Int(11, label='齿数')
    beta = Float(0.0, label='螺旋角')
    x = Float(0.35, label='变位系数')
    alpha_n = Float(20.0, label='法向压力角')
    b = Float(180.0, label='齿宽')
    d_s = Float(20.0, label='轴孔直径')
    create_gear = Button('创建齿轮')

    def _create_gear_fired(self):
        gear_data = {
            'm_n': self.m_n,
            'z': self.z,
            'beta': self.beta,
            'x': self.x,
            'alpha_n': self.alpha_n,
            'b': self.b,
            'd_s': self.d_s,
        }

        extgear_2 = {'m_n': 10.0, 'z': 11, 'beta': 0, 'x': 0.35, 'alpha_n': 20.0, 'b': 180, 'd_s': 20.0}
        geardata = gear_data  # 在这里选择齿轮数据
        mygear = pygear.CylindricalGearWheel(geardata)  # 创建圆柱齿轮实例
        mygear_solid = mygear.makeOCCSolid()  # 创建齿轮的 OCC 3D 实体


        #pygear.writeOCCShape(mygear_solid, 'extgear_1.stp', 'step')
        self.display, self.start_display, self.add_menu, self.add_function_to_menu = init_display()
        self.display.DisplayShape(mygear_solid, update=False)
        self.start_display()



    traits_view = View(Group(
        VGroup(
            VGroup(
                Item('m_n'),
                Item('z'),
                Item('beta'),
                Item('x'),
                Item('alpha_n'),
                Item('b'),
                Item('d_s'),
                show_border=True,
                label='齿轮参数'
            ),
            HGroup(
                Item('create_gear', show_label=False),
                show_border=True,
                label='操作'
            ),
        ),
        style_sheet='*{font-size:25px}'),
        resizable=True,
        title='齿轮生成器',
    )
def show_gear_creator_dialog(self):
    gc = GearCreator()
    gc.configure_traits()
