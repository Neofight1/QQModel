import tkinter as tk
from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk
from django.db.backends import sqlite3

from QQModel.Entity.user import user
from QQModel.Interface.login import LoginPage
import random


class RegisterPage:
    #  注册界面
    # 姓名、昵称、性别、账号、电子邮箱、密码   User (name, nickname, gender, account, email, password)
    global genderLabel

    def __init__(self, master=None):
        self.root = master
        self.root.title('账号注册')
        self.root.configure(bg='#eaf1f8')
        self.root.geometry('536x520')
        self.name = StringVar()  # 姓名
        self.nickname = StringVar()  # 昵称
        self.gender = StringVar()  # 性别
        self.account = StringVar()  # 账号
        self.email = StringVar()  # 邮箱
        self.password0 = StringVar()  # 第一次输入密码
        self.password1 = StringVar()  # 第二次输入密码
        self.gender = "未选择"
        # self.v = IntVar()  # 性别判别因子  0为未选 1为男 2为女
        # self.v = 0
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
        frm7 = Frame(self.page)  # 第二次输入密码
        frm8 = Frame(self.page)  # 注册和返回
        # 姓名
        frm11 = Frame(frm1)
        frm12 = Frame(frm1)
        frm13 = Frame(frm1)
        Label(frm11, text='姓名', fg="#2295ec", font=('微软雅黑', 12)).pack(side=RIGHT)
        Label(frm12, bg="#eaf1f8", 	width=12).pack()
        entry = tk.Entry(frm13, textvariable=self.name, relief=FLAT).pack(side=LEFT)
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
        entry1 = tk.Entry(frm23, textvariable=self.nickname, relief=FLAT)
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
        Label(frm32, bg="#eaf1f8", width=8).pack()
        global genderLabel
        genderLabel = Label(frm33, text="  ", justify=RIGHT, bg="#eaf1f8", width=7, font=('微软雅黑', 12))
        genderLabel.pack(side=LEFT)
        Button(frm33, text='女', command=self.girl, bg='#badaf8', font=('微软雅黑', 12), width=4,  relief=FLAT).pack(side=RIGHT)
        Button(frm33, text='男', command=self.boy, bg='#badaf8', font=('微软雅黑', 12), width=4, relief=FLAT).pack(side=RIGHT)
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
        Label(frm42, bg="#eaf1f8", width=12).pack()
        Label(frm43, text=self.makeaccount(), fg="black", font=('微软雅黑', 12)).pack(side=RIGHT)
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
        entry2 = tk.Entry(frm53, textvariable=self.email, relief=FLAT)
        entry2.pack(side=LEFT)
        frm51.pack(side=LEFT)
        frm53.pack(side=RIGHT)
        frm52.pack(side=RIGHT)
        frm5.pack()
        # 第一次输入密码
        frm61 = Frame(frm6)
        frm62 = Frame(frm6)
        frm63 = Frame(frm6)
        Label(frm61, text='密码', fg="#2295ec", font=('微软雅黑', 12)).pack(side=RIGHT)
        Label(frm62, bg="#eaf1f8", width=12).pack()
        entry3 = tk.Entry(frm63, textvariable=self.password0, relief=FLAT)
        entry3.pack(side=LEFT)
        frm61.pack(side=LEFT)
        frm63.pack(side=RIGHT)
        frm62.pack(side=RIGHT)
        frm6.pack()
        # 第二次输入密码
        frm71 = Frame(frm7)
        frm72 = Frame(frm7)
        frm73 = Frame(frm7)
        Label(frm71, text='确认密码', fg="#2295ec", font=('微软雅黑', 12)).pack(side=RIGHT)
        Label(frm72, bg="#eaf1f8", width=7).pack()
        entry4 = tk.Entry(frm73, textvariable=self.password1, relief=FLAT)
        entry4.pack(side=LEFT)
        frm71.pack(side=LEFT)
        frm73.pack(side=RIGHT)
        frm72.pack(side=RIGHT)
        frm7.pack()
        # 按钮
        button1 = Button(frm8, text="返回", command=self.repage, relief=FLAT, font=('微软雅黑', 10), bg='#00a3ff', fg="#ffffff", width=18, height=1,)
        button1.pack(side=RIGHT)
        Label(frm8, fg="#eaf1f8", bg="#eaf1f8").pack(side=RIGHT)
        button2 = Button(frm8, text="注册", command=self.register, relief=FLAT, font=('微软雅黑', 10), bg='#00a3ff', fg="#ffffff", width=18, height=1,)
        button2.pack(side=RIGHT)
        frm8.pack(pady=15)
        self.page.pack()

    def repage(self):
        #  返回
        self.page.destroy()
        LoginPage(self.root)

    def register(self):
        #  注册
        if len(self.name.get()) == 0:
            messagebox.showerror("错误", "姓名不能为空")
        elif len(self.nickname.get()) == 0:
            messagebox.showerror("错误", "昵称不能为空")
        elif self.gender == "未选择":
            messagebox.showerror("错误", "性别未选择")
        elif len(self.email.get()) == 0:
            messagebox.showerror("错误", "邮箱不能为空")
        elif len(self.password0.get()) == 0:
            messagebox.showerror("错误", "密码不能为空")
        elif self.password0.get() != self.password1.get():
            messagebox.showerror("错误", "两次密码不一致")
        else:
            a = user(name=self.name.get(), nickname=self.nickname.get(), gender=self.gender,
                     account=self.account, email=self.email.get(), password=self.password0.get())
            if a.create_user() == 1:
                messagebox.showinfo('提示', '注册成功')
            else:
                messagebox.showerror("错误", "注册失败")

    def makeaccount(self):
        #  生成账号  9位随机数
        while 1:
            str1 = ""
            for i in range(1, 10):
                temp = random.randint(1, 9)
                str1 += str(temp)
            self.account = str1
            #  数据库查询是否有这个号了，无就退出循环，有继续循环
            a = user(account=self.account)
            if a.select_for_account():
                break
        return self.account

    def boy(self):
        #  男孩
        genderLabel.configure(text="男")
        self.gender = "男"

    def girl(self):
        #  男孩
        genderLabel.configure(text="女")
        self.gender = "女"

root = Tk()
RegisterPage(root)
root.mainloop()

