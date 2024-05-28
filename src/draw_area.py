#IMPORTS:

from PyQt6.QtCore import Qt, QLineF
from PyQt6.QtGui import QMouseEvent, QBrush, QImage
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsView
from src.constants import *
from src.rectangle_item import RectangleItem


#DRAW AREA CLASS:

class DrawArea(QGraphicsView):
  #INIT:
  
  def __init__(self, parent = None):
    super(DrawArea, self).__init__(parent)
    self.bg_image = QImage('./assets/bg.jpg')

    # Creating scene for drawing elements
    scene = QGraphicsScene()
    scene.setSceneRect(0, 0, SCENE_WIDTH, SCENE_HEIGHT)
    scene.setBackgroundBrush(QBrush(self.bg_image))

    self.setScene(scene)

    self.points = []
    self.connections = []
    self.connectionsDict = {}


  # EVENTS:

  def resizeEvent(self, event):
      self.update_view()

  def showEvent(self, event):
    # Ensure that the update only happens when showing the window
    # programmatically, otherwise it also happen when unminimizing the
    # window or changing virtual desktop
    if not event.spontaneous():
        self.update_view()
    
  def mouseDoubleClickEvent(self, event: QMouseEvent | None):
    if event.button() == Qt.MouseButton.LeftButton:
      #creating rectangle on area
      self.add_new_block(event)
    super().mouseDoubleClickEvent(event)
  
  
  # CUSTOM METHODS:

  def update_view(self):
    scene = self.scene()
    scene_rect = scene.sceneRect()
    self.fitInView(scene_rect, Qt.AspectRatioMode.KeepAspectRatio)

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

    if self.collisions_checker(rectangle):
      self.scene().addItem(rectangle)

  #Check for all collisions before element created
  def collisions_checker(self, rectangle):
    colliding = self.scene().collidingItems(rectangle)

    #get positions for scene and current element
    position_x = rectangle.scenePos().x()
    position_y = rectangle.scenePos().y()
    rect_width = rectangle.rect().width()
    rect_height = rectangle.rect().height()
    # rectangle doesn't have scene yet. so using self:
    scene_width = self.sceneRect().width()
    scene_height = self.sceneRect().height()

    if position_x < 0 or position_x + rect_width > scene_width:
      return False
    if position_y < 0 or position_y + rect_height > scene_height:
      return False
    
    if len(colliding) == 0:
      return True
    else:
      for collider in colliding:
        if collider.type() == 3:
          return False
      return True

  # Adding new line to scene and connect it between two block
  def hello_new_line(self, event,  context_item = None):
    # Adding start and end line points to list
    self.points.append(context_item.pos().x())
    self.points.append(context_item.pos().y())
    self.connections.append(context_item)

    #if all points added we can draw line
    if len(self.points) == 4:
      half_width = context_item.rect().width()/2
      half_height = context_item.rect().height()/2
      
      # Sorry for that mess
      new_line = QLineF(
        self.points[0] + half_width,
        self.points[1] + half_height,
        self.points[2] + half_width,
        self.points[3] + half_height
      )
      
      connection_line = self.scene().addLine(new_line)
      connection_line.setZValue(-1)
      connection_index = len(self.connectionsDict) + 1

      self.connectionsDict[connection_index] = []

      for item in range(len(self.connections)):
        self.connectionsDict[connection_index].append(self.connections[item])
        
        self.connections[item].add_line_connection(connection_line, True if item == 0 else False)
        self.connections[item].set_connection_state(event)
        self.connections[item].set_connection_index(connection_index)
      
      # Clear line data after it was created
      self.clear_points_and_connections()

  # Clear line data after it was created
  def clear_points_and_connections(self):
    self.points = []
    self.connections = []

  def remove_connection_by_index(self, index):
    for rectangle in self.connectionsDict[index]:
      print(rectangle)
      rectangle.remove_line_connection()
    del self.connectionsDict[index]
