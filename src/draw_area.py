#IMPORTS:

from src.constants import *
from src.rectangle_item import RectangleItem
from src.connection_line import ConnectionLine

from PyQt6.QtCore import Qt
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


#DRAW AREA CLASS:

class DrawArea(QGraphicsView):
  startItem = newConnection = None
  
  #INIT:
  
  def __init__(self, parent = None):
    super(DrawArea, self).__init__(parent)
    self.bg_image = QImage('./assets/bg.jpg')

    # Creating scene for drawing elements
    scene = QGraphicsScene()
    scene.setSceneRect(0, 0, SCENE_WIDTH, SCENE_HEIGHT)
    scene.setBackgroundBrush(QBrush(self.bg_image))

    self.setScene(scene)

    self.connection_status = False
    self.connections = []
    self.connectionsDict = {}

    self.ctrl = False


  # EVENTS:

  def resizeEvent(self, event):
      self.update_view()

  def showEvent(self, event):
    # Ensure that the update only happens when showing the window
    # programmatically, otherwise it also happen when unminimizing the
    # window or changing virtual desktop
    if not event.spontaneous():
        self.update_view()
  
  def keyPressEvent(self, event: QKeyEvent | None) -> None:
        if event.key() == Qt.Key.Key_Control:
          self.ctrl = True
        return super().keyPressEvent(event)

  def keyReleaseEvent(self, event: QKeyEvent | None) -> None:
        if event.key() == Qt.Key.Key_Control:
          self.ctrl = False
        return super().keyPressEvent(event)
  
  def mousePressEvent(self, event):
    if event.button() == Qt.MouseButton.RightButton:
      self.connections_updater(event)

    super().mousePressEvent(event)
    
  def mouseDoubleClickEvent(self, event: QMouseEvent | None):
    if event.button() == Qt.MouseButton.LeftButton:
      #creating rectangle on area
      self.add_new_block(event)

    super().mouseDoubleClickEvent(event)

  def mouseMoveEvent(self, event):
    if self.newConnection:
        item = self.check_connection_area(event.scenePosition())
        if (item and item != self.startItem and
            self.startItem.onLeft != item.onLeft):
                point_2 = item.scenePos()
        else:
            point_2 = event.scenePosition()
        self.newConnection.setP2(point_2)
        return
    super().mouseMoveEvent(event)

  
  # CUSTOM METHODS:

  def connections_updater(self, event):
    item = self.check_connection_area(event.scenePosition())
    
    if self.ctrl:
      collided = item.collidingItems()
      for collider in collided:
        if isinstance(collider, ConnectionLine):
          self.scene().removeItem(collider)
    else:
      if item and not self.connection_status:
          item.set_connection_state(True)
          self.connection_status = True
          self.startItem = item

          self.newConnection = ConnectionLine(item, event.scenePosition())
          self.scene().addItem(self.newConnection)
      elif item and self.connection_status:
        self.connection_status = False

        if self.newConnection:
          item_next = self.check_connection_area(event.scenePosition())
          
          if item_next and item_next != self.startItem:
            self.newConnection.setEnd(item)

            if self.startItem.add_line(self.newConnection):
              item_next.add_line(self.newConnection)
            else:
              self.startItem.set_connection_state(False)
              self.startItem.remove_line(self.newConnection)
              self.scene().removeItem(self.newConnection)
          else:
              self.startItem.set_connection_state(False)
              self.startItem.remove_line(self.newConnection)
              self.scene().removeItem(self.newConnection)
        self.startItem.set_connection_state(False)
        self.startItem = self.newConnection = None

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
    
    rectangle = RectangleItem(0, 0, BOX_WIDTH, BOX_HEIGHT)
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

  #Check is we have connections on clicked item block
  def check_connection_area(self, pos):
    for item in self.scene().items(pos):
      if isinstance(item, RectangleItem):
        return item