import pymysql as pymysql

from QQModel.Entity.friend import friend


class request:
    # 请求  Request (account,receiver_account, state)
    # state为0表示未处理，1表示同意，2表示拒绝

    def __init__(self, account='', receiver_account='', state=0):
        self.account = account
        self.receiver_account = receiver_account
        self.state = state
        self.db = pymysql.connect("localhost", "root", "Sunbz241290", "qqsimulator")
        self.cursor = self.db.cursor()  # 创建一个游标对象 cursor

    def send_request(self):
        # 创建申请 -1表示原来没有 0表示未处理，1表示同意，2表示拒绝
        self.check_request()
        if self.state==-1:
            sql = "INSERT INTO Request(account,receiver_account, state) values('" + str(self.account) + "','" \
                  + str(self.receiver_account) + "',0) "
        elif self.state==0:
            return self.state
        elif self.state==1:
            return self.state
        elif self.state==2:
            sql = "UPDATE Request  set state = 0 " + "  WHERE receiver_account = '" + self.receiver_account + "' " + \
                  " AND account = '" + self.account + "'"
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
        self.db.close()
        return self.state

    def check_request(self):
        # 查看申请状态，是无申请还是怎样
        sql = "SELECT state FROM Request WHERE receiver_account = '"+self.receiver_account+"' "+\
              " AND account = '"+self.account+"'"
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            if results == ():
                self.state = -1
                return
            for r in results:
                self.state = r[0]
        except:
            self.db.rollback()

    def select_send_friend(self):
        # 查看发送的申请   为account赋值
        sql = "SELECT  sendname, receivename, sendaccount, receiveaccount, state FROM V_Request_User WHERE sendaccount = '"+ self.account+"' "
        requests = []
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            for r in results:
                temp = {'sendname': "",'receivename': "",'sendaccount': "",'receiveaccount': "",'state': 0}
                temp['sendname'] = r[0]
                temp['receivename'] = r[1]
                temp['sendaccount'] = r[2]
                temp['receiveaccount'] = r[3]
                temp['state'] = r[4]
                requests.append(temp)
        except:
            self.db.rollback()
        self.db.close()
        return requests

    def select_receive_friend(self):
        # 查看收到的的申请    为account赋值
        sql = "SELECT  sendname, receivename, sendaccount, receiveaccount, state FROM V_Request_User WHERE receiveaccount = '"+ self.account+"' "
        requests = []
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            for r in results:
                temp = {'sendname': "",'receivename': "",'sendaccount': "",'receiveaccount': "",'state': 0}
                temp['sendname'] = r[0]
                temp['receivename'] = r[1]
                temp['sendaccount'] = r[2]
                temp['receiveaccount'] = r[3]
                temp['state'] = r[4]
                requests.append(temp)
        except:
            self.db.rollback()
        self.db.close()
        return requests

    def deal_request(self):
        # 处理申请
        # 申请得到同意后，系统会自动成功添加好友state置为1。
        # 申请得到拒绝后， state置为2，不执行操作
        sql = "UPDATE  request SET state = "+str(self.state)+"  WHERE receiver_account = '"+self.receiver_account+"' "+" AND account = '"+self.account+"'"
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
        self.db.close()
        if(self.state==1):
            a = friend(account=self.account, friend_account=self.receiver_account)
            a.create_friend()

# a = request(account="256767845")
# users = []
# users = a.select_send_friend()
# print(users)
# for i in users:
#     print(i.get('sendname'))