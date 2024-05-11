import pygame
import vgamepad

class GameController:
    def __init__(self):
        pygame.init()
        pygame.joystick.init()
        self.joystick = None
        if pygame.joystick.get_count() > 0:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
            print("has_inited_joystick")

    def read_buttons(self):
        pygame.event.pump()
        button_states = {}
        for i in range(self.joystick.get_numbuttons()):
            button_states[i] = self.joystick.get_button(i)
        return button_states

    def read_axes(self):
        pygame.event.pump()
        axes = {}
        for i in range(self.joystick.get_numaxes()):
            axes[i] = self.joystick.get_axis(i)
        return axes

    def read_hat(self):
        pygame.event.pump()
        return self.joystick.get_hat(0)

    def get_events(self):
        pygame.event.pump()
        return pygame.event.get(), pygame.time.get_ticks()

    def check_button_press(self, button_id):
        events, _ = self.get_events()
        for event in events:
            if event.type == pygame.JOYBUTTONDOWN and event.button == button_id:
                return True
        return False

    def check_axis_motion(self, axis_id, threshold=0.5):
        axis_value = self.read_axes().get(axis_id, 0)
        return abs(axis_value) > threshold

    def update(self):
        """可以在这里添加更多与游戏控制器状态相关的复杂逻辑"""
        pass