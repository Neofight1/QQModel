import tkinter as tk
from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk

# from QQModel.Interface.friend import FriendPage
from QQModel.Interface.friend import FriendPage
from QQModel.Interface.login import LoginPage

# #eaf1f8经典灰
# 初始界面
from QQModel.Interface.me import me
from QQModel.Interface.model import ModelPage


class BasicPage:
    #  用户界面
    def __init__(self, master, username='', account='', password='', email=''):
        self.root = master
        self.root.title('用户界面')
        self.root.configure(bg='#00a3ff')
        self.root.geometry('584x550')
        self.username = username  # 用户名
        self.account = account  # 账号
        self.password = password  # 密码
        self.email = email  # 邮箱
        self.page = Frame(self.root)
        img_open = Image.open('../normal.png')
        img_png = ImageTk.PhotoImage(img_open)
        label_img = tk.Label(self.page, image=img_png)
        label_img.pack()
        self.create_page()
        img = Image.open("../basic.png")
        img_ = ImageTk.PhotoImage(img)
        Label(self.page, image=img_).pack()
        self.root.mainloop()

    def create_page(self):
        #  布局
        frm1 = Frame(self.page, bg="#00a3ff")  # 最上层
        frm2 = Frame(self.page, bg="#00a3ff")  #
        frm3= Frame(self.page)  #
        # 搜索 聊天 朋友
        button2 = Button(frm1, text="聊天", relief=FLAT, font=('微软雅黑', 10), bg='#00a3ff',
                         fg="#ffffff", width=17, height=1)
        button3 = Button(frm1, text="朋友", relief=FLAT, font=('微软雅黑', 10), bg='#00a3ff',
                         fg="#ffffff", width=17, height=1)
        button4 = Button(frm1, text="返回", command=self.repage, relief=FLAT, font=('微软雅黑', 10), bg='#00a3ff',
                         fg="#ffffff", width=17, height=1)
        button5 = Button(frm1, text="个人", command=self.me, relief=FLAT, font=('微软雅黑', 10), bg='#00a3ff',
                         fg="#ffffff", width=17, height=1)
        button2.pack(side=LEFT)
        button3.pack(side=LEFT)
        button5.pack(side=LEFT)
        button4.pack(side=LEFT)
        frm1.pack()
        Label(frm2, fg="#ffffff", bd=1, bg="#00a3ff", width=100, height=1).pack()
        frm2.pack()
        self.page.pack()

    def modelpage(self):
        #  返回聊天界面
        self.page.destroy()
        ModelPage(self.root, username=self.username, account=self.account, password=self.password, email=self.email)

    def repage(self):
        #  返回登录界面
        self.page.destroy()
        LoginPage(self.root)
    #
    # def friendpage(self):
    #     #  返回朋友界面
    #     self.page.destroy()
    #     FriendPage(self.root, username=self.username, account=self.account, password=self.password, email=self.email)

    def me(self):
        # 打开个人信息界面
        top = Toplevel(self.root)
        me(top,self.account)


root = Tk()
BasicPage(root)
root.mainloop()