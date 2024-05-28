#IMPORTS:

import random

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
    QPolygonF, 
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


#RECTANGLE BOX CLASS:

class RectangleItem(QGraphicsRectItem):
  #INIT:

  def __init__(self, x, y, width, height, parent):
    super().__init__(x, y, width, height)
    
    brush = QBrush(QColor(*[random.randint(0, 255) for _ in range(3)]))

    self.setBrush(brush)
    self.setAcceptDrops(True)
    self.setAcceptHoverEvents(True)
    self.setCursor(Qt.CursorShape.OpenHandCursor) 
    self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
    self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
    self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsFocusable)
    self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemSendsGeometryChanges)
    self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemSendsScenePositionChanges)

    #PROPERTIES:
    
    self.connection_status = False
    self.parent = parent
    self.line = None
    self.isPoint = None
    self.connection_index = None

  #EVENTS:

  def itemChange(self, change , value):
    if change == QGraphicsItem.GraphicsItemChange.ItemPositionChange and self.scene():
      self.move_connection_to_center()
      
      newPos = value
      rectScene = self.scene().sceneRect()

      if not rectScene.contains(newPos) :
        #Keep the item inside the scene rect.
        newPos.setX(min(rectScene.right() - self.rect().width(), max(newPos.x(), rectScene.left())))
        newPos.setY(min(rectScene.bottom() - self.rect().height(), max(newPos.y(), rectScene.top())))
        
        return newPos

    return super(RectangleItem, self).itemChange(change, value)
  
  def mouseMoveEvent(self, event):
    super().mouseMoveEvent(event)
    self.offset_position_check()
    
    colliding = self.collidingItems()

    if len(colliding) > 0:
      self.check_collisions(event)

  def mousePressEvent(self, event: QGraphicsSceneMouseEvent | None) -> None:
    self.setZValue(1)

    if event.button() == Qt.MouseButton.RightButton:
      if self.line == None:
        self.set_connection_state(event)
      else:
        self.parent.remove_connection_by_index(self.connection_index)
        self.scene().removeItem(self.line)
        self.remove_line_connection()
      
    return super().mousePressEvent(event)
  
  def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent | None) -> None:
    super().mouseReleaseEvent(event)
    self.offset_position_check()
    
    colliding = self.collidingItems()

    if len(colliding) > 0:
      self.check_collisions(event)


  #CUSTOM METHODS:

  def add_line_connection(self, line, ispoint):
    self.line = line
    self.isPoint = ispoint
  
  def remove_line_connection(self):
    if self.line:
      self.scene().removeItem(self.line)
    self.line = None
    self.isPoint = None
  
  def set_connection_index(self, index):
    self.connection_index = index
  
  # Change state of the selected block while connection with another my lines
  def set_connection_state(self, event):
    if self.connection_status == False:
      self.connection_status = True
      self.setCursor(Qt.CursorShape.ArrowCursor) 
      self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, False)
      self.setOpacity(0.5)
      self.parent.hello_new_line(event, self)

    else:
      self.connection_status = False
      self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, True)
      self.setCursor(Qt.CursorShape.OpenHandCursor) 
      self.setOpacity(1)

  # Redraw line connected to block when block position updated
  def move_connection_to_center(self):
    if self.line != None:
      position_x = self.sceneBoundingRect().x() + self.rect().width()/2
      position_y = self.sceneBoundingRect().y() + self.rect().height()/2

      newCenterPos = QPointF(position_x, position_y)

      point_1 = newCenterPos if self.isPoint else self.line.line().p1()
      point_2 = self.line.line().p2() if self.isPoint else newCenterPos

      self.line.setLine(QLineF(point_1, point_2))
  
  # Move block to new position if it overlaps another
  def check_collisions(self, event: QGraphicsSceneMouseEvent | None):
    self.setZValue(0)

    collisions = self.collidingItems()

    if len(collisions) > 0:
      for collision in range(len(collisions)):
        if collisions[collision].type() == 3:
          
          collider = collisions[collision]
          
          # Get coordinates of centers of two blocks
          selfCenterX = self.pos().x() + self.rect().width() / 2
          selfCenterY = self.pos().y() + self.rect().height() / 2
          collideCenterX = collider.pos().x() + collider.rect().width() / 2
          colliderCenterY = collider.pos().y() + collider.rect().height() / 2
          
          # creating line between two centers to check cos
          line_central_position_1 = QPointF(collideCenterX, colliderCenterY)
          line_central_position_2 = QPointF(selfCenterX, selfCenterY)

          line = QLineF(line_central_position_1, line_central_position_2)

          # get Cosinus of angle between line and horisontal line
          cos = (collider.rect().width()/2 / line.length()) if line.length() > 0 else 0
          
          # Check cosinus value to know which side our block closer to
          # And put our block to new position
          if cos > 0.4 and cos < 0.7 :
            if self.pos().x() > collideCenterX:
              self.setX(collider.pos().x() + collider.rect().width())
            else:
              self.setX(collider.pos().x() - collider.rect().width())
          else:
            if self.pos().y() > colliderCenterY:
              self.setY(collider.pos().y() + collider.rect().height())
            else:
              self.setY(collider.pos().y() - collider.rect().height())
          
      collisions = self.collidingItems()

      #Check if our block not moving out of the scene
  def offset_position_check(self):
    #Check X axis
    if self.pos().x() < 0:
      self.setX(0)
    elif self.pos().x() + self.rect().width() > self.scene().sceneRect().width():
      self.setX(self.scene().sceneRect().width() - self.rect().width())

    #Check Y axis
    if self.pos().y() < 0:
      self.setY(0)
    elif self.pos().y() + self.rect().height() > self.scene().sceneRect().height():
      self.setY(self.scene().sceneRect().height() - self.rect().height())