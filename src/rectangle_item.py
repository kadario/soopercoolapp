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


  #EVENTS:

  def itemChange(self, change , value):
    if change == QGraphicsItem.GraphicsItemChange.ItemPositionChange and self.scene():
      self.move_line_to_center()
      
      newPos = value
      rectScene = self.scene().sceneRect()

      if not rectScene.contains(newPos) :
        #Keep the item inside the scene rect.
        newPos.setX(min(rectScene.right(), max(newPos.x(), rectScene.left())))
        newPos.setY(min(rectScene.bottom(), max(newPos.y(), rectScene.top())))
        
        return newPos

    return super(RectangleItem, self).itemChange(change, value)
  
  def mouseMoveEvent(self, event):
    super().mouseMoveEvent(event)
    
    colliding = self.collidingItems()

    if len(colliding) > 0:
      self.check_collisions(event)

  def mousePressEvent(self, event: QGraphicsSceneMouseEvent | None) -> None:
    self.setZValue(1)

    if event.button() == Qt.MouseButton.RightButton:
      if self.line == None:
        self.set_connection_state()
      else:
        self.scene().removeItem(self.line)
        self.line = None
      
    return super().mousePressEvent(event)
  
  def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent | None) -> None:
    colliding = self.collidingItems()

    if len(colliding) > 0:
      self.check_collisions(event)
    
    super().mouseReleaseEvent(event)


  #CUSTOM METHODS:

  def closest(self, pos, i, j):
    return i if QLineF(pos, i).length() < QLineF(pos, j).length() else j

  def tangentPositions(self, item_A, item_B):
    radius = self.rect().width() / 2
    
    radius_A = radius + item_A.rect().width() / 2
    radius_B = radius + item_B.rect().width() / 2
    
    position_A = item_A.pos(); 
    position_B = item_B.pos()
    
    diameter = QLineF(position_A, position_B).length()
    
    chord_distance = (radius_A ** 2 - radius_B ** 2 + diameter ** 2) / (2 * diameter)
    half_chord = abs(radius_A ** 2 - chord_distance ** 2) ** 0.5 *(-1*(chord_distance > radius_A) | 1)
    
    mid = position_A + chord_distance * (position_B - position_A) / diameter
    
    dx = half_chord * (position_B - position_A).y() / diameter
    dy = half_chord * (position_B - position_A).x() / diameter
    
    return mid + QPointF(dx, -dy), mid + QPointF(-dx, dy)

  def add_line(self, line, ispoint):
    self.line = line
    self.isPoint = ispoint
  
  # Change state of the selected block while connection with another my lines
  def set_connection_state(self):
    if self.connection_status == False:
      self.connection_status = True
      self.setCursor(Qt.CursorShape.ArrowCursor) 
      self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, False)
      self.setOpacity(0.5)
      self.parent.hello_new_line(self)

    else:
      self.connection_status = False
      self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, True)
      self.setCursor(Qt.CursorShape.OpenHandCursor) 
      self.setOpacity(1)

  # Redraw line connected to block when block position updated
  def move_line_to_center(self):
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
          
          # Get coordinates of center of two blocks
          selfCenterX = self.pos().x() + self.rect().width() / 2
          selfCenterY = self.pos().y() + self.rect().height() / 2
          collideCenterX = collider.pos().x() + collider.rect().width() / 2
          colliderCenterY = collider.pos().y() + collider.rect().height() / 2
          
          # creating line between two centers to check cosinus
          line_central_position_1 = QPointF(collideCenterX, colliderCenterY)
          line_central_position_2 = QPointF(selfCenterX, selfCenterY)

          line = QLineF(line_central_position_1, line_central_position_2)

          # get Cosinus
          cosinus = (collider.rect().width()/2 / line.length()) if line.length() > 0 else 0
          
          # Check cosinus value to know which side our block closer to
          # And put our block to
          if cosinus > 0.4 and cosinus < 0.7 :
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