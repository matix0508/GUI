from database import Database
class User:
    def __init__(self,login, password=None, id=None, name=None, level=None):
        self.id = id
        self.name = name
        self.login = login
        self.password = password
        self.level = level

    def __repr__(self):
        return f"user: {self.login}"
