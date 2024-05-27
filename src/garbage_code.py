"""
This file is to collect all unusable parts of the code.
Probably, it will be needed someday (No)
"""
import sys
import random

from PyQt6.QtCore import QSize, Qt, QEvent, QRectF, QPointF, QPoint, QSizeF
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
    QLabel
  )


# self.setFixedSize(QSize(800, 500))
#     self.setMaximumSize(QSize(1200, 800))
    
#     button = QPushButton("Press Me!")

#     centralize button on window
#     self.setCentralWidget(button)

#Widget

class SomeWidget(QWidget):
  def __init__(self, parent):
    super().__init__(parent)

    self.centralWidget = QLabel("sdasdas")
    layout = QVBoxLayout()
    layout.addWidget(self.centralWidget)
    self.setLayout(layout)

#Window

# self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    # self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    # self.setMinimumSize(QSize(400, 300))
    # self.setWindowIcon(QIcon("assets/icon.png"))

  # def paintEvent(self, event):
  #   width = self.frameGeometry().width()
    # height = self.frameGeometry().height()

    # pen = QPen()
    # pen.setWidth(1)
    # pen.setColor(QColor('red'))

    # some_painter = QPainter(self)
    # some_painter.setPen(pen)
    # some_painter.drawRect(10, 10, width - 20, height - 60)
    # some_painter.drawRect(10, 10, 10, 10)

  #   scene = QGraphicsScene(0, 0, 400, 200)
  #   rect = QGraphicsRectItem(0, 0, 200, 50)
  #   rect.setPos(50, 20)
  #   brush = QBrush(Qt.GlobalColor.red)
  #   rect.setBrush(brush)

  #   # Define the pen (line)
  #   pen = QPen(Qt.GlobalColor.cyan)
  #   pen.setWidth(10)
  #   rect.setPen(pen)

  #   scene.addItem(rect)

  # def mousePressEvent(self, event):
  #   print("Mouse pressed!")
  #   super().mousePressEvent(event)


  # def clickEvent(self, event):
  #   print("click!")


#DrawArea


    # super().__init__()

    # parentWidth = parent.frameGeometry().width()
    # parentHeight = parent.frameGeometry().height()
    
    # self.setGeometry(0, 0, parentWidth, parentHeight)
    

    # self.columns = 14 # num of columns in grid
    # self.rows = 49 # num of rows in grid

    # grid = QGridLayout(self)

    

    
    

    # self.scene = QGraphicsScene(self)
    # self.item = QGraphicsRectItem(300,400,100,100)
    # self.scene.addItem(self.item)
    # self.setScene(self.scene)


    # side = 10
    # rect = QRectF(0, 0, side, side)
    # rect = QGraphicsRectItem(0, 0, 50, 50)
    # rect.setPos(50, 20)
    # brush = QBrush(Qt.GlobalColor.red)
    # rect.setBrush(brush)

    # # Define the pen (line)
    # pen = QPen(Qt.GlobalColor.cyan)
    # pen.setWidth(10)
    # rect.setPen(pen)

    # scene.addItem(rect)
  
  # def paintEvent(self, event):
  #   print("paint event")
    
    # parentWidth = self.getParent.frameGeometry().width()
    # parentHeight = self.getParent.frameGeometry().height()

    # self.setGeometry(0, 0, parentWidth, parentHeight)

    # parentWidth = self.parent.frameGeometry().width()
    # parentHeight = self.parent.frameGeometry().height()
    # self.setGeometry(0, 0, parentWidth, parentHeight)
  
  # def resizeEvent(self, event):
  #   print("resize event")


  # def sceneEvent(self, event: QEvent | None) -> bool:
    # print(self.collidingItems())
    # print("parent", self.parent)
    # return super().sceneEvent(event)

# class CurvePaint(QGraphicsItem):
#   def __init__(self, parent=None):
#     super(CurvePaint, self).__init__(parent)
    # self.x = x
    # self.y = y
    # self.polygon = QPolygonF([
    #     QPointF(self.x-10, self.y-10), QPointF(self.x-10, self.y+10),
    #     QPointF(self.x+10, self.y+10), QPointF(self.x+10, self.y-10),
    #     ])
    # self._painter = QPainter()
    
  
  # def paint(self, painter, option, widget):
  #   print("items", self.scene().itemsBoundingRect())
  #   painter = QPainter(self)
  #   path = QPainterPath()
    
  #   points = [
  #         QPointF(20,40),
  #         QPointF(60,10),
  #         QPointF(100,50),
  #         QPointF(80,200),
  #         QPointF(200,300),
  #         QPointF(150,400),
  #         QPointF(350,450),
  #         QPointF(400,350),
  #         ]

  #   painter.setPen(Qt.GlobalColor.red)
  #   painter.setBrush(QBrush(Qt.GlobalColor.red))

  #   for i in range(len(points)):
  #         painter.drawEllipse(points[i], 3, 3)
    
  #   painter.setPen(Qt.GlobalColor.red)
  #   painter.setBrush(QBrush(Qt.GlobalColor.red, Qt.BrushStyle.NoBrush)) #reset the brush
  #   path.moveTo(points[0])

  #   for i in range(0,len(points),2):
  #     path.quadTo(points[i], points[i+1])

  #   painter.drawPath(path)





# class BlocksConnection(QPainterPath):
#   def __init__(self, x1, y1, x2, y2):
#     super().__init__()

#     middle_x = x1 - x2 if x1 > x2 else x2 - x1
#     middle_y = y1 - y2 if y1 > y2 else y2 - y1

#     self.moveTo(x1, y1)
#     self.quadTo(middle_x, middle_y, x2, y2)
    # for i in range(0,len(points), 2):
    #   self.quadTo(points[i], points[i+1])


#DrawArea move

  # def mouseMoveEvent(self, event):
  #   if len(self.points) == 2:
  #     self.scene().addPath(BlocksConnection(self.points[0], self.points[1], event.pos().x(), event.pos().y()))

  #   print("position", event.pos())
  
  # def mousePressEvent(self, event: QGraphicsSceneMouseEvent | None) -> None:
  #   if len(self.points) < 4:
  #     self.points.append(event.pos().x())
  #     self.points.append(event.pos().y())
    
  #   if len(self.points) == 4:
  #     self.scene().addPath(BlocksConnection(self.points[0], self.points[1], self.points[2], self.points[3]))

  #     self.points = []
    
  #   print("points", self.points)
    
  #   super().mousePressEvent(event)


import sys
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *


class Arrow(QGraphicsItem):

    def __init__(self, startItem, endItem, parent=None, scene=None):
        super().__init__(parent, scene)

        self.startItem = startItem
        self.endItem = endItem

    def boundingRect(self):
        p1 = self.startItem.pos() + self.startItem.rect().center()
        p3 = self.endItem.pos() + self.endItem.rect().center()
        bounds = p3 - p1
        size = QSizeF(abs(bounds.x()), abs(bounds.y()))
        return QRectF(p1, size)

    def paint(self, painter, option, widget=None):

        p1 = self.startItem.pos() + self.startItem.rect().center()
        p3 = self.endItem.pos() + self.endItem.rect().center()

        pen = QPen()
        pen.setWidth(1)
        painter.setRenderHint(QPainter.Antialiasing)

        if self.isSelected():
            pen.setStyle(Qt.DashLine)
        else:
            pen.setStyle(Qt.SolidLine)

        pen.setColor(Qt.black)
        painter.setPen(pen)
        painter.drawLine(QLineF(p1, p3))
        painter.setBrush(Qt.NoBrush)

    def updatePosition(self):
        print("update")
        #Not sure what to do here...


class TextBox(QGraphicsRectItem):
    def __init__(self, text, position, rect=QRectF(0, 0, 200, 100), parent=None, scene=None):
        super().__init__(rect, parent, scene)

        self.setFlags(QGraphicsItem.ItemIsFocusable |
                      QGraphicsItem.ItemIsMovable |
                      QGraphicsItem.ItemIsSelectable)

        self.text = QGraphicsTextItem(text, self)  

        self.setPos(position)

        self.arrows = []

    def paint(self, painter, option, widget=None):
        painter.setPen(Qt.black)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(Qt.white)
        painter.drawRect(self.rect())

    def addArrow(self, arrow):
        self.arrows.append(arrow)

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionChange:
            for arrow in self.arrows:
                arrow.updatePosition()

        return value


class MainWindow(QMainWindow):
  def __init__(self, parent=None):
    super(MainWindow, self).__init__(parent)

    self.setWindowTitle("Supercool app!")
    self.setFixedSize(QSize(800, 500))

    layout = QVBoxLayout()
    layout.setContentsMargins(0, 0, 0, 0)
    layout.addWidget(DrawArea(self))
    
    widget = QWidget()
    widget.setLayout(layout)

    self.setCentralWidget(widget)

class RectangleItem(QGraphicsRectItem):
    def __init__(self, x, y, width, height, parent):
        super().__init__(x, y, width, height)

        self.parent = parent

        self.x = x
        self.y = y
        
        brush = QBrush(QColor(*[random.randint(0, 255) for _ in range(3)]))

        self.setBrush(brush)
        self.setAcceptDrops(True)
        self.setAcceptHoverEvents(True)
        self.setCursor(Qt.CursorShape.OpenHandCursor) 
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsFocusable)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemSendsGeometryChanges)

    def paint(self, painter: QPainter | None, option: QStyleOptionGraphicsItem | None, widget: QWidget | None = ...) -> None:
        return super().paint(painter, option, widget)

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent | None) -> None:
        self.setZValue(1)
        
        if event.button() == Qt.MouseButton.LeftButton:
            self.prev_pos = self.pos()

        if event.button() == Qt.MouseButton.RightButton:
            self.connection_start = self.pos()

        if self.opacity() == 1:
            self.setCursor(Qt.CursorShape.ArrowCursor) 
            self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, False)
            self.setOpacity(0.5)
        else:
            self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, True)
            self.setCursor(Qt.CursorShape.OpenHandCursor) 
            self.setOpacity(1)
    
        return super().mousePressEvent(event)

    def checkCollisions(self, event: QGraphicsSceneMouseEvent | None):
        self.setZValue(0)

        collisions = self.collidingItems()

        if len(collisions) > 0:
            for collision in range(len(collisions)):
                if collisions[collision].UserType == 65536:
                    new_position = self.mapToScene(collisions[collision].pos())
                    differ_x_axis = self.sceneBoundingRect().x() - collisions[collision].sceneBoundingRect().x()
                    differ_y_axis = self.sceneBoundingRect().y() - collisions[collision].sceneBoundingRect().y()
                    
                    half_width_collision = collisions[collision].sceneBoundingRect().x() + 25
                    
                    half_height_collision_top = collisions[collision].sceneBoundingRect().y()
                    half_height_collision_bottom = collisions[collision].sceneBoundingRect().y() + 20

                    position_to_left = new_position.x() + 51 - differ_x_axis
                    position_to_right = new_position.x() - 51 - differ_x_axis
                    position_to_top = new_position.y() + 31 - differ_y_axis
                    position_to_bottom = new_position.y() - 31 - differ_y_axis

                    if self.sceneBoundingRect().x() > half_width_collision:
                        self.setPos(QPointF(position_to_left, new_position.y()))
                    else:
                        self.setPos(QPointF(position_to_right, new_position.y()))

                    if self.sceneBoundingRect().y() < half_height_collision_top:
                        self.setPos(QPointF(new_position.x(), position_to_bottom))
                    elif self.sceneBoundingRect().y() > half_height_collision_bottom:
                        self.setPos(QPointF(new_position.x(), position_to_top))

    def mouseMoveEvent(self, event: QGraphicsSceneMouseEvent | None) -> None:
        return super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent | None) -> None:
        self.checkCollisions(self)
        return super().mouseReleaseEvent(event)
    
    def keyPressEvent(self, event: QKeyEvent | None) -> None:
        if event.key() == Qt.Key.Key_Escape:
            if self.opacity() == 0.5:
                self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, True)
                self.setCursor(Qt.CursorShape.OpenHandCursor)
                self.setOpacity(1)
        
        return super().keyPressEvent(event)


class DrawArea(QGraphicsView):
    def __init__(self, parent):
        super(DrawArea, self).__init__(parent)

        scene = QGraphicsScene()
        scene.setSceneRect(0, 0, 798, 498)
        scene.setBackgroundBrush(QColor(185, 222, 126))

        self.points = []
        self.setScene(scene)

    def mouseDoubleClickEvent(self, event: QMouseEvent | None):
        item = self.itemAt(event.pos())
        if item:
            return super().mousePressEvent(event)
        
        scene_position = self.mapToScene(event.pos())
        pos_x = scene_position.x() - 25
        pos_y = scene_position.y() - 15
        rectangle = RectangleItem(pos_x, pos_y, 50, 30, self)
        
        self.scene().addItem(rectangle)

        super().mouseDoubleClickEvent(event)

    def paintEvent(self, event: QPaintEvent | None) -> None:
        return super().paintEvent(event)

def run():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

run()



