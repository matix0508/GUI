from template import GUIProgram, sg



class MyProgram(GUIProgram):
    def __init__(self):
        GUIProgram.__init__(self)

    def save_to_file(self, filename):
        lst = []
        for item in ['expense', 'cost', 'date', 'category']:
            lst.append(self.values[item])
        with open(filename, "a") as file:
            file.write(", ".join(lst))
            file.write("\n")


    def setup(self):
        self.layout = [
            [sg.Text("Add new expense")],
            [sg.Text("Expense: "), sg.Input(key='expense', do_not_clear=False)],
            [sg.Text('Cost: '), sg.Input(key='cost', do_not_clear=False)],
            [sg.Text('Date: '), sg.Input(key='date', do_not_clear=False)],
            [sg.Text('Category'), sg.Input(key='category', do_not_clear=False)],
            [sg.Button('Submit', bind_return_key=True)]
        ]
        self.title = "Expenses"

    def main_loop(self):
        while True:
            self.event, self.values = self.window.read()
            if self.event == sg.WIN_CLOSED:
                break

            if self.event == 'Submit':
                self.save_to_file('mfile.txt')

p = MyProgram()
p.run()
