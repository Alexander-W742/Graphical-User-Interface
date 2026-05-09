from PySide6.QtWidgets import QMainWindow
from view import Ui_NameFormater
from model import NameModel

class NameController(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_NameFormater()
        self.ui.setupUi(self)

        self.model = NameModel()

        # Connect buttons to methods
        self.ui.capitalizeButton.clicked.connect(self.capitalize_text)
        self.ui.reverseButton.clicked.connect(self.reverse_text)
    
    def capitalize_text(self):
        text = self.ui.inputLineEdit.text()

        result = self.model.capitalize_text(text)

        self.ui.outputLabel.setText(result)
    
    def reverse_text(self):
         text = self.ui.inputLineEdit.text()

         result = self.model.reverse_text(text)

         self.ui.outputLabel.setText(result)