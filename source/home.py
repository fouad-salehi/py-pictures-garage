from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton,
    QLabel, QFileDialog, QFrame
)
from theme import GRAY_500, GRAY_900


class HomePage(QWidget):
    def __init__(self):
        super().__init__()

        outer = QVBoxLayout(self)
        outer.setContentsMargins(40, 40, 40, 40)
        outer.setSpacing(0)

        card = QFrame()
        card.setObjectName("card")
        card.setStyleSheet("""
            QFrame#card {
                background-color: white;
                border: 1px solid #e5e7eb;
                border-radius: 8px;
            }
        """)
        outer.addWidget(card)

        layout = QVBoxLayout(card)
        layout.setContentsMargins(48, 48, 48, 48)
        layout.setSpacing(16)
        layout.setAlignment(Qt.AlignCenter)

        brand = QLabel("PyPicturesGarage")
        brand.setAlignment(Qt.AlignCenter)
        brand.setStyleSheet(f"""
            font-size: 28px;
            font-weight: 600;
            color: {GRAY_900};
            letter-spacing: -0.01em;
        """)

        subtitle = QLabel("Turn your photos into art")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet(f"font-size: 14px; color: {GRAY_500};")

        btn_load = QPushButton("Select Image")
        btn_load.setObjectName("primary")
        btn_load.setFixedSize(220, 40)
        btn_load.setCursor(Qt.PointingHandCursor)
        btn_load.clicked.connect(self.choose_image)

        hint = QLabel("PNG, JPG or BMP  ·  up to 20 MB")
        hint.setAlignment(Qt.AlignCenter)
        hint.setStyleSheet(f"font-size: 12px; color: {GRAY_500};")

        layout.addWidget(brand)
        layout.addWidget(subtitle)
        layout.addSpacing(16)
        layout.addWidget(btn_load, alignment=Qt.AlignCenter)
        layout.addSpacing(8)
        layout.addWidget(hint)

        self.selected_path = None
        self.on_image_selected = None

    def choose_image(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Select Image", "",
            "Images (*.png *.jpg *.jpeg *.bmp)"
        )
        if path:
            self.selected_path = path
            if self.on_image_selected:
                self.on_image_selected(path)
