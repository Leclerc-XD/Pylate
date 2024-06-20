# Imports
# PyQt5 Framework ~ QtCore, QtWidgets, QtGui
from languages import keys,values
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QComboBox, QTextEdit
from PyQt5.QtGui import QFont, QFontDatabase
# 

class TranslatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.settings()
        self.initUI()
        
    def settings(self):
        self.resize(500,400)
        self.setWindowTitle('PyRush')
        
        
    # Events
    def click_events(self):
        pass
    
    

    # Design
    def initUI(self):
        #Widgets
        self.title = QLabel("P̴̛̟̯̰̣̼̦̞͚͝͝ỷ̷̡̛̻̥͚̅̍͌͠Ļ̵̢̠͖̬̫̣͖́̿̓̀̉̒̌͝ȧ̸̻͖̭̉̍̄̒̀͌̌͊̄ť̷̢̧̞̬̣̖̮̼̆̒̎̓́̎́͝è̶̡̨̜͇̜̹̳͇̓͑͜")
        self.inputbox = QComboBox()
        self.outputbox = QComboBox()
        self.translatebutton = QPushButton("Translate")
        self.speakbutton = QPushButton("Speak")
        self.resetbutton = QPushButton("Reset")

        self.textinput = QTextEdit()
        self.reversebutton = QPushButton("Reverse")
        self.textoutput = QTextEdit()
        
        self.inputbox.addItems(values)
        self.outputbox.addItems(values)
        #Layouts
        self.master_layout = QHBoxLayout()
        self.layout1 = QVBoxLayout()
        self.layout2 = QVBoxLayout()


        #Add Widgets to layout
        self.layout1.addWidget(self.title)
        self.layout1.addWidget(self.inputbox)
        self.layout1.addWidget(self.outputbox)
        self.layout1.addWidget(self.translatebutton)
        self.layout1.addWidget(self.speakbutton)
        self.layout1.addWidget(self.resetbutton)

        self.layout2.addWidget(self.textinput)
        self.layout2.addWidget(self.reversebutton)
        self.layout2.addWidget(self.textoutput)

        self.master_layout.addLayout(self.layout1, 35)
        self.master_layout.addLayout(self.layout2, 65)
        self.setLayout(self.master_layout)

        #CSS
        self.setStyleSheet("""
                            QWidget{
                                background-color: #ADD8E6;
                            }

                            QLabel{
                                color:blue;
                                font-size: 60px;
                                
                            }
                            QPushButton:hover{
                                background-color:blue;
                                border: 1px solid #000;
                            }
                                
                                
                                
                                
                                """)
    
    # Google Translation
    
    
    # Take Translation & Put it on the Screen
    
    
    
    # Reset the App
    
    
    


if __name__ == "__main__":
    app = QApplication([])
    window = TranslatorApp()
    window.show()
    app.exec_()