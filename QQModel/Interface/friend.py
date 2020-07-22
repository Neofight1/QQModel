import tkinter as tk
from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk

from QQModel.Entity.friend import friend
from QQModel.Entity.request import request
from QQModel.Entity.user import user
from QQModel.Interface.login import LoginPage

# #eaf1f8经典灰
# 初始界面
from QQModel.Interface.me import me
from QQModel.Interface.model import ModelPage


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


# root = Tk()
# FriendPage(root,account="256767845")
# root.mainloop()