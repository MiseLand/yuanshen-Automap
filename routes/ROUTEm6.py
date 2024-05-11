import tkinter as tk
from AutoMap import GamepadController, AutoMap
import time
import vgamepad

class ROUTE:
    point_names = [
         "初始化起点", "渊下宫起点","渊下第二点", "三小宝", "三机兵", "渊下终点", "层岩起点", "巨蛇—机兵",
         "巨蛇—空壳", "岩龙蜥", "层岩终点", "枫丹双球", "枫丹大宝", "枫丹跳崖",
         "枫丹役人", "沉玉第一点", "沉玉三玄文", "薄荷岛", "童梦", "鸡哥", "沙漠第一大宝", "沙漠机兵"
         , "往昔流血狗", "双丘", "须弥神像大宝", "层岩地面下", "层岩地面龙蜥", "稻妻荒海", "踏鞴沙", "天云峠终点", 
           "传奇盗宝团（还没写）","传奇龙蜥"
      ]

    def __init__(self,automap,gamepadcontroller):
         self.auto_map = automap
         self.gamepad = gamepadcontroller

    def get_point_name(self,index):
         return self.point_names[index]

    def execute_point(self, index):
         print(f"Executing: {self.point_names[index]}")
         method_name = f"case_{index + 1}"
         method = getattr(self, method_name, None)
         if method:
               method()
         else:
               print(f"No method found for index: {index}")


   
    def case_1(self):
        # 去往点位：当前点位：起点")
        # 将渊下和层岩缩到最小
        self.auto_map.open_map(1)
        self.auto_map.size_map(-1,1)

        self.auto_map.gamepad.press_button(GamepadController.B)
        time.sleep(0.02)
        self.auto_map.gamepad.release_button(GamepadController.B)

   

    def case_2(self):
        # 去往点位：点位：渊下第二点")
        self.auto_map.open_map(0.4)
        self.auto_map.move_map((0.61, 1),0.21,0.1)
        self.auto_map.pick_point()
   
   
    def case_3(self):
        # 去往点位：点位：三小宝")
        self.auto_map.open_map(0.4)
        self.auto_map.move_map((1, -0.09),0.27,0.1)
        self.auto_map.pick_point()

 
    def case_4(self):
        # 去往点位：点位：三机兵")
        self.auto_map.open_map(0.4)
        self.auto_map.move_map((1,-0.7),0.1,0.15)
        self.auto_map.pick_point()
   
 
    def case_5(self):
        # 去往点位：点位：渊下终点")
        self.auto_map.open_map(0.4)
        self.auto_map.move_map((-0.75, -1),0.17,0.2)
        self.auto_map.pick_point()
     


    def case_6(self):
       # 去往点位：点位：层岩起点")
        self.auto_map.open_map(0.4)
        self.auto_map.switch_map(1,0)

        self.auto_map.pick_point()
        time.sleep(0.02)
        self.auto_map.pick_point()
    
   
    def case_7(self):
        # 去往点位：点位：巨蛇—机兵")
        self.auto_map.open_map(0.4)
        self.auto_map.move_map((-0.1, -1),0.1)
        self.auto_map.pick_point()
        time.sleep(0.02)
        self.auto_map.pick_point()

       
       
    def case_8(self):
        # 去往点位：点位：巨蛇—空壳")
        self.auto_map.open_map(0.4)
        self.auto_map.move_map((1, -0.38),0.05)
        self.auto_map.pick_point()
        time.sleep(0.02)
        self.auto_map.pick_point()
    
     
     
    def case_9(self):
        # 去往点位：点位：岩龙蜥")
        self.auto_map.open_map(0.4)
        self.auto_map.move_map((0.27, -1),0.12)
        self.auto_map.pick_point()
        time.sleep(0.02)
        self.auto_map.pick_point()


    def case_10(self):
        # 去往点位：点位：层岩终点")
        self.auto_map.open_map(0.4)
        self.auto_map.move_map((1, -0.28),0.12)
        self.auto_map.pick_point()
        time.sleep(0.02)
        self.auto_map.pick_point()



    def case_11(self):
        # 去往点位：点位：枫丹双球")
        self.auto_map.open_map(0.4)
        self.auto_map.switch_map(0,1)
        self.gamepad.press_button(GamepadController.A)
        time.sleep(0.02)
        self.gamepad.release_button(GamepadController.A)
        time.sleep(0.6)

        self.auto_map.size_map(-1,0.35,delay = 0)

        self.auto_map.move_map((-0.91,-1),0.23,0.25)
        self.auto_map.pick_point()
        time.sleep(0.1)
      
      
      
    def case_12(self):
        # 去往点位：点位：枫丹大宝")
        self.auto_map.open_map(0.5)
        self.auto_map.move_map((0.34, -1),0.04,0.1)
        self.auto_map.pick_point()
        time.sleep(0.02)
        self.auto_map.pick_point()

  
    def case_13(self):
        # 去往点位：点位：枫丹跳崖")
        self.auto_map.open_map(0.5)
        self.auto_map.move_map((1, -0.29),0.02,0.1)
        self.auto_map.pick_point()
        time.sleep(0.02)
        self.auto_map.pick_point()    


 
    def case_14(self):
        # 去往点位：点位：枫丹役人")
        self.auto_map.open_map(0.4)
        self.auto_map.move_map((1, -0.05),0.4)
        self.auto_map.pick_point()
        time.sleep(0.02)
        self.auto_map.pick_point()    
    


    def case_15(self):
        # 去往点位：点位：沉玉第一点")
        self.auto_map.open_map(0.4)
        self.auto_map.move_map((1, -0.78),0.43)
        self.auto_map.pick_point()
        time.sleep(0.02)
        self.auto_map.pick_point()   



    def case_16(self):
        # 去往点位：点位：沉玉三玄文")
        self.auto_map.open_map(0.4)
        self.auto_map.move_map((1, -0.3),0.08)
        self.auto_map.pick_point()
        time.sleep(0.02)
        self.auto_map.pick_point()   

 
 
    def case_17(self):
        # 去往点位：点位：薄荷岛")
        self.auto_map.open_map(0.4)
        self.auto_map.move_map((1, 0.41),0.25)
        self.auto_map.pick_point()
        time.sleep(0.02)
        self.auto_map.pick_point()   


    def case_18(self):
        # 去往点位：点位：童梦")
        self.auto_map.open_map(0.4)
        self.auto_map.switch_map(0,-1)
        self.gamepad.press_button(GamepadController.A)
        time.sleep(0.02)
        self.gamepad.release_button(GamepadController.A)
        time.sleep(0.4)# 开须弥地图延时

        self.auto_map.move_map((-0.96,-1),0.16,0.1)
        self.auto_map.pick_point()
        time.sleep(0.1)



    def case_19(self):
        # 去往点位：点位：鸡哥")
        self.auto_map.open_map(0.4)
        self.auto_map.move_map((-1, 0.92),0.17)
        self.auto_map.pick_point()
        time.sleep(0.02)
        self.auto_map.pick_point()   


    def case_20(self):
        # 去往点位：点位：沙漠第一大宝")
        self.auto_map.open_map(0.4)
        self.auto_map.move_map((-1, 0.03),0.41)
        self.auto_map.pick_point()
        time.sleep(0.02)
        self.auto_map.pick_point()  


    def case_21(self):
        # 去往点位：点位：沙漠机兵")
        
        self.auto_map.open_map(0.4)
        self.auto_map.move_map((0.26, -1),0.08)
        self.auto_map.pick_point()
        time.sleep(0.02)
        self.auto_map.pick_point()  


    def case_22(self):
        # 去往点位：点位：往昔流血狗")
        self.auto_map.open_map(0.4)
        self.auto_map.move_map((1, -0.14),0.35)
        self.auto_map.pick_point()
        time.sleep(0.02)
        self.auto_map.pick_point()  


    def case_23(self):
        # 去往点位：点位：双丘")
        self.auto_map.open_map(0.4)
        self.auto_map.move_map((0.28, -1),0.39)
        self.auto_map.pick_point()
        time.sleep(0.02)
        self.auto_map.pick_point()  


    def case_24(self):
        # 去往点位：点位：须弥神像大宝")
        self.auto_map.open_map(0.4)
        self.auto_map.move_map((1, 0.58),0.31)
        self.auto_map.pick_point()
        time.sleep(0.02)
        self.auto_map.pick_point()  


    def case_25(self):
        # 去往点位：点位：层岩地面下")
        self.auto_map.open_map(0.4)
        self.auto_map.move_map((1, 0.63),0.24)
        self.auto_map.pick_point()
        time.sleep(0.02)
        self.auto_map.pick_point()  


    def case_26(self):
       # 去往点位：点位：层岩地面龙蜥")
        self.auto_map.open_map(0.4)
        self.auto_map.move_map((0.48, 1),0.06)
        self.auto_map.pick_point()
        time.sleep(0.02)
        self.auto_map.pick_point()  


    def case_27(self):
        # 去往点位：点位：稻妻荒海")
        self.auto_map.open_map(0.4)
        self.auto_map.switch_map(-1,-1)
        self.gamepad.press_button(GamepadController.A)
        time.sleep(0.02)
        self.gamepad.release_button(GamepadController.A)
        time.sleep(0.3)# 开稻妻地图延时

        self.auto_map.move_map((-0.27,1),0.24,0.1)
        self.auto_map.pick_point()
        time.sleep(0.1)


    def case_28(self):
        # 去往点位：点位：踏鞴沙")
        self.auto_map.open_map(0.4)
        self.auto_map.switch_map(0,0)
        self.gamepad.press_button(GamepadController.A)
        time.sleep(0.02)
        self.gamepad.release_button(GamepadController.A)
        time.sleep(0.3)# 稻妻地图回正延时

        self.auto_map.move_map((-1,-0.64),0.43,0.1)
        self.auto_map.pick_point()
        time.sleep(0.1)
        self.auto_map.pick_point()

  
  
    def case_29(self):
        # 去往点位：点位：天云峠终点")
        self.auto_map.open_map(0.4)
        self.auto_map.move_map((1,-0.72),0.44,0.1)
        self.auto_map.pick_point()
        time.sleep(0.02)
        self.auto_map.pick_point()  


    def case_30(self):
        # 去往点位：点位：传奇盗宝团")
        self.auto_map.open_map(0.4)
        self.auto_map.switch_map(0,-1)
        self.gamepad.press_button(GamepadController.A)
        time.sleep(0.02)
        self.gamepad.release_button(GamepadController.A)
        time.sleep(0.3)# 开枫丹地图延时

        self.auto_map.move_map((1,0.05),0.51,0.1)
        self.auto_map.pick_point()
        time.sleep(0.02)
        self.auto_map.pick_point()  

    def case_31(self):
        # 去往点位：点位：传奇龙蜥")
        self.auto_map.open_map(0.4)
        self.auto_map.move_map((0.51,-1),0.74)
        self.auto_map.pick_point()
        time.sleep(0.02)
        self.auto_map.pick_point()  



# 如果这个文件被当作主脚本运行，执行以下代码
if __name__ == "__main__":
    route = ROUTE()
    route.execute_point(0)
# 可以在这个文件中定义其他需要的功能或工具函数


    
    

