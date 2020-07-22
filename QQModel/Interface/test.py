# 多层窗口的实现
# from tkinter import *
#
# root = Tk()
#
# root.title('Toplevel')
#
# Label(root, text='主顶层（默认）').pack(pady = 10)
#
# t1 = Toplevel(root)
#
# Label(t1, text='子顶层').pack(padx=10, pady=10)
#
# t2 = Toplevel(root)
#
# Label(t2, text='临时顶层').pack(padx=10, pady=10)
#
# t2.transient(root)
#
# t3 = Toplevel(root, borderwidth=5, bg='green')
#
# Label(t3, text='不被视窗管理的顶层控件', bg='blue', fg='white').pack(padx=10, pady=10)
#
# t3.overrideredirect(1)
#
# t3.geometry('300x100+150+150')
#
# root.mainloop()


# 滑动框的实现
# import tkinter as tk
#
# root = tk.Tk()
#
# sb = tk.Scrollbar(root)
# sb.pack(side="right", fill="y")
#
# lb = tk.Listbox(root, yscrollcommand=sb.set)
#
# for i in range(1):
#     # tk.Label(sb, text="牛皮", font=('微软雅黑', 10), bg='#cfe8ff', width=420, ).pack()
#     lb.insert("end", "牛皮")
#
# lb.pack(side="left", fill="both")
#
# sb.config(command=lb.yview)
#
# root.mainloop()

# import tkinter as tk
#
# master = tk.Tk()
#
# # 创建一个空列表
# theLB = tk.Listbox(master)
# theLB.pack()
#
# # 往列表里添加数据
# for item in ["鸡蛋", "鸭蛋", "鹅蛋", "李狗蛋"]:
#     theLB.insert("end", item)
#
# theButton = tk.Button(master, text="删除", command=lambda x=theLB: x.delete("active"))
# theButton.pack()
#
# master.mainloop()


# 滑动框绑定操作
# TclError   _tkinter.TclError
# import tkinter
# from tkinter import FLAT, messagebox
# import tkinter as tk
# from tkinter import *
# def myPrint():
#     print(lb.curselection()[0])#提取点中选项的下标
#     print(lb.get(lb.curselection()))#提前点中选项下标的值
#     # lb.insert(lb.curselection(), "*elements")
#     # lb.delete(lb.curselection()+1)
#     # lb.delete(lb.curselection())
#     # try:
#     #     lb.insert(lb.curselection(), "*elements")
#     #     lb.delete(lb.curselection())
#     # except TclError:
#     #     messagebox.showerror("错误", "注册失败")
#     #     return
#     lb.insert(lb.curselection()[0], "*elements")
#     lb.delete(lb.curselection()[0])
#     messagebox.showerror("无", "修改成功")
#
#
#
# win = tkinter.Tk()
# win.title("Listbox列表框")
# win.geometry("800x600+600+100")
# lbv=tkinter.StringVar()#绑定变量
# #SINGLE与BORWSE作用相似，但是不支持鼠标按下后移动选中位置
# lb=tkinter.Listbox(win,selectmode=tkinter.SINGLE,listvariable=lbv)
# lb.pack()
# for item in["good","nice","handsome","very good","verynice"]:
#     lb.insert(tkinter.END,item)
# lb.insert(tkinter.ACTIVE,"cool")
# #打印当前列表的选项
# # print(lbv.get())
# #设置选项,把列表值变为1，2，3
# #lbv.set(("1","2","3"))
# #绑定事件
# button5 = tkinter.Button(win, text="同意", relief=FLAT, command=myPrint, font=('微软雅黑', 10), bg='#00a3ff',
#                          fg="#ffffff", width=14, height=1)
# button5.pack()
# # lb.bind("<Double-Button-1>",myPrint)
# #"<Double-Button-1>"  鼠标双击
# win.mainloop()


# 字符串分割
# txt = "niuniu                                                                        通过"
# x = txt.split(" ", 1)
# print(x[0])


# 时间格式化
# import time
# # 优化格式化化版本
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
# str=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
# print(str)


# 下滑框
# import tkinter as tk
#
# window = tk.Tk()
# # 设置窗口大小
# winWidth = 600
# winHeight = 400
# # 获取屏幕分辨率
# screenWidth = window.winfo_screenwidth()
# screenHeight = window.winfo_screenheight()
#
# x = int((screenWidth - winWidth) / 2)
# y = int((screenHeight - winHeight) / 2)
#
# # 设置主窗口标题
# window.title("Menu菜单参数说明")
# # 设置窗口初始位置在屏幕居中
# window.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
# # 设置窗口图标
# window.iconbitmap("../login.png")
# # 设置窗口宽高固定
# window.resizable(0, 0)
#
# var = tk.StringVar()
# var.set("请选择")
# tk.OptionMenu(window, var, "one", "two", "three").pack()
#
#
# def getValue():
#     print(var.get())
#
#
# tk.Button(window, text="get value", width=30, pady=5, command=getValue).pack()
# window.mainloop()


# 下滑框
# import tkinter
# from tkinter import ttk
# def go(*args):  # 处理事件，*args表示可变参数
#     print(comboxlist.get())  # 打印选中的值
# win = tkinter.Tk()  # 构造窗体
# comvalue = tkinter.StringVar()  # 窗体自带的文本，新建一个值
# comboxlist = ttk.Combobox(win, textvariable=comvalue)  # 初始化
# comboxlist["values"] = ("1", "2", "3", "4")
# comboxlist.current(0)  # 选择第一个
# comboxlist.bind("<<ComboboxSelected>>", go)  # 绑定事件,(下拉列表框被选中时，绑定go()函数)
# comboxlist.pack()
#
# win.mainloop()  # 进入消息循环


# tkinter  的Text演示
# import tkinter as tk
#
# root = tk.Tk()
#
# text = tk.Text(root, width=20, height=5, relief="flat")
# text.pack()
#
# # 设置 tag
# text.tag_config("tag_1", backgroun="yellow", foreground="red")
#
# # "insert" 索引表示插入光标当前的位置
# text.insert("insert", "I love ")
# text.insert("end", "FishC.com!", "tag_1")
# text.insert("end", "FishC.com!\n", "tag_1")
#
# root.mainloop()
#  这就是我要找的啊
# import tkinter as tk
#
# root = tk.Tk()
#
# text = tk.Text(root, width=200, height=5)
# text.pack()
#
# text.insert("insert", "I love Python!")
#
#
# def show():
#     text.insert("insert", "I love Python!")
#
#
# b1 = tk.Button(root, text="点我点我", command=show)
# text.window_create("insert", window=b1)
#
# root.mainloop()


# value='脚本123牛'
# length = len(value)
# utf8_length = len(value.encode('utf-8'))
# length = (utf8_length - length)/2 + length
# print(length)

# 每隔一段时间执行代码
import threading

def hello():
    print("hello, world")
    t = threading.Timer(10.0, hello)
    t.start()
print("Hi")
i=10
i=i+20
print(i)
hello()