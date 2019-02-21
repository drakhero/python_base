from pymysql import *
class MysqlPython():
    def __init__(self,database,
                     host="localhost",
                     user="root",
                     password="123456",
                     charset="utf8",
                     port=3306):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
        self.port = port

    def open(self):
        self.coon = connect(host=self.host,
                            user=self.user,
                            password=self.password,
                            database=self.database,
                            charset=self.charset,
                            port=self.port)

        self.cursor = self.coon.cursor()

    def close(self):
        self.coon.close()
        self.cursor.close()

    def execute(self,sql,L=[]):
        self.open()
        try:
            self.cursor.execute(sql,L)
            self.coon.commit()
        except Exception:
            self.coon.rollback()
        self.close()

    def All(self,sql,L=[]):
        self.open()
        self.cursor.execute(sql,L)
        result = self.cursor.fetchall()
        self.close()
        return result








