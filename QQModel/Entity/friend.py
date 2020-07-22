import pymysql as pymysql

class friend:
    # 朋友

    def __init__(self, account='', friend_account=''):
        self.account = account
        self.friend_account = friend_account
        self.db = pymysql.connect("localhost", "root", "Sunbz241290", "qqsimulator")
        self.cursor = self.db.cursor()  # 创建一个游标对象 cursor

    def create_friend(self):
        # 创建朋友
        sql = "INSERT INTO friend(account, friend_account) values('"+str(self.account) +"','"+str(self.friend_account)+"')  "
        sql += ", ('" + str(self.friend_account) + "','" + str(
            self.account) + "')"
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
        self.db.close()

    def delete_friend(self):
        # 删除朋友
        sql = "DELETE FROM friend WHERE account = '%s' " % self.account+" AND friend_account = '%s'" % self.friend_account
        sql += "   DELETE FROM friend WHERE account = '%s' " % self.friend_account+" AND friend_account = '%s'" % self.account
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
        self.db.close()

    def select_friend(self):
        # 搜索朋友
        sql = "SELECT friend_account  FROM friend WHERE account ='"+self.account+"'"
        friend_account = []
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            for r in results:
                temp = {'account': ""}
                temp['account'] = r[0]
                friend_account.append(temp)
        except:
            self.db.rollback()
        self.db.close()
        return friend_account

    def judge_friend(self):
        # 判断是否是朋友  1为真，0为假
        sql = "SELECT *  FROM friend WHERE account ='"+self.account+"' AND friend_account='"+self.friend_account+"'"
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            if results!=():
                return 1
        except:
            self.db.rollback()
        self.db.close()
        return 0

# a = friend(account="342567451", friend_account="256767845")

# users = []
# users = a.judge_friend()
# print(users)
# for i in users:
#     print(i.get('nickname'))