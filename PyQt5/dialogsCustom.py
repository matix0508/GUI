import sys
from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
)

class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.setWindowTitle("HELLO")

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Something Happened, is that ok?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.buttonClicked)
        self.setCentralWidget(button)

    def buttonClicked(self, s):
        print("Click", s)

        dlg = CustomDialog(self)
        if dlg.exec_():
            print("Success")
        else:
            print("Cancel")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
