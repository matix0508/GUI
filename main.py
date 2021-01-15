from login import Login
from menu import Menu
from adding import AddExpense

class Program:
    def __init__(self):
        self.user = None
        self.login = None
        self.menu = None
        self.adding = None

    def run(self):
        self.login = Login()
        self.login.run()
        self.user = self.login.user
        print(self.user)
        self.menu = Menu(self.user)
        self.adding = AddExpense(self.user)
        while True:
            self.menu.run()
            if self.menu.choice == 1:
                self.adding.user = self.user
                self.adding.run()
            if self.menu.choice == 3:
                self.login.user = None
                self.login.run()
                self.user = self.login.user
            end = self.menu.ending or self.adding.ending or self.login.ending
            if end:
                break;


Program().run()
