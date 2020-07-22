import string
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import threading
from PIL import Image, ImageTk

# from QQModel.Interface.friend import FriendPage
from QQModel.Entity.chat import chat
from QQModel.Entity.friend import friend
from QQModel.Entity.user import user
# from QQModel.Interface.friend import FriendPage
from QQModel.Interface.login import LoginPage

# #eaf1f8经典灰
from QQModel.Interface.me import me


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
        self.password0 = password  # 密码
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

    # def friendpage(self):
    #     #  返回朋友界面
    #     self.page.destroy()
    #     FriendPage(self.root, username=self.username, account=self.account, password=self.password, email=self.email)

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
        # print("c",templist)
        mvp = self.maxlength(templist)
        for i in templist:
            chattext.insert("end", " ".ljust(2, "*"),"tag_3")
            chattext.insert("end", i.ljust(int(self.chinalength(i,mvp)), '-'), "tag_1")
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


# root = Tk()
# ModelPage(root,account="256767845",username="至高广播")
# root.mainloop()