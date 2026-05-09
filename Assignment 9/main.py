import sys
from PySide6.QtWidgets import QApplication
from controller import NameController

app = QApplication(sys.argv)

window = NameController()
window.show()

sys.exit(app.exec())