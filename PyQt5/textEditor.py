from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QAction,
                            QFileDialog, QApplication)
from PyQt5.QtGui import QIcon, QKeySequence, QFont
import sys
from pathlib import Path

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.fname = None

        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        saveFile = QAction(QIcon('save.png'), 'Save', self)
        saveFile.setShortcut('Ctrl+S')
        saveFile.setStatusTip('Save the file')
        saveFile.triggered.connect(self.saveChanges)

        saveAs = QAction(QIcon('save.png'), 'Save As', self)
        saveAs.setStatusTip("Save the copy in some location")
        saveAs.triggered.connect(self.saveAs)


        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)
        fileMenu.addAction(saveAs)

        self.bold_action = QAction(QIcon('bold.png'), 'Bold', self)
        self.bold_action.setShortcut(QKeySequence.Bold)
        self.bold_action.setCheckable(True)
        self.bold_action.toggled.connect(lambda x: self.textEdit.setFontWeight(QFont.Bold if x else QFont.Normal))

        editMenu = menubar.addMenu('&Edit')
        editMenu.addAction(self.bold_action)

        self.setGeometry(300, 300, 550, 450)
        self.setWindowTitle('File dialog')
        self.show()


    def showDialog(self):
        home_dir = str(Path.home())
        self.fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir)

        if self.fname[0]:
            self.setWindowTitle(self.fname[0])
            with open(self.fname[0], 'r') as f:
                data = f.read()
                self.textEdit.setText(data)

    def saveChanges(self):
        if not self.fname:
            self.fname = QFileDialog.getSaveFileName(self, 'Choose Location', str(Path.home()))
        if self.fname[0]:
            self.setWindowTitle(self.fname[0])
            with open(self.fname[0], 'w') as f:
                f.write(self.textEdit.toPlainText())

    def saveAs(self):
        self.fname = QFileDialog.getSaveFileName(self, 'Choose Location', str(Path.home()))

        if self.fname[0]:
            self.setWindowTitle(self.fname[0])
            with open(self.fname[0], 'w') as f:
                f.write(self.textEdit.toPlainText())



def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

main()
