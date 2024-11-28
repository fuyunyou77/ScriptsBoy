###
 # @Author: fuyunyou
 # @Date: 2024-11-28 18:14:13
 # @LastEditors: fuyunyou
 # @LastEditTime: 2024-11-28 18:16:13
 # @Description:自动关机脚本，提前定时提醒
 # @FilePath: \ScriptsBoy\auto_shutdown.py
###
import os
import time
import tkinter as tk
from tkinter import messagebox

# 定义关机函数
def shutdown_computer():
    os.system("shutdown /s /f /t 0")  # 强制关机，不延迟

# 定义显示关机警告的函数
def show_shutdown_warning(seconds_before_shutdown):
    # 创建主窗口（这里我们不需要显示它，所以可以直接隐藏）
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口

    # 计算倒计时的时间间隔（每秒更新一次）
    interval = 1000  # 毫秒

    # 创建一个变量来跟踪剩余时间
    remaining_time = seconds_before_shutdown

    # 定义一个更新倒计时的函数
    def update_countdown():
        nonlocal remaining_time
        if remaining_time > 0:
            # 更新消息框中的文本
            label_var.set(f"系统将在 {remaining_time} 秒后关机。")
            # 安排下一次更新
            root.after(interval, update_countdown)
            # 减少剩余时间
            remaining_time -= 1
        else:
            # 时间到，关闭消息框并关机
            messagebox_window.destroy()
            shutdown_computer()

    # 创建一个字符串变量来动态更新文本
    label_var = tk.StringVar()

    # 创建消息框窗口
    messagebox_window = tk.Toplevel(root)
    messagebox_window.title("关机警告")
    messagebox_window.geometry("300x100")  # 设置窗口大小

    # 在消息框中添加标签来显示倒计时
    label = tk.Label(messagebox_window, textvariable=label_var, font=("Helvetica", 16))
    label.pack(pady=20)  # 添加一些垂直填充

    # 初始化倒计时文本
    label_var.set(f"系统将在 {seconds_before_shutdown} 秒后关机。")

    # 开始倒计时
    update_countdown()

    # 进入主事件循环（虽然在这个脚本中我们实际上不需要它，因为倒计时会自动更新）
    # 但为了保持窗口打开，我们还是调用它
    root.mainloop()  # 注意：在实际应用中，由于我们使用了root.after，这个mainloop可能不会真正“循环”
    # 因为一旦倒计时结束，窗口就会被销毁，mainloop也会随之结束

# 设置关机前的警告时间（秒）
warning_time = 20

# 显示关机警告
show_shutdown_warning(warning_time)