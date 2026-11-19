from PyQt5.QtCore import Qt, QRect, pyqtSignal, QPoint
from PyQt5.QtGui import QPainter, QPen, QColor, QPixmap
from PyQt5.QtWidgets import QLabel
from theme import BLUE_500, GRAY_500


class CropLabel(QLabel):
    crop_finished = pyqtSignal(QRect)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAlignment(Qt.AlignCenter)
        self.setMinimumSize(640, 380)
        self.setMouseTracking(True)
        self._full_pixmap = None
        self.start_point = None
        self.end_point = None
        self.selecting = False

    def set_full_pixmap(self, pixmap):
        self._full_pixmap = pixmap
        self.start_point = None
        self.end_point = None
        self.update()

    def clear(self):
        self._full_pixmap = None
        self.start_point = None
        self.end_point = None
        self.update()

    def _display_rect(self):
        if self._full_pixmap is None or self._full_pixmap.isNull():
            return QRect()
        pw = self._full_pixmap.width()
        ph = self._full_pixmap.height()
        lw = self.width()
        lh = self.height()
        scale = min(lw / pw, lh / ph)
        dw = int(pw * scale)
        dh = int(ph * scale)
        x = (lw - dw) // 2
        y = (lh - dh) // 2
        return QRect(x, y, dw, dh)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self._full_pixmap is not None:
            if self._display_rect().contains(event.pos()):
                self.start_point = event.pos()
                self.end_point = event.pos()
                self.selecting = True
                self.update()

    def mouseMoveEvent(self, event):
        if self.selecting:
            self.end_point = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.selecting:
            self.selecting = False
            self.end_point = event.pos()
            disp = self._display_rect()
            x1 = max(min(self.start_point.x(), self.end_point.x()), disp.left())
            y1 = max(min(self.start_point.y(), self.end_point.y()), disp.top())
            x2 = min(max(self.start_point.x(), self.end_point.x()), disp.right())
            y2 = min(max(self.start_point.y(), self.end_point.y()), disp.bottom())
            if x2 - x1 > 5 and y2 - y1 > 5:
                self.crop_finished.emit(QRect(x1, y1, x2 - x1, y2 - y1))
            self.start_point = None
            self.end_point = None
            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor("#f9fafb"))

        if self._full_pixmap is None or self._full_pixmap.isNull():
            painter.setPen(QColor(GRAY_500))
            painter.drawText(self.rect(), Qt.AlignCenter, "No image loaded")
            painter.end()
            return

        disp = self._display_rect()
        scaled = self._full_pixmap.scaled(
            disp.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
        )
        painter.drawPixmap(disp.topLeft(), scaled)

        if self.start_point and self.end_point:
            pen = QPen(QColor(BLUE_500), 2, Qt.DashLine)
            painter.setPen(pen)
            rect = QRect(self.start_point, self.end_point).normalized()
            painter.drawRect(rect)

        painter.end()
