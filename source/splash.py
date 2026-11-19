from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSplashScreen
from PyQt5.QtGui import QPixmap, QPainter, QColor, QFont
from theme import GRAY_50, GRAY_500, GRAY_900, BLUE_600


class Splash(QSplashScreen):
    def __init__(self):
        pix = QPixmap(600, 400)
        pix.fill(QColor(GRAY_50))
        painter = QPainter(pix)

        painter.setPen(QColor(BLUE_600))
        painter.setFont(QFont("Segoe UI", 36, QFont.Bold))
        painter.drawText(pix.rect(), Qt.AlignCenter, "PyPicturesGarage")

        painter.setPen(QColor(GRAY_900))
        painter.setFont(QFont("Segoe UI", 12))
        painter.drawText(
            pix.rect().adjusted(0, 150, 0, 0),
            Qt.AlignCenter,
            "Turn your photos into art"
        )

        painter.setPen(QColor(GRAY_500))
        painter.setFont(QFont("Segoe UI", 10))
        painter.drawText(
            pix.rect().adjusted(0, 320, 0, 0),
            Qt.AlignCenter,
            "Loading..."
        )

        painter.end()
        super().__init__(pix, Qt.WindowStaysOnTopHint)
