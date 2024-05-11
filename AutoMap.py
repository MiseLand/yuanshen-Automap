import vgamepad
import time
from gamepad_controller import GamepadController

class AutoMap:
    def __init__(self):
        self.gamepad = GamepadController()

    def __init__(self, gamepadcontroller):
        self.gamepad = gamepadcontroller

    def open_map(self, delay=0.4):
        self.gamepad.press_button(GamepadController.LEFT_SHOULDER)
        self.gamepad.right_joystick(0, -1)
        time.sleep(0.3)
        self.gamepad.right_joystick(0, 0)
        time.sleep(delay)
        self.gamepad.release_button(GamepadController.LEFT_SHOULDER)
        

    def pick_point(self):
        self.gamepad.press_button(GamepadController.A)
        time.sleep(0.02)
        self.gamepad.release_button(GamepadController.A)
        time.sleep(0.1)
        self.gamepad.press_button(GamepadController.A)
        time.sleep(0.02)
        self.gamepad.release_button(GamepadController.A)
        

    def quick_T(self):
        self.gamepad.press_button(GamepadController.LEFT_SHOULDER)
        time.sleep(0.1)
        self.gamepad.press_button(GamepadController.X)
        time.sleep(0.02)
        self.gamepad.release_button(GamepadController.X)
        time.sleep(0.02)

    def switch_map(self, x = 0, y = 0):
        # 切换地图的操作
        self.gamepad.press_button(GamepadController.Y)
        time.sleep(0.02)
        self.gamepad.release_button(GamepadController.Y)
        ynum = abs(y)
        if(y>0):
            dir_y = 1
        elif(y<0):
            dir_y = -1
        for i in range(ynum):
            self.gamepad.left_joystick(0, dir_y)
            time.sleep(0.02)
            self.gamepad.left_joystick(0, 0)
            time.sleep(0.1)

        xnum = abs(x)
        if(x>0):
            dir_x = 1
        elif(x<0):
            dir_x = -1
        for j in range(xnum):
            self.gamepad.left_joystick(dir_x,0)
            time.sleep(0.02)
            self.gamepad.left_joystick(0, 0)
            time.sleep(0.1)

        return
    
    def move_map(self, axis = (0,0), span = -1, delay = 0):
        # 移动地图的操作
        self.gamepad.left_joystick(axis[0], axis[1])
        if(span >= 0):
            time.sleep(span)
            self.gamepad.left_joystick(0, 0)

        time.sleep(delay)
        return
    
    def size_map(self, triger = 0, span = -1, delay = 0): 

        if(triger > 0):
            self.gamepad.left_trigger(triger)
            self.gamepad.right_trigger(0)
        elif(triger < 0):
            self.gamepad.right_trigger(-triger)
            self.gamepad.left_trigger(0)
        else:
            self.gamepad.left_trigger(0)
            self.gamepad.right_trigger(0)
        if(span >= 0):
            time.sleep(span)
            self.gamepad.right_trigger(0)
            self.gamepad.left_trigger(0)

        time.sleep(delay)

        return
    
    