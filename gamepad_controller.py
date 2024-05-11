import vgamepad

class GamepadController:
    # 按键定义
    UP = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP
    DOWN = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN
    LEFT = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT
    RIGHT = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT

    START = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_START
    BACK = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_BACK
    GUIDE = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_GUIDE

    LEFT_THUMB = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB
    RIGHT_THUMB = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB
    LEFT_SHOULDER = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER
    RIGHT_SHOULDER = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER

    A = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_A
    B = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_B
    X = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_X
    Y = vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_Y

    def __init__(self):
        self.gamepad = vgamepad.VX360Gamepad()

    def left_trigger(self, value):
        self.gamepad.left_trigger_float(value)
        self.gamepad.update()

    def right_trigger(self, value):
        self.gamepad.right_trigger_float(value)
        self.gamepad.update()

    def left_joystick(self, x_value, y_value):
        self.gamepad.left_joystick_float(x_value, y_value)
        self.gamepad.update()

    def right_joystick(self, x_value, y_value):
        self.gamepad.right_joystick_float(x_value, y_value)
        self.gamepad.update()

    def press_button(self, button):
        self.gamepad.press_button(button)
        self.gamepad.update()

    def release_button(self, button):
        self.gamepad.release_button(button)
        self.gamepad.update()