import tkinter as tk
from AutoMap import GamepadController, AutoMap
import time
import vgamepad

class ROUTE:
   point_names = [
         "初始化起点", "镀金驮起点", "护士森神像", "须弥城湖边", "五绿洲", "三运河上", "三运河副本",
         "三运河下", "折胫谷", "愚妄行宫左", "愚妄行宫", "圣显厅", "神的棋盘上",
         "千柱的花园", "铄石之丘", "丰饶绿洲", "双丘", "终点—禅那园神像", "空置"
      ]

   def __init__(self, automap, gamepadcontroller):
        self.auto_map = automap
        self.gamepad = gamepadcontroller  # Ensure this is an instance of GamepadController

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
      # 去往点位：点位：镀金驮起点")
      # 地图缩到最小
      self.auto_map.open_map(1)
      self.auto_map.size_map(-1,1)

      self.auto_map.gamepad.press_button(GamepadController.B)
      time.sleep(0.02)
      self.auto_map.gamepad.release_button(GamepadController.B)

   
   def case_2(self):
      # 去往点位：点位：护士森神像")
      self.auto_map.open_map(0.5)
      self.auto_map.move_map((-0.22, 1),delay=0.02)
      self.auto_map.size_map(1,0.33,delay = 0)
      self.auto_map.move_map((0, 0),0,delay=0.05)
      self.auto_map.pick_point()

   
   def case_3(self):
      # 去往点位：点位：须弥城湖边")
      self.auto_map.open_map(0.5)
      self.auto_map.move_map((-1, -0.16),0.28,0.05)
      self.auto_map.pick_point()
      
    
   def case_4(self):
      # 去往点位：点位：五绿洲")
      self.auto_map.open_map(0.5)
      self.auto_map.move_map((-1,0.15),0.58,0.05)
      self.auto_map.pick_point()
      

    
   def case_5(self):
      # 去往点位：点位：三运河上")
      self.auto_map.open_map(0.5)
      self.auto_map.move_map((-1,-0.34),0.1,0.05)
      self.auto_map.pick_point()
      

   
   def case_6(self):
      # 去往点位：点位：三运河副本")
      
      self.auto_map.open_map(0.5)
      self.auto_map.move_map((1,-0.87),0.1,0.05)
      self.auto_map.pick_point()
      
    
   def case_7(self):
      # 去往点位：点位：三运河下")
      
      self.auto_map.open_map(0.5)
      self.auto_map.move_map((-0.78,-1),0.06,0.05)
      self.auto_map.pick_point()
     
   @staticmethod
   def case_8(self):
      # 去往点位：点位：折胫谷")
      self.auto_map.open_map(0.5)  
      self.auto_map.move_map((-0.47, 1),0.05,0.05)      
      self.auto_map.pick_point()
   

    
   def case_9(self):
      # 去往点位：点位：愚妄行宫左")
      
      self.auto_map.open_map(0.5)
      self.auto_map.move_map((1, -0.06),0.28,0.05)   
      self.auto_map.pick_point()
      

    
   def case_10(self):
      # 去往点位：点位：愚妄行宫")
      
      self.auto_map.open_map(0.5)
      self.auto_map.move_map((1, 0.5),0.15,0.05)   
      self.auto_map.pick_point()

   
   def case_11(self):
      # 去往点位：点位：圣显厅")
            
      self.auto_map.open_map(0.5)
      self.auto_map.move_map((-0.55, -1),0.18,0.05)  
      self.auto_map.pick_point()
      

   
   def case_12(self):
      # 去往点位：点位：神的棋盘上")
            
      self.auto_map.open_map(0.5)
      self.auto_map.move_map((-1, 0.31),0.2,0.05)  
      self.auto_map.pick_point()
      
     
   def case_13(self):
      # 去往点位：点位：千柱的花园")
            
      
      self.auto_map.open_map(0.5)
      self.auto_map.move_map((-0.28, -1),0.08,0.05)  
           
      self.auto_map.pick_point()
      self.time.sleep(0.05)
      self.auto_map.pick_point()
      
    
   def case_14(self):
      # 去往点位：点位：铄石之丘")
         
      self.auto_map.open_map(0.5)
      self.auto_map.move_map((-0.15, -1),0.33,0.05)  
      self.auto_map.pick_point()
      

    
   def case_15(self):
      # 去往点位：点位：丰饶绿洲")
      
      
      self.auto_map.open_map(0.5)
      self.auto_map.move_map((1, 0.41),0.33,0.05)  
      self.auto_map.pick_point()
    
 
   def case_16(self):
      # 去往点位：双丘"
         
      self.auto_map.open_map(0.5)
      self.auto_map.move_map((1, 0.41),0.45,0.05)  
      self.auto_map.pick_point()
     

    
   def case_17(self):
      # "去往：终点—禅那园神像"
      
      self.auto_map.open_map(0.5)
      self.auto_map.move_map((0.015,1),0.28,0.05)  
     
      self.auto_map.pick_point()
      self.auto_map.pick_point()

    
   def case_18(self):
      self.output_label.config(text="当前点位：空置")


# 如果这个文件被当作主脚本运行，执行以下代码
if __name__ == "__main__":
   route = ROUTE()
   route.execute_point(0)
# 可以在这个文件中定义其他需要的功能或工具函数
