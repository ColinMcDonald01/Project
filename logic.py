from PyQt6.QtWidgets import *
from Project1 import *
class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: submit)
        def submit(self):
            try:
                ID = int(self.input_id.text())
            except:
                self.label_2.setText('Invalid ID')
            file = open('IDs.txt', 'r')
            for i in file.readlines():
                if(i==ID):
                    self.label_2.setText('Already Voted')
                else:
                    with open("IDs.txt", "a") as myfile:
                        myfile.write(ID)
                        myfile.write('\n')
                    if(radioButton_1.isChecked()):
                        with open("Votes.txt", "a") as myfile:
                            myfile.write("Jane")
                    if(radioButton_2.isChecked()):
                        with open("Votes.txt", "a") as myfile:
                            myfile.write("John")
                    else:
                        with open("Votes.txt", "a") as myfile:
                            s = self.lineEdit.text()
                            myfile.write(s)
                    y = 0
                    z=0
                    a=0
                    files = open('Votes.txt', 'r')
                    for i in files.readlines():
                        if i =='Jane':
                            y+=1
                        elif i =='John':
                            z+=1
                        else:
                            a+=1
                    self.label_2.setText(f'Jane: {y} John:{z} Other: {a}')
                    input_id.delete(0, 'end')
                    lineEdit.delete(0, 'end')
