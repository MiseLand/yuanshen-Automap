import tkinter as tk
from game_controller import GameController
from game_gui import GameGUI
import importlib
import sys
from AutoMap import AutoMap
from gamepad_controller import GamepadController
import pygame

def load_route_module(module_name, mapcontroller, gamepadcontroller):
    """动态加载指定的路线模块并创建ROUTE实例"""
    if module_name in sys.modules:
        importlib.reload(sys.modules[module_name])
    else:
        sys.modules[module_name] = importlib.import_module(module_name)
    return sys.modules[module_name].ROUTE(mapcontroller, gamepadcontroller)

def main():
    # 初始化 Pygame
    pygame.init()
    pygame.joystick.init()

    # 创建 GameController 实例 检测手柄输入
    controller = GameController()

    # 创建 GamepadController 实例 控制虚拟手柄输出
    gamepadcontroller = GamepadController()

    # 创建 AutoMap 实例
    mapcontroller = AutoMap(gamepadcontroller)

    # 创建 GUI 实例，传递 GameController 和一个函数用于加载路线
    gui = GameGUI(controller, lambda module_name: load_route_module(module_name, mapcontroller, gamepadcontroller))

    # 启动 GUI
    gui.start()
    
    input("按 Enter 键退出程序...")

if __name__ == "__main__":
    main()



