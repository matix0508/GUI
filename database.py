import mysql.connector

class Database:
    def __init__(self, host, user, password, db_name, port):
        self.host = host
        self.user = user
        self.password = password
        self.name = db_name
        self.port = port
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.name,
                port=self.port
            )
            self.cursor = self.connection.cursor()
        except:
            raise Exception("Can't do that")

    def select(self, sql):
        if not self.connection:
            self.connect()

        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def insert(self, sql):
        if not self.connection:
            self.connect()

        self.cursor.execute(sql)
        self.connection.commit()
