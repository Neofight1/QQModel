
from tkinter import messagebox
import tkinter as tk
from tkinter import *

from PIL import Image
from PIL import ImageTk

from QQModel.Entity.chat import chat
from QQModel.Entity.friend import friend
from QQModel.Entity.request import request
from QQModel.Entity.user import user
import random


class LoginPage:
    global entry1
    global Button1
    global temp
    temp = 0

    def __init__(self, master):
        # 登录界面
        self.root = master
        self.root.geometry('536x371')
        self.root.title('模拟QQ')
        self.root.configure(bg='#eaf1f8')
        self.account = StringVar()  # 账号
        self.password = StringVar()  # 密码
        self.judge = IntVar()  # 操作判断
        self.page = Frame(self.root)
        # 图片
        img_open = Image.open('../login.png')
        img_png = ImageTk.PhotoImage(img_open)
        label_img = tk.Label(self.page, image=img_png)
        label_img.pack()
        self.create_page()
        self.root.mainloop()

    def create_page(self):
        # 界面布局
        frm1 = Frame(self.page)
        frm2 = Frame(self.page)
        frm3 = Frame(self.page)
        frm11 = Frame(frm1)
        frm12 = Frame(frm1)
        Label(frm11, text='账号', fg="#2295ec", font=('微软雅黑', 12)).pack(side=RIGHT)
        entry = tk.Entry(frm12, textvariable=self.account, relief=FLAT).pack(side=LEFT)
        Button(frm12, text="注册账号", command=self.register, fg="#2295ec", width=6, height=1, font=('微软雅黑', 10),
               relief=FLAT).pack(side=RIGHT)
        frm11.pack(side=LEFT)
        frm12.pack(side=RIGHT)
        frm1.pack(pady=15)
        # 输入密码框
        frm21 = Frame(frm2)
        frm22 = Frame(frm2)
        Label(frm21, text='密码', fg="#2295ec", font=('微软雅黑', 12)).pack(side=RIGHT)
        global entry1
        global Button1
        entry1 = tk.Entry(frm22, textvariable=self.password, fg="#ffffff", relief=FLAT, selectbackground="white",
                          selectforeground="white")
        entry1.pack(side=LEFT)
        Button1 = Button(frm22, command=self.show_password, text="显示密码", fg="#2295ec", width=6, height=1, font=('微软雅黑', 10), relief=FLAT)
        Button1.pack(side=RIGHT)
        frm21.pack(side=LEFT)
        frm22.pack(side=RIGHT)
        frm2.pack()
        # 登录选项
        Button(frm3, command=self.get_context, text="登录", bg='#00a3ff', fg="#ffffff", width=18, height=1, font=('微软雅黑', 10),
               relief=FLAT).pack(pady=15)
        frm3.pack()
        self.page.pack()

    def get_context(self):
        # 登录
        account_text = self.account.get()
        password_text = self.password.get()
        if account_text == '':
            tk.messagebox.showinfo('提示', "账号不能为空")
            return
        if password_text == '':
            tk.messagebox.showinfo('提示', "密码不能为空")
            return
        a = user(account=self.account.get(), password=self.password.get())
        # 返回0为没有此帐号，1为校验成功，2为密码错误
        b = a.login_check()
        print(b,self.account.get(), self.password.get())
        if b == 0:
            messagebox.showerror("错误", "没有此账号")
        elif b == 1:
            messagebox.showinfo('提示', '登录成功')
            temp = a.get_user()
            self.page.destroy()
            BasicPage(self.root, username=temp.nickname, account=temp.account, password=temp.password, email=temp.email)
        elif b == 2:
            messagebox.showerror("错误", "密码错误")

        # 数据库操作 成功就进入，失败显示问题

    def register(self):
        # 注册功能跳转
        self.page.destroy()
        RegisterPage(self.root)

    def show_password(self):
        # 显示密码以及消失
        global temp
        if temp == 0:
            entry1.configure(fg='black')
            Button1.configure(text="隐藏密码")
            temp = 1
        else:
            entry1.configure(fg='#ffffff')
            Button1.configure(text="显示密码")
            temp = 0


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



class ModelPage:
    global lb1   #左上
    global lb2   #左下
    global users1   #左上
    global users2   #左下
    global chattext    # 聊天框
    global t           # 输入框
    #  聊天界面
    def __init__(self, master, username='', account='', password='', email=''):
        self.root = master
        self.root.title('用户界面')
        self.root.configure(bg='#00a3ff')
        self.root.geometry('584x550')
        self.username = username  # 用户名
        self.account = account  # 账号
        self.password = password  # 密码
        self.email = email  # 邮箱
        self.select = StringVar()  # 搜索信息


        self.talkaccount = ''  # 聊天的人的账号
        self.tempname = StringVar()  # 聊天的人的昵称
        self.content = ''  # 输入框里的信息
        self.chatcontent = StringVar()  # 聊天内容


        # 递归判别
        self.mark = 0

        self.page = Frame(self.root)
        img_open = Image.open('../normal.png')
        img_png = ImageTk.PhotoImage(img_open)
        label_img = tk.Label(self.page, image=img_png)
        label_img.pack()
        img = Image.open("../search.png")
        img_ = ImageTk.PhotoImage(img)
        Label(self.page, image=img_, width=24, height=25, relief=FLAT)
        self.create_page()
        self.root.mainloop()

    def create_page(self):
        #  布局
        frm1 = Frame(self.page, bg="#00a3ff")  # 最上层
        frm2 = Frame(self.page, bg="#00a3ff")  #
        frm3= Frame(self.page)  #
        # 搜索 聊天 朋友
        entry1 = tk.Entry(frm1, textvariable=self.select,  width=15).pack(side=LEFT)
        button1 = Button(frm1, text="搜索", command=self.select_user, relief=FLAT, font=('微软雅黑', 10), bg='#00a3ff',
                         fg="#ffffff", width=11, height=1)
        button2 = Button(frm1, text="聊天", relief=FLAT, font=('微软雅黑', 10), bg='#00a3ff',
                         fg="#ffffff", width=11, height=1)
        button3 = Button(frm1, text="朋友", command=self.friendpage, relief=FLAT, font=('微软雅黑', 10), bg='#00a3ff',
                         fg="#ffffff", width=11, height=1)
        button4 = Button(frm1, text="返回", command=self.repage, relief=FLAT, font=('微软雅黑', 10), bg='#00a3ff',
                         fg="#ffffff", width=11, height=1)
        button5 = Button(frm1, text="个人", command=self.me, relief=FLAT, font=('微软雅黑', 10), bg='#00a3ff',
                         fg="#ffffff", width=11, height=1)
        button1.pack(side=LEFT)
        button2.pack(side=LEFT)
        button3.pack(side=LEFT)
        button5.pack(side=LEFT)
        button4.pack(side=LEFT)
        frm1.pack()
        Label(frm2, fg="#ffffff", bd=1, bg="#00a3ff", width=100, height=1).pack()
        frm2.pack()
        # 两块
        # 左
        frmL = Frame(frm3, bg="#e7e7e7", width=80, height=400)
        # 搜索结果标签
        frmLB1 = Frame(frmL, bg="#e7e7e7", width=18, height=400)
        Label(frmLB1, text="搜索结果", bd=1, bg="#e7e7e7", font=('微软雅黑', 10, ), width=20, height=1, anchor=W).pack()
        # 搜索结果
        frmLB2 = Frame(frmL, bg="#e7e7e7", width=80, height=400)
        sb1 = tk.Scrollbar(frmLB2, activerelief="flat",relief="ridge")
        sb1.pack(side="right", fill="y")
        global lb1  # 搜索结果
        lb1 = tk.Listbox(frmLB2, yscrollcommand=sb1.set, background='white', relief="flat", font=('微软雅黑', 10, ), width=18, height=10, selectbackground="#00a3ff")
        # 查询数据并输出在下拉框里
        lb1.pack(side="left", fill="both")
        sb1.config(command=lb1.yview)
        # 朋友标签
        frmLB3 = Frame(frmL, bg="#e7e7e7", width=18, height=400)
        Label(frmLB3, text="朋友", bd=1, bg="#e7e7e7", font=('微软雅黑', 10,), width=20, height=1, anchor=W).pack()
        # 朋友
        frmLB4 = Frame(frmL, bg="#e7e7e7", width=80, height=500)
        sb2 = tk.Scrollbar(frmLB4, activerelief="flat", relief="ridge")
        sb2.pack(side="right", fill="y")
        global lb2  # 朋友结果
        lb2 = tk.Listbox(frmLB4, yscrollcommand=sb1.set, background='white', relief="flat", font=('微软雅黑', 10,),
                         width=18, height=10, selectbackground="#00a3ff")
        # 查询数据并输出在下拉框里
        lb2.pack(side="left", fill="both")
        sb2.config(command=lb1.yview)

        frmLB1.pack()
        frmLB2.pack()
        frmLB3.pack()
        frmLB4.pack()
        frmL.pack(side=LEFT)


        # 右
        frmR = Frame(frm3, bg="#ffffff", width=420, height=500)
        frmR.pack(side=RIGHT)
        #名字
        frmRT_name = Frame(frmR, bg="#c2def6", width=420, height=25)
        Label(frmRT_name, textvariable=self.tempname, bd=1, bg="#c2def6", font=('微软雅黑', 14,), width=420, height=1, anchor=W).pack()
        frmRT_name.pack(side=TOP)
        # 对话
        frmRT = Frame(frmR, bg="#eeeeee", width=420, height=275)
        global chattext
        chattext = Text(frmRT, height=13, relief=FLAT, font=('微软雅黑', 10), state="disabled")
        chattext.pack(side=TOP)
        frmRT.pack(side=TOP)
        # 输入框和确定键
        frmRB = Frame(frmR, bg="blue", width=420, height=200)
        Label(frmRB,  bd=1, bg="#c2def6", font=('微软雅黑', 10,), width=420, height=1,
              anchor=W).pack()
        global t  # 输入框
        t = tk.Text(frmRB, height=5, relief=FLAT, font=('微软雅黑', 10))
        t.pack(side=TOP)
        frmRBR = Frame(frmRB, bg="#ffffff", width=40, height=20)
        frmRB.pack(side=BOTTOM)
        Label(frmRBR, bd=1, bg="#ffffff", width=50, height=1).pack(side=LEFT)
        button6 = Button(frmRBR, text="发送", command=self.sendchat, fg="#ffffff", bd=1, bg="#0188fb", width=10, height=1, relief=FLAT)
        button6.pack(side=RIGHT)
        frmRBR.pack()
        frm3.pack()
        self.page.pack()
        self.initialization()
        lb1.bind("<Double-Button-1>", self.showchat1)
        lb2.bind("<Double-Button-1>", self.showchat2)
        #"<Double-Button-1>"  鼠标双击

    def repage(self):
        #  返回登录界面
        self.page.destroy()
        LoginPage(self.root)

    def friendpage(self):
        #  返回朋友界面
        self.page.destroy()
        FriendPage(self.root, username=self.username, account=self.account, password=self.password, email=self.email)

    def me(self):
        # 打开个人信息界面
        top = Toplevel(self.root)
        me(top,self.account)

    def initialization(self):
        # 初始化信息
        global lb2
        global users2
        users2 = []
        b = friend(account=self.account)
        temp1 = b.select_friend()
        for i in temp1:
            c = user(account=i.get('account'))
            temp = c.get_user()
            temp2 = {}
            temp2['name'] = temp.name
            temp2['nickname'] = temp.nickname
            temp2['gender'] = temp.gender
            temp2['account'] = temp.account
            temp2['email'] = temp.email
            temp2['password'] = temp.password
            users2.append(temp2)
            lb2.insert("end", temp.nickname)

    def select_user(self):
        global lb1
        global users1
        users1 = []
        lb1.delete(0, END)
        a = user(account=self.select.get())
        # 接收到的申请
        users1 = a.select_user()
        for i in users1:
            b = friend(account=self.account, friend_account=i['account'])
            temp = b.judge_friend()
            if temp==1:
                lb1.insert("end", i.get('nickname').ljust(6,chr(12288)) + "朋友")
                i['judge']=1
            else:
                if i['account']==self.account:
                    lb1.insert("end", i.get('nickname').ljust(6,chr(12288)) + "我")
                else:
                    lb1.insert("end", i.get('nickname'))
                i['judge'] = 0

    def showchat1(self, event):
        # 展示聊天记录
        global users1
        global chattext
        try:
            temp = lb1.curselection()[0]
            self.tempname.set(users1[temp].get('nickname'))
            self.talkaccount = users1[temp].get('account')
            # 设置可编辑
            chattext.configure(state="normal")
            chattext.delete(1.0, "end")
            # 对方
            chattext.tag_config("tag_1", backgroun="#eeeeee", foreground="black", font=('微软雅黑', 10,))
            # 我
            chattext.tag_config("tag_2", backgroun="#2683f5", foreground="white", font=('微软雅黑', 10,))
            chattext.tag_config("tag_3", backgroun="white", foreground="white", font=('微软雅黑', 10,))
            # 导入聊天框
            a = chat(account=self.account, receiver_account=self.talkaccount)
            b = a.get_chat()
            for r in b:
                if r['account'] == self.account:
                    tempstr = r['content']
                    c = tempstr.split("\n")
                    self.deal_chat2(c)
                elif r['account'] == self.talkaccount:
                    tempstr = r['content']
                    c = tempstr.split("\n")
                    self.deal_chat1(c)
            # 设置不可编辑
            chattext.configure(state="disabled")
        except IndexError:
            return

    def showchat2(self, event):
        # 展示聊天记录
        global users2
        global chattext
        # 表明已经有人开始聊天了
        self.mark = 1
        temp = lb2.curselection()[0]
        self.tempname.set(users2[temp].get('nickname'))
        self.talkaccount = users2[temp].get('account')
        # 设置可编辑
        chattext.configure(state="normal")
        chattext.delete(1.0, "end")
        # 对方
        chattext.tag_config("tag_1", backgroun="#eeeeee", foreground="black", font=('微软雅黑', 10,))
        # 我
        chattext.tag_config("tag_2", backgroun="#2683f5", foreground="white", font=('微软雅黑', 10,))
        chattext.tag_config("tag_3", backgroun="white", foreground="white", font=('微软雅黑', 10,))
        # 导入聊天框
        a = chat(account=self.account, receiver_account=self.talkaccount)
        b = a.get_chat()
        for r in b:
            if r['account']==self.account:
                tempstr = r['content']
                c = tempstr.split("\n")
                self.deal_chat2(c)
            elif r['account']==self.talkaccount:
                tempstr = r['content']
                c = tempstr.split("\n")
                self.deal_chat1(c)
        # 设置不可编辑
        chattext.configure(state="disabled")


    def deal_chat1(self,templist):
        # 处理一条对话   对方发来的
        global chattext
        mvp = self.maxlength(templist)
        for i in templist:
            if i != '':
                chattext.insert("end", " ".ljust(2, "*"), "tag_3")
                chattext.insert("end", i.ljust(int(self.chinalength(i, mvp)), '-'), "tag_1")
                chattext.insert("end", "\n")
        chattext.insert("end", "\n")

    def deal_chat2(self,templist):
        # 处理一条对话   我发的
        global chattext
        mvp = self.maxlength(templist)
        for i in templist:
            if i!='':
                chattext.insert("end", " ".ljust(66 - int(mvp), "*"),"tag_3")
                chattext.insert("end", i.ljust(int(self.chinalength(i,mvp)), ' '), "tag_2")
                chattext.insert("end", "\n")
        chattext.insert("end", "\n")

    def maxlength(self,templist):
        # 计算一个字符列表中所有字符中最长字符串长度
        length = 0
        for i in templist:
            value = i
            length1 = len(value)
            utf8_length = len(value.encode('utf-8'))
            length1 = (utf8_length - length1) / 2 + length1
            if length1>length:
                length = length1
        if length>60:  # 对话框最大长度
            length = 60
        # print(str," ",length)
        return length

    def reallength(self,str):
        # 计算一个字符串真正长度
        value = str
        length1 = len(value)
        utf8_length = len(value.encode('utf-8'))
        length1 = (utf8_length - length1) / 2 + length1
        return length1

    def chinalength(self,str,a):
        # 补足用
        value = str
        length1 = len(value)
        utf8_length = len(value.encode('utf-8'))
        return a-self.reallength(str)+length1

    def sendchat(self):
        # 发出聊天信息
        global t
        self.content = t.get(1.0, "end")
        if self.reallength(self.content)>80:
            messagebox.showerror("错误", "输入字段过长")
            return
        if self.reallength(self.content) == 0:
            messagebox.showerror("错误", "输入不能为空")
            return
        if len(self.tempname.get()) == 0:
            return
        # 信息输入到数据库
        a = chat(account=self.account, receiver_account=self.talkaccount, sendName=self.username,
                 receiveName=self.tempname.get(), content=self.content)
        a.create_chat()
        # 展示出来
        global chattext
        chattext.configure(state="normal")
        c = self.content.split("\n")
        self.deal_chat2(c)
        chattext.configure(state="disabled")
        t.delete(1.0, "end")


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
        button2 = Button(frm1, text="聊天", command=self.modelpage, relief=FLAT, font=('微软雅黑', 10), bg='#00a3ff',
                         fg="#ffffff", width=17, height=1)
        button3 = Button(frm1, text="朋友", command=self.friendpage, relief=FLAT, font=('微软雅黑', 10), bg='#00a3ff',
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

    def friendpage(self):
        #  返回朋友界面
        self.page.destroy()
        FriendPage(self.root, username=self.username, account=self.account, password=self.password, email=self.email)

    def me(self):
        # 打开个人信息界面
        top = Toplevel(self.root)
        me(top,self.account)


class FriendPage:
    global lb   #右上
    global lb1   #右下
    global lb2   #左
    global users1   #右上
    global users2   #右上
    global users3   #左
    #  用户界面
    def __init__(self, master, username='', account='', password='', email=''):
        self.root = master
        self.root.title('用户界面')
        self.root.configure(bg='#00a3ff')
        self.root.geometry('584x600')
        self.username = username  # 用户名
        self.account = account  # 账号
        self.password = password  # 密码
        self.email = email  # 邮箱
        self.select = StringVar()  # 搜索信息
        self.page = Frame(self.root)
        img_open = Image.open('../normal.png')
        img_png = ImageTk.PhotoImage(img_open)
        label_img = tk.Label(self.page, image=img_png)
        label_img.pack()
        self.create_page()
        self.root.mainloop()

    def create_page(self):
        #  布局
        frm1 = Frame(self.page, bg="#00a3ff")  # 最上层
        frm2 = Frame(self.page, bg="#00a3ff")  #
        frm3= Frame(self.page)  #
        # 搜索 聊天 朋友
        entry1 = tk.Entry(frm1, textvariable=self.select, width=15).pack(side=LEFT)
        button1 = Button(frm1, text="搜索", command=self.select_user, relief=FLAT, font=('微软雅黑', 10), bg='#00a3ff',
                         fg="#ffffff", width=11, height=1)
        button2 = Button(frm1, text="聊天", relief=FLAT, command=self.modelpage, font=('微软雅黑', 10), bg='#00a3ff',
                         fg="#ffffff", width=11, height=1)
        button3 = Button(frm1, text="朋友", relief=FLAT, font=('微软雅黑', 10), bg='#00a3ff',
                         fg="#ffffff", width=11, height=1)
        button4 = Button(frm1, text="返回", command=self.repage, relief=FLAT, font=('微软雅黑', 10), bg='#00a3ff',
                         fg="#ffffff", width=11, height=1)
        button5 = Button(frm1, text="个人", command=self.me, relief=FLAT, font=('微软雅黑', 10), bg='#00a3ff',
                         fg="#ffffff", width=11, height=1)
        button1.pack(side=LEFT)
        button2.pack(side=LEFT)
        button3.pack(side=LEFT)
        button5.pack(side=LEFT)
        button4.pack(side=LEFT)
        frm1.pack()
        Label(frm2,  bd=1, bg="#00a3ff", width=100, height=1).pack()
        frm2.pack()
        # 两块
        # 左
        frmL = Frame(frm3, bg="#e7e7e7", width=80, height=500)
        # 具体内容
        frmLB1 = Frame(frmL, bg="#e7e7e7", width=80, height=500)
        sb2 = tk.Scrollbar(frmLB1, activerelief="flat",relief="ridge")
        sb2.pack(side="right", fill="y")
        global lb2
        lb2 = tk.Listbox(frmLB1, yscrollcommand=sb2.set, background='white', relief="flat", font=('微软雅黑', 10, ), width=18, height=22, selectbackground="#00a3ff")
        # 查询数据并输出在下拉框里
        lb2.pack(side="left", fill="both")
        sb2.config(command=lb2.yview)
        # 按钮
        frmLB2 = Frame(frmL, bg="#cfe8ff", width=80, height=500)
        button7 = Button(frmLB2, text="发送申请", command=self.send_request, relief=FLAT, font=('微软雅黑', 10), bg='#00a3ff',
                         fg="#ffffff", width=9, height=1)

        button8 = Button(frmLB2, text="查看信息", command=self.check_user, relief=FLAT, font=('微软雅黑', 10), bg='#00a3ff',
                         fg="#ffffff", width=9, height=1)
        button7.pack(side=RIGHT)
        button8.pack(side=LEFT)
        frmLB1.pack()
        frmLB2.pack()
        frmL.pack(side=LEFT)
        # 右
        frmR = Frame(frm3, bg="#ffffff", width=420, height=500)
        frmR.pack(side=RIGHT)
        frmRT = Frame(frmR, bg="#eaf1f8", width=420, height=225)
        frmRB = Frame(frmR, bg="#cfe8ff", width=420, height=225)
        # 我收到的
        frmRT1 = Frame(frmRT, bg="#c2def6", width=420, height=25)
        Label(frmRT1, text="我收到的", font=('微软雅黑', 10), bg='#cfe8ff',  width=52, anchor=W).pack(side=LEFT)
        frmRT1.pack(side=TOP)
        # 具体内容
        frmRT2 = Frame(frmRT, bg="#eeeeee", width=420, height=200)
        sb = tk.Scrollbar(frmRT2, activerelief="flat",relief="ridge")
        sb.pack(side="right", fill="y")
        global lb
        lb = tk.Listbox(frmRT2, yscrollcommand=sb.set, background='white', relief="flat", font=('微软雅黑', 10, ), width=50, selectbackground="#00a3ff")
        # 查询数据并输出在下拉框里
        lb.pack(side="left", fill="both")
        sb.config(command=lb.yview)
        # 按钮
        frmRT3 = Frame(frmRT, bg="#eeeeee", width=420, height=200)
        button5 = Button(frmRT3, text="同意", relief=FLAT, command=self.deal_ok, font=('微软雅黑', 10), bg='#00a3ff',
                         fg="#ffffff", width=14, height=1)
        button6 = Button(frmRT3, text="拒绝", relief=FLAT, command=self.deal_no, font=('微软雅黑', 10), bg='#00a3ff',
                         fg="#ffffff", width=14, height=1)
        button5.pack(side=LEFT)
        button6.pack(side=RIGHT)
        frmRT2.pack(side=TOP)
        frmRT3.pack()
        frmRT.pack(side=TOP)
        # 我发出的
        frmRB1 = Frame(frmRB, bg="#cfe8ff", width=420, height=40)
        Label(frmRB1, text="我发出的", font=('微软雅黑', 10), bg='#cfe8ff',  width=52, anchor=W).pack(side=LEFT)
        frmRB1.pack(side=TOP)
        # 具体内容
        frmRB2 = Frame(frmRB, bg="#eeeeee", width=420, height=200)
        sb1 = tk.Scrollbar(frmRB2, activerelief="flat", relief="ridge")
        sb1.pack(side="right", fill="y")
        global lb1
        lb1 = tk.Listbox(frmRB2, yscrollcommand=sb1.set, background='white', relief="flat", font=('微软雅黑', 10), width=50)
        # 查询数据并输出在下拉框里
        lb1.pack(side="left", fill="both")
        sb1.config(command=lb.yview)
        frmRB2.pack(side=TOP)
        frmRB.pack()
        frm3.pack(side=TOP)
        self.page.pack()
        self.add_request()

    def modelpage(self):
        #  返回登录界面
        self.page.destroy()
        ModelPage(self.root,username=self.username, account=self.account, password=self.password, email=self.email)

    def repage(self):
        #  返回登录界面
        self.page.destroy()
        LoginPage(self.root)

    def add_request(self):
        global lb
        a = request(account=self.account)
        global users1
        users1 = []
        global users2
        users2 = []
        # 接收到的申请
        users1 = a.select_receive_friend()
        for i in users1:
            if i.get('state')==0:
                lb.insert("end", i.get(
                    'sendname').ljust(25,chr(12288)) + "未处理")
            elif i.get('state')==1:
                lb.insert("end", i.get(
                    'sendname').ljust(25,chr(12288)) + "通过")
            elif i.get('state')==2:
                lb.insert("end", i.get(
                    'sendname').ljust(25,chr(12288)) + "拒绝")
        # 发送的申请
        global lb1
        b = request(account=self.account)
        users2 = b.select_send_friend()
        for i in users2:
            if i.get('state') == 0:
                lb1.insert("end", i.get(
                    'receivename').ljust(25,chr(12288)) + "未处理")
            elif i.get('state') == 1:
                lb1.insert("end", i.get(
                    'receivename').ljust(25,chr(12288)) + "通过")
            elif i.get('state') == 2:
                lb1.insert("end", i.get(
                    'receivename').ljust(25,chr(12288)) + "拒绝")

    def deal_ok(self):
        global lb
        global users1
        temp=0
        try:
            temp = lb.curselection()[0]
            str=users1[temp].get('sendname')
            if users1[temp].get('state')!=0:
                messagebox.showerror("错误", "您已经对此请求做出过回应")
                return
            lb.insert(temp, str.ljust(25,chr(12288)) + "通过")
            lb.delete(temp+1)
            users1[temp]["state"]=1
        except IndexError:
            messagebox.showerror("错误", "未选择")
            return
        a = request(account=users1[temp].get('sendaccount'), receiver_account=self.account, state=1)
        a.deal_request()

    def deal_no(self):
        global lb
        global users1
        temp=0
        try:
            temp = lb.curselection()[0]
            str=users1[temp].get('sendname')
            if users1[temp].get('state')!=0:
                messagebox.showerror("错误", "您已经对此请求做出过回应")
                return
            lb.insert(temp, str.ljust(25,chr(12288)) + "拒绝")
            lb.delete(temp+1)
            users1[temp]["state"] = 2
        except TclError:
            messagebox.showerror("错误", "未选择")
            return
        except IndexError:
            messagebox.showerror("错误", "未选择")
            return
        a = request(account=users1[temp].get('sendaccount'), receiver_account=self.account, state=2)
        a.deal_request()

    def select_user(self):
        global lb2
        global users3
        users3 = []
        lb2.delete(0, END)
        a = user(account=self.select.get())
        #
        users3 = a.select_user()
        # print(users3)
        for i in users3:
            b = friend(account=self.account, friend_account=i['account'])
            temp = b.judge_friend()
            if temp==1:
                lb2.insert("end", i.get('nickname').ljust(8,chr(12288)) + "朋友")
                i['judge']=1
            else:
                if i['account']==self.account:
                    lb2.insert("end", i.get('nickname').ljust(8,chr(12288)) + "我")
                else:
                    lb2.insert("end", i.get('nickname'))
                i['judge'] = 0

    def check_user(self):
        # 查看信息
        global lb2
        global users3
        try:
            temp = lb2.curselection()[0]
            # nickname, account, gender, email
            str1 = users3[temp].get('nickname') + "的个人信息"
            str2 = "账号：" + users3[temp].get('account') + "\n性别：" + users3[temp].get('gender') + "\n邮箱：" + users3[
                temp].get('email')
            messagebox.showinfo(str1, str2)
        except TclError:
            messagebox.showerror("错误", "未选择")
            return
        except IndexError:
            messagebox.showerror("错误", "未选择")
            return

    def send_request(self):
        # 发送请求
        global lb2
        global lb1
        global users3
        try:
            temp = lb2.curselection()[0]
            if users3[temp].get('judge')==1:
                messagebox.showinfo("提示", "你们已经是朋友辣")
                return
            if users3[temp].get('account')==self.account:
                messagebox.showinfo("提示", "这是你自己哦")
                return
            a = request(account=self.account, receiver_account=users3[temp].get('account'))
            b = a.send_request()
            print(b)
            if b==-1:
                lb1.insert("end", users3[temp].get('nickname').ljust(25,chr(12288)) + "未处理")
            elif b==2:
                temp1 = 0
                for i in range(0, lb1.size()):
                    print(lb1.get(i))
                    if lb1.get(i).split(" ", 1)==users3[temp].get('nickname'):
                        temp1 = i
                lb1.insert(temp1, users3[temp].get('nickname').ljust(25,chr(12288)) + "未处理")
                lb1.delete(temp1 + 1)
        except TclError:
            messagebox.showerror("错误", "未选择")
            return
        except IndexError:
            messagebox.showerror("错误", "未选择")
            return

    def me(self):
        # 打开个人信息界面
        top = Toplevel(self.root)
        me(top,self.account)


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