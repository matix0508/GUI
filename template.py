import PySimpleGUI as sg

class GUIProgram:
    def __init__(self):
        self.event = None
        self.values = None
        self.layout = None
        self.window = None
        self.title = "GUI app"

    def setup(self):
        self.layout = [
            [sg.Text("Welcome to my GUI app")],
            [],
            []
        ]


    def main_loop(self):
        while True:
            self.event, self.values = self.window.read()
            if self.event == sg.WIN_CLOSED:
                break
        self.window.close()

    def run(self):
        self.setup()
        self.window = sg.Window(self.title, self.layout)
        self.main_loop()
