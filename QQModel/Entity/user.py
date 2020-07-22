import pymysql as pymysql
import cryptography


class user:
    # 用户

    def __init__(self, name='', nickname='', gender='', account='', email='', password=''):
        self.name = name
        self.nickname = nickname
        self.gender = gender
        self.account = account
        self.email = email
        self.password = password
        self.db = pymysql.connect("localhost", "root", "Sunbz241290", "qqsimulator")
        self.cursor = self.db.cursor()  # 创建一个游标对象 cursor

    def select_for_account(self):
        # 查重account   返回0说明重复，1说明不重复
        sql = "SELECT name FROM user WHERE account = '%s' " % self.account
        try:
            self.cursor.execute(sql)
            self.db.commit()
            results = self.cursor.fetchall()
            for r in results:
                t_name = r[0]
                if t_name != "":
                    print(t_name)
                    return 0
        except:
            self.db.rollback()
        self.db.close()
        return 1

    def login_check(self):
        # 登录校验  返回0为没有此帐号，1为校验成功，2为密码错误
        print(self.account)
        sql = "SELECT password FROM user WHERE account = '%s' " % self.account
        try:
            self.cursor.execute(sql)
            self.db.commit()
            results = self.cursor.fetchall()
            t_password = ''
            for r in results:
                t_password = r[0]
            if t_password == "":
                return 0
            elif t_password == self.password:
                return 1
            else:
                return 2
        except:
            self.db.rollback()
        self.db.close()
        return 1

    def create_user(self):
        # 创建帐户  1为操作成功，0为操作失败  User (name, nickname, gender, account, email, password)
        sql = "INSERT INTO user(name, nickname, gender, account, email, password) values('"+str(self.name) +\
              "','"+str(self.nickname)+"','"+str(self.gender)+"','"+str(self.account)+"','"\
              + str(self.email)+"','"+str(self.password)+"')"
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
            return 0
        self.db.close()
        return 1

    def get_user(self):
        # 获取用户信息
        sql = "SELECT name, nickname, gender, account, email, password FROM user WHERE account = '"+self.account+"' "
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            for r in results:
                self.name = r[0]
                self.nickname = r[1]
                self.gender = r[2]
                self.account = r[3]
                self.email = r[4]
                self.password = r[5]
        except:
            self.db.rollback()
        self.db.close()
        return self

    def set_user(self):
        # 更新用户信息
        sql = "UPDATE user SET name='"+self.name+"' , nickname='"+self.nickname+"', gender='"+self.gender+"', email='"+self.email+"', password='"+self.password+"' WHERE account = '%s' " % self.account
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
            return 0
        self.db.close()
        return 1

    def select_user(self):
        # 搜索用户  根据昵称（模糊查询）或者账号可以搜索用户   结果返回一个集合
        sql = "SELECT DISTINCT nickname, account, gender, email  FROM user WHERE account LIKE '%"+str(self.account)+"%' or nickname LIKE '%"+str(self.account)+"%'"
        users = []
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            for r in results:
                temp = {'nickname': "", 'account': "",'gender':"", 'email':""}
                temp['nickname'] = r[0]
                temp['account'] = r[1]
                temp['gender'] = r[2]
                temp['email'] = r[3]
                users.append(temp)
        except:
            self.db.rollback()
        self.db.close()
        return users

# a = user(account="4", nickname="4")
# users = []
# users = a.select_user()
# print(users)

