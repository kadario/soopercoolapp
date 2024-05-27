#IMPORTS:

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import (
    QWidget, 
    QMainWindow, 
    QVBoxLayout,
  )

from src.constants import *
from src.draw_area import DrawArea

#MAIN WINDOW:
"""
In the Main Window we collecting all widgets and layout that will show our application
If we will need to add more elements on the screen, we can always import it here
"""

class MainWindow(QMainWindow):
  def __init__(self, parent = None):
    super(MainWindow, self).__init__(parent)

    self.setWindowTitle("Supercool app!")
    self.setFixedSize(QSize(SCENE_WIDTH, SCENE_HEIGHT))

    layout = QVBoxLayout()
    layout.setContentsMargins(0, 0, 0, 0)
    layout.addWidget(DrawArea(self))
    
    widget = QWidget()
    widget.setLayout(layout)

    self.setCentralWidget(widget)
