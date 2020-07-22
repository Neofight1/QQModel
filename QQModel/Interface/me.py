import tkinter as tk
from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk
from django.db.backends import sqlite3

from QQModel.Entity.user import user
import random


class me:
    #  个人信息界面
    # 姓名、昵称、性别、账号、电子邮箱、密码   User (name, nickname, gender, account, email, password)
    global genderLabel

    def __init__(self, master=None,account=''):
        self.root = master
        self.root.title('个人信息')
        self.root.configure(bg='#eaf1f8')
        self.root.geometry('536x450')
        self.name = StringVar()  # 姓名
        self.nickname = StringVar()  # 昵称
        self.gender = StringVar()  # 性别
        self.account = account  # 账号
        self.email = StringVar()  # 邮箱
        self.password = StringVar()  # 第一次输入密码
        # 与文本框变量绑定
        self.name1 = StringVar()
        self.nickname1 = StringVar()
        self.gender1 = StringVar()
        self.account1 = StringVar()
        self.email1 = StringVar()
        self.password1 = StringVar()
        # 初始化
        self.initialization()
        # 变量绑定初始化
        self.name1.set(self.name)
        self.nickname1.set(self.nickname)
        self.gender1.set(self.gender)
        self.account1.set(self.account)
        self.email1.set(self.email)
        self.password1.set(self.password)
        self.page = Frame(self.root)
        img_open = Image.open('../login.png')
        img_png = ImageTk.PhotoImage(img_open)
        label_img = tk.Label(self.page, image=img_png)
        label_img.pack()
        self.create_page()
        self.root.mainloop()

    def create_page(self):
        #  布局
        frm1 = Frame(self.page)  # 姓名
        frm2 = Frame(self.page)  # 昵称
        frm3 = Frame(self.page)  # 性别
        frm4 = Frame(self.page)  # 账号
        frm5 = Frame(self.page)  # 邮箱
        frm6 = Frame(self.page)  # 第一次输入密码
        frm8 = Frame(self.page)  # 注册和返回
        # 姓名
        frm11 = Frame(frm1)
        frm12 = Frame(frm1)
        frm13 = Frame(frm1)
        Label(frm11, text='姓名', fg="#2295ec", font=('微软雅黑', 12)).pack(side=RIGHT)
        Label(frm12, bg="#eaf1f8", 	width=12).pack()
        entry = tk.Entry(frm13, textvariable=self.name1, relief=FLAT, font=('微软雅黑', 12)).pack(side=LEFT)
        frm11.pack(side=LEFT)
        frm13.pack(side=RIGHT)
        frm12.pack(side=RIGHT)
        frm1.pack()
        # 昵称
        frm21 = Frame(frm2)
        frm22 = Frame(frm2)
        frm23 = Frame(frm2)
        Label(frm21, text='昵称', fg="#2295ec", font=('微软雅黑', 12)).pack(side=RIGHT)
        Label(frm22, bg="#eaf1f8", width=12).pack()
        entry1 = tk.Entry(frm23, textvariable=self.nickname1, relief=FLAT, font=('微软雅黑', 12))
        entry1.pack(side=LEFT)
        frm21.pack(side=LEFT)
        frm23.pack(side=RIGHT)
        frm22.pack(side=RIGHT)
        frm2.pack()
        # 性别
        frm31 = Frame(frm3)
        frm32 = Frame(frm3)
        frm33 = Frame(frm3)
        Label(frm31, text='性别', fg="#2295ec", font=('微软雅黑', 12)).pack(side=RIGHT)
        Label(frm32, bg="#eaf1f8", width=9).pack()
        global genderLabel
        genderLabel = Label(frm33, textvariable=self.gender1, justify=RIGHT, bg="#eaf1f8", width=6, font=('微软雅黑', 12))
        genderLabel.pack(side=LEFT)
        Button(frm33, text='女', command=self.girl, bg='#badaf8', font=('微软雅黑', 12), width=6,  relief=FLAT).pack(side=RIGHT)
        Button(frm33, text='男', command=self.boy, bg='#badaf8', font=('微软雅黑', 12), width=6, relief=FLAT).pack(side=RIGHT)
        frm31.pack(side=LEFT)
        frm33.pack(side=RIGHT)
        frm32.pack(side=RIGHT)
        frm3.pack()
        # 账号
        frm41 = Frame(frm4)
        frm42 = Frame(frm4)
        frm43 = Frame(frm4)
        frm44 = Frame(frm4)
        Label(frm41, text='账号', fg="#2295ec", font=('微软雅黑', 12), width=3).pack(side=RIGHT)
        Label(frm42, bg="#eaf1f8", width=17).pack()
        Label(frm43, textvariable=self.account1, fg="black", font=('微软雅黑', 12)).pack(side=RIGHT)
        Label(frm44, bg="#eaf1f8", width=8).pack()
        frm41.pack(side=LEFT)
        frm44.pack(side=RIGHT)
        frm43.pack(side=RIGHT)
        frm42.pack(side=RIGHT)
        frm4.pack()
        # 邮箱
        frm51 = Frame(frm5)
        frm52 = Frame(frm5)
        frm53 = Frame(frm5)
        Label(frm51, text='邮箱', fg="#2295ec", font=('微软雅黑', 12)).pack(side=RIGHT)
        Label(frm52, bg="#eaf1f8", width=12).pack()
        entry2 = tk.Entry(frm53, textvariable=self.email1, relief=FLAT, font=('微软雅黑', 12))
        entry2.pack(side=LEFT)
        frm51.pack(side=LEFT)
        frm53.pack(side=RIGHT)
        frm52.pack(side=RIGHT)
        frm5.pack()
        # 输入密码
        frm61 = Frame(frm6)
        frm62 = Frame(frm6)
        frm63 = Frame(frm6)
        Label(frm61, text='密码', fg="#2295ec", font=('微软雅黑', 12)).pack(side=RIGHT)
        Label(frm62, bg="#eaf1f8", width=12).pack()
        entry3 = tk.Entry(frm63, textvariable=self.password1, relief=FLAT, font=('微软雅黑', 12))
        entry3.pack(side=LEFT)
        frm61.pack(side=LEFT)
        frm63.pack(side=RIGHT)
        frm62.pack(side=RIGHT)
        frm6.pack()
        # 按钮
        button1 = Button(frm8, command=self.register, text="修改", relief=FLAT, font=('微软雅黑', 10), bg='#00a3ff', fg="#ffffff", width=18, height=1,)
        button1.pack(side=RIGHT)
        frm8.pack(pady=15)
        self.page.pack()


    def register(self):
        #  修改
        if len(self.name1.get()) == 0:
            messagebox.showerror("错误", "姓名不能为空")
        elif len(self.nickname1.get()) == 0:
            messagebox.showerror("错误", "昵称不能为空")
        elif len(self.email1.get()) == 0:
            messagebox.showerror("错误", "邮箱不能为空")
        elif len(self.password1.get()) == 0:
            messagebox.showerror("错误", "密码不能为空")
        else:
            if messagebox.askokcancel("提示", "确定修改嘛"):
                a = user(name=self.name1.get(), nickname=self.nickname1.get(), gender=self.gender1.get(),
                         account=self.account1.get(), email=self.email1.get(), password=self.password1.get())
                if a.set_user() == 1:
                    messagebox.showinfo('提示', '修改成功')
                else:
                    messagebox.showerror("错误", "修改失败")

    def initialization(self):
        #  初始化
        a = user(account=self.account)
        b=a.get_user()
        self.name = b.name  # 姓名
        self.nickname =b.nickname  # 昵称
        self.gender = b.gender  # 性别
        self.account = b.account  # 账号
        self.email = b.email  # 邮箱
        self.password = b.password  # 密码

    def boy(self):
        #  男孩
        global genderLabel
        genderLabel.configure(text="男")
        self.gender1.set("男")

    def girl(self):
        #  男孩
        global genderLabel
        genderLabel.configure(text="女")
        self.gender1.set("女")

# root = Tk()
# me(root,'256767845')
# root.mainloop()

