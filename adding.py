from template import GUIProgram, sg



class AddExpense(GUIProgram):
    def __init__(self, user):
        GUIProgram.__init__(self)
        self.user = user

    def save_to_file(self, filename):
        lst = []
        for item in ['expense', 'cost', 'date', 'category']:
            lst.append(self.values[item])
        with open(filename, "a") as file:
            if self.user:
                file.write(str(self.user) + ':\t')
            file.write(", ".join(lst))
            file.write("\n")


    def setup(self):
        self.layout = [
            [sg.Text("Add new expense")],
            [sg.Text("Expense: "), sg.Input(key='expense', do_not_clear=False)],
            [sg.Text('Cost: '), sg.Input(key='cost', do_not_clear=False)],
            [sg.Text('Date: '), sg.Input(key='date', do_not_clear=False)],
            [sg.Text('Category'), sg.Input(key='category', do_not_clear=False)],
            [sg.Button('Confirm and Continue', bind_return_key=True), sg.Button('Confirm')]
        ]
        self.title = "Expenses"

    def main_loop(self):
        if self.event == 'Confirm':
            self.save_to_file('mfile.txt')
            self.running = False
        if self.event == 'Confirm and Continue':
            self.save_to_file('mfile.txt')
