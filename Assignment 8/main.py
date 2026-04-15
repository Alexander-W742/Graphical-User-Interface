import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ans8_ui import Ui_root

class MainWindow(QMainWindow):
    def __inti__(self):
        super().__inti__()

        self.ui = Ui_root()
        self.ui.setupUi(self)

        # Connect buttons
        self.ui.btnS.clicked.connect(self.submit)
        self.ui.btnR.clicked.connect(self.reset)
        self.ui.btnQ.clicked.connect(self.quit_app)

    def submit(self):
        first = self.ui.entFirst.text()
        last = self.ui.entLast.text()
        email = self.ui.entEmail()
        phone = self.ui.entPhone.text()

        # Validation
        if first == "" or last == "":
            QMessageBox.warning(self, "Error", "First and Last Name are required!")
            return
        
        # Display data
        message = f"""
First Name: {first}
Last Name: {last}
Email: {email}
Phone: {phone}
"""
        QMessageBox.information(self, "Submitted Data", message)

    def reset(self):
        self.ui.entFirst.clear()
        self.ui.entLast.clear()
        self.ui.entEmail.clear()
        self.ui.entPhone.clear()

    def quit_app(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())