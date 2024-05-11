import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import pygame
from importlib import reload, import_module
import os

import sys
routes_path = os.path.join(os.getcwd(), 'routes')
if routes_path not in sys.path:
    sys.path.append(routes_path)

class GameGUI:
    def __init__(self, controller, load_module_func):
        self.controller = controller
        self.window = tk.Tk()
        self.window.title("Route Navigator")
        self.window.geometry("400x300")
        self.current_number = 0
        self.load_module_func = load_module_func
        self.module = 'ROUTEm6'  # 默认模块
        self.route = self.load_module_func(self.module)  # 使用函数加载模块
        
        self.base_route_path = os.path.join(os.getcwd(), 'routes')
          # 确保route文件夹存在
        if not os.path.exists(self.base_route_path):
            os.makedirs(self.base_route_path)
        self.editor_window = None  # 用于存储编辑器窗口的引用
        self.current_file = None  # 当前打开的文件路径

        # 动态获取模块列表
        self.modules = self.scan_route_modules()
        if not self.modules:  # 如果没有找到任何模块，添加一个占位符
            self.modules.append("No modules found")

        # 下拉菜单以选择不同的路线模块
        self.module_var = tk.StringVar(self.window)
        self.module_var.set(self.modules[0])  # 设置初始模块为列表中的第一个模块
        self.module_menu = tk.OptionMenu(self.window, self.module_var, *self.modules, command=self.on_module_change)
        self.module_menu.pack(pady=10)

        self.label = tk.Label(self.window, text=f"Selected Number: {self.current_number}")
        self.label.pack(pady=10)
        self.output_label = tk.Label(self.window, text="点位")
        self.output_label.pack(pady=10)
        self.program_paused = False
        self.status_label = tk.Label(self.window, text="程序状态：运行中")
        self.status_label.pack(pady=20)
        self.left_thumb_press_count = 0
        self.last_thumb_press_time = 0
        self.window.after(100, self.check_joystick)

        # 添加编辑按钮
        edit_button = tk.Button(self.window, text="Edit Routes", command=self.open_editor)
        edit_button.pack(pady=10)  # 确保使用.pack()将按钮添加到窗口


    def open_editor(self):
        """打开一个新窗口来编辑route文件"""
        if self.editor_window:
            self.editor_window.destroy()

        self.editor_window = tk.Toplevel(self.window)
        self.editor_window.title("Route Editor")
        self.editor_window.geometry("600x400")

        # 添加文本框用于代码编辑
        self.text_editor = scrolledtext.ScrolledText(self.editor_window, wrap=tk.WORD)
        self.text_editor.pack(fill=tk.BOTH, expand=True)

        # 添加菜单栏
        menu_bar = tk.Menu(self.editor_window)
        self.editor_window.config(menu=menu_bar)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)  # 添加新建文件选项
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As...", command=self.save_as_file)  # 可选：添加“另存为”功能

    def new_file(self):
        """清空编辑器，为新建文件做准备"""
        self.text_editor.delete(1.0, tk.END)
        self.current_file = None  # 没有与之关联的文件路径

    def open_file(self):
        """打开一个文件对话框来选择并加载一个route文件"""
        file_path = filedialog.askopenfilename(initialdir=self.base_route_path,
                                               filetypes=[("Python Files", "*.py")])
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:  # 指定使用 UTF-8 编码打开文件
                    code = file.read()
                    self.text_editor.delete(1.0, tk.END)
                    self.text_editor.insert(tk.END, code)
                self.current_file = file_path
            except UnicodeDecodeError:
                messagebox.showerror("Error", "无法读取文件，文件编码可能不正确。")

    def save_file(self):
        if self.current_file:
            with open(self.current_file, 'w', encoding='utf-8') as file:
                code = self.text_editor.get(1.0, tk.END)
                file.write(code)
            messagebox.showinfo("Save", "File saved successfully!")
        else:
            self.save_as_file()

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(initialdir=self.base_route_path,
                                                 defaultextension=".py",
                                                 filetypes=[("Python Files", "*.py")])
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as file:
                code = self.text_editor.get(1.0, tk.END)
                file.write(code)
            self.current_file = file_path
            messagebox.showinfo("Save As", "File saved successfully!")


    def scan_route_modules(self):
        """扫描当前工作目录的 'routes' 子文件夹中的以 'ROUTE' 开头的 Python 文件"""
        directory = self.base_route_path
        if not os.path.exists(directory):
            os.makedirs(directory)  # 如果目录不存在，则创建它
        files = os.listdir(directory)
        route_files = [f[:-3] for f in files if f.startswith('ROUTE') and f.endswith('.py')]
        return route_files

    
    def load_route_module(self, module_name):
        """ 动态加载指定的路线模块 """
        try:
            if module_name in sys.modules:
                reload(sys.modules[module_name])
            else:
                imported_module = import_module(module_name)
            self.route = imported_module.ROUTE(self.controller)
        except ModuleNotFoundError:
            messagebox.showerror("Error", f"Module {module_name} not found.")
            return None


    def on_module_change(self, module_name):
        """处理模块变更，加载选择的模块"""
        if module_name == "No modules found":
            messagebox.showinfo("Info", "No valid modules available.")
            return
        try:
            self.route = self.load_module_func(module_name)
            self.update_output_label()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load module {module_name}: {str(e)}")

    def update_output_label(self):
        point_name = self.route.get_point_name(self.current_number)
        self.output_label.config(text=f"当前点位：{point_name}")

    def next_point(self):
        self.current_number += 1
        if self.current_number >= len(self.route.point_names):
            self.current_number = 0
        self.update_label()

    def execute_current_point_and_advance(self):
        self.route.execute_point(self.current_number)
        self.next_point()

    def change_number(self, delta):
        self.current_number += delta
        self.current_number = max(0, min(len(self.route.point_names) - 1, self.current_number))
        self.update_label()

    def update_label(self):
        self.label.config(text=f"Selected Number: {self.current_number}")
        self.update_output_label()

    def update_status(self):
        status_text = "程序状态：暂停中" if self.program_paused else "程序状态：运行中"
        self.status_label.config(text=status_text)

    def check_joystick(self):
        events, _ = self.controller.get_events()
        for event in events:
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 9:  # 假设左摇杆键的索引为9
                    self.left_thumb_press_count += 1
                    if self.left_thumb_press_count == 2:
                        self.program_paused = not self.program_paused
                        self.update_status()
                        self.left_thumb_press_count = 0  # 重置计数
                elif event.button == 4:  # LS键索引为4
                    if not self.program_paused:
                        self.execute_current_point_and_advance()

            elif event.type == pygame.JOYAXISMOTION:
                # 检测左扳机的运动
                if event.axis == 4:  # 假设左扳机对应的轴索引为2
                    trigger_value = self.controller.read_axes()[4]
                    if trigger_value > 0.5:
                        if not self.program_paused:
                            self.route.auto_map.quick_T()

        hat = self.controller.read_hat()
        if hat[0] == -1 and not self.program_paused:
            self.change_number(-1)
        elif hat[0] == 1 and not self.program_paused:
            self.change_number(1)
        self.window.after(100, self.check_joystick)

    def handle_double_click(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_thumb_press_time < 500:
            self.left_thumb_press_count += 1
        else:
            self.left_thumb_press_count = 1
        self.last_thumb_press_time = current_time
        if self.left_thumb_press_count == 2:
            self.program_paused = not self.program_paused
            self.update_status()
            self.left_thumb_press_count = 0

    def start(self):
        self.window.mainloop()  # 启动 GUI 主循环
