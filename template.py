import PySimpleGUI as sg

class GUIProgram:
    def __init__(self):
        self.event = None
        self.values = None
        self.layout = None
        self.window = None
        self.title = "GUI app"
        self.running = False
        self.ending = False

    def setup(self):
        self.layout = [
            [sg.Text("Welcome to my GUI app")]
        ]


    def main_loop(self):
        pass

    def run(self):
        self.setup()
        self.running = True
        self.window = sg.Window(self.title, self.layout, element_justification='c')
        while self.running:
            self.event, self.values = self.window.read()
            if self.event == sg.WIN_CLOSED:
                self.running = False
                self.ending = True
            self.main_loop()
        self.window.close()
