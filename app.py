#IMPORTS:

import sys

from PyQt6.QtWidgets import QApplication
from src.main import MainWindow


#RUN APP FUNCTION:

"""
Main function that running our 'Supercool' app
"""
def run():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

run()