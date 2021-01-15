from template import GUIProgram, sg
from database import Database
from user import User

def get_credentials():
    with open("passy", "r") as file:
        output = file.read().split("\n")
        output = output[:-1]
    return output


def get_users():
    output = []
    credentials = get_credentials()
    budget = Database(
        host=credentials[0],
        user=credentials[1],
        password=credentials[2],
        db_name=credentials[3],
        port=int(credentials[4])
    )

    for id, login, password, name, level in budget.select("SELECT UserID, login, password, name, level from users"):
        output.append(User(login, password, id, name, level))
        print(password)
    return output

class Login(GUIProgram):
    def __init__(self):
        GUIProgram.__init__(self)
        self.users = []
        self.user = None


    def setup(self):
        self.users = get_users()

        self.layout = [
            [sg.Text(size=(40,1), key='-OUTPUT-')],
            [sg.Text("login: "), sg.Input(key="-LOGIN-")],
            [sg.Text("password: "), sg.Input(key='-PASS-', password_char="*", do_not_clear=False)],
            [sg.Button("Submit", bind_return_key=True)]
        ]
        self.title = 'Login'

    def login(self, login, password):
        for u in self.users:
            if u.login == login and u.password == password:
                self.user = u
        if not self.user:
            self.window['-OUTPUT-'].update("Wrong login or password!")

                # self.layout = [
                #     [sg.Text("ID: "), sg.Text(str(u.id))],
                #     [sg.Text("Login: "), sg.Text(u.login)],
                #     [sg.Text("Name: "), sg.Text(u.name)],
                #     [sg.Text("Level: "), sg.Text(str(u.level))],
                #     [sg.Button("Logout"), sg.Button("Change Data")]
                # ]
                # self.window.close()
                # self.window = sg.Window(login, self.layout)

    def main_loop(self):
        if not self.user:
            if self.values['-LOGIN-']:
                self.login(self.values['-LOGIN-'], self.values['-PASS-'])

        if self.user:
            self.running = False
