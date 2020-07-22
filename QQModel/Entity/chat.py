import pymysql as pymysql
import time

class chat:
    # 聊天   Chat ( sortID , account , receiver_account , sendName , receiveName , content , date)
    #  sortID,  date  不用给

    def __init__(self, sortID=1, account='', receiver_account='', sendName='', receiveName='', content='', date=''):
        self.sortID = sortID
        self.account = account
        self.receiver_account = receiver_account
        self.sendName = sendName
        self.receiveName = receiveName
        self.content = content
        # 记下当前时间
        self.date = time.strftime('%Y-%m-%d ',time.localtime(time.time()))
        self.db = pymysql.connect("localhost", "root", "Sunbz241290", "qqsimulator")
        self.cursor = self.db.cursor()  # 创建一个游标对象 cursor
        self.select_ID()

    def select_ID(self):
        #   为sortID赋值
        sql = "SELECT max(sortID) FROM chat "
        try:
            self.cursor.execute(sql)
            ID = self.cursor.fetchall()
            self.sortID=ID[0][0]+1
        except:
            self.db.rollback()

    def create_chat(self):
        # 创建对话
        sql = "INSERT INTO chat(sortID , account , receiver_account , sendName , receiveName , content , date) values('"\
              +str(self.sortID) +"','"+self.account+"','" + self.receiver_account+ "','" + self.sendName + "','"+\
              self.receiveName + "','" + str(self.content)+ "','" + self.date+ "')"
        print(sql)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
        self.db.close()

    def get_chat(self):
        # 获取对话   需要知道两人账号
        sql = "SELECT sortID , account , receiver_account , sendName , receiveName , content , date  FROM chat WHERE " \
              "(account ='"+self.account+"' AND receiver_account = '"+self.receiver_account+"') OR ( account ='"\
              +self.receiver_account+"' AND receiver_account = '"+self.account+"') ORDER BY sortID"
        chats = []
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            for r in results:
                temp = {"sortID":0 , "account":'' , "receiver_account":'' , "sendName":'' , "receiveName":'' , "content":'', "date":''}
                temp['sortID'] = r[0]
                temp['account'] = r[1]
                temp['receiver_account'] = r[2]
                temp['sendName'] = r[3]
                temp['receiveName'] = r[4]
                temp['content'] = r[5]
                temp['date'] = r[6]
                chats.append(temp)
        except:
            self.db.rollback()
        self.db.close()
        return chats


# a = chat(account='434696013', receiver_account='256767845')
# users = []
# users = a.get_chat()
# # print(users)
# for i in users:
#     print(i.get('content'))