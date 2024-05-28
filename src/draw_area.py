#IMPORTS:

from PyQt6.QtCore import QSize, Qt, QEvent, QRectF, QPointF, QPoint, QSizeF, QLineF
from PyQt6.QtGui import (
    QIcon,
    QKeyEvent,
    QMouseEvent,
    QMoveEvent,
    QPaintEngine,
    QPaintEvent,
    QPainter, 
    QPainterPath, 
    QPen,
    QBrush,
    QColor,
    QPalette,
    QPixmap
  )

from PyQt6.QtWidgets import (
    QApplication,
    QGraphicsSceneDragDropEvent,
    QGraphicsSceneHoverEvent,
    QGraphicsSceneMouseEvent,
    QStyleOptionGraphicsItem, 
    QWidget,
    QMainWindow,
    QPushButton,
    QGraphicsScene,
    QGraphicsView,
    QGraphicsRectItem,
    QGridLayout,
    QVBoxLayout,
    QGraphicsItem,
    QLayout,
    QLabel,
    QGraphicsEllipseItem,
    QGraphicsLineItem

  )

from src.constants import *
from src.rectangle_item import RectangleItem


#DRAW AREA CLASS:

class DrawArea(QGraphicsView):
  #INIT:
  
  def __init__(self, parent = None):
    super(DrawArea, self).__init__(parent)

    # Creating scene for drawing elements
    scene = QGraphicsScene()
    scene.setSceneRect(0, 0, SCENE_WIDTH, SCENE_HEIGHT)

    scene.setBackgroundBrush(QColor(185, 222, 126))

    self.setScene(scene)
    # self.fitInView(QRectF(self.scene().sceneRect()))
    print(scene.sceneRect())


    self.points = []
    self.connections = []
  
  
  # EVENTS:

  def updateView(self):
    scene = self.scene()
    r = scene.sceneRect()
    print('rect %d %d %d %d' % (r.x(), r.y(), r.width(), r.height()))
    self.fitInView(r, Qt.AspectRatioMode.KeepAspectRatio)

  def resizeEvent(self, event):
      print('resize event start')
      self.updateView()
      print('resize event end')

  def showEvent(self, event):
      # ensure that the update only happens when showing the window
      # programmatically, otherwise it also happen when unminimizing the
      # window or changing virtual desktop
      if not event.spontaneous():
          print('show event')
          self.updateView()
    
  def mouseDoubleClickEvent(self, event: QMouseEvent | None):
    if event.button() == Qt.MouseButton.LeftButton:
      self.add_new_block(event)
    super().mouseDoubleClickEvent(event)
  
  
  # CUSTOM METHODS:

  #Creating and adding block to scene
  def add_new_block(self, event: QMouseEvent | None):
    #check if item on same position
    item = self.itemAt(event.pos())
    
    if item:
      return super().mousePressEvent(event)
    
    mouse_position = self.mapToScene(event.pos())
    
    box_center_x = mouse_position.x() - BOX_WIDTH/2
    box_center_y = mouse_position.y() - BOX_HEIGHT/2
    
    rectangle = RectangleItem(0, 0, BOX_WIDTH, BOX_HEIGHT, self)
    rectangle.setPos(box_center_x, box_center_y)

    self.scene().addItem(rectangle)

  # Adding new line to scene and connect it between two block
  def hello_new_line(self, context_item = None):
    # Adding start and end line points to list 
    self.points.append(context_item.pos().x())
    self.points.append(context_item.pos().y())
    self.connections.append(context_item)

    #if all points added we can draw line
    if len(self.points) == 4:
      connection_line = self.scene().addLine(QLineF(
        self.points[0] + BOX_WIDTH/2, 
        self.points[1] + BOX_HEIGHT/2, 
        self.points[2] + BOX_WIDTH/2, 
        self.points[3] + BOX_HEIGHT/2
      ))

      connection_line.setZValue(-1)

      for item in range(len(self.connections)):
        self.connections[item].add_line(connection_line, True if item == 0 else False)
        self.connections[item].set_connection_state()
      
      # Clear line data after it was created
      self.clear_points_and_connections()

  # Clear line data after it was created
  def clear_points_and_connections(self):
    self.points = []
    self.connections = []