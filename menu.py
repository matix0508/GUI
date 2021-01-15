from template import GUIProgram, sg

class Menu(GUIProgram):
    def __init__(self, user):
        GUIProgram.__init__(self)
        self.user = user
        self.choice = None


    def setup(self):
        self.layout = [
            [sg.Text("Hello "+ str(self.user))],
            [sg.Button("Add Expense")],
            [sg.Button('View(Edit) your Expenses')],
            [sg.Button('Logout')]
        ]
        self.title = "Menu"

    def main_loop(self):
        if self.event == 'Add Expense':
            self.choice = 1
            self.running = False
        if self.event == 'Logout':
            self.choice = 3
            self.running = False
