
from PyQt6.QtCore import QLineF
from PyQt6.QtWidgets import QGraphicsLineItem

class ConnectionLine(QGraphicsLineItem):
    def __init__(self, start_item, next_point):
      super().__init__()
      self.start = start_item
      self.end = None

      self.offset = start_item.rect().center()
      self.start_point = start_item.scenePos() + self.offset
      self.next_point_center = next_point + self.offset

      self._line = QLineF(self.start_point, next_point)
      self.setLine(self._line)
      self.setZValue(-1)
      

    def controlPoints(self):
      return self.start_point, self.end

    def setP2(self, next_point):
      self._line.setP2(next_point)
      self.setLine(self._line)

    def setStart(self, start_point):
      self.start = start_point
      self.updateLine()

    def setEnd(self, end):
      self.end = end
      self.updateLine(end)

    def updateLine(self, source):
      if source == self.start:
          self._line.setP1(source.scenePos() + self.offset)
      else:
          self._line.setP2(source.scenePos()  + self.offset)
      self.setLine(self._line)