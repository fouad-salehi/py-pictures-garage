import os
import cv2
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QLabel, QFileDialog, QMessageBox, QFrame, QScrollArea
)
from effects import EFFECTS, apply_effect
from theme import GRAY_500, GRAY_900
from crop_label import CropLabel


def cv_to_pixmap(img_bgr):
    rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    h, w, ch = rgb.shape
    bytes_per_line = ch * w
    qimg = QImage(rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)
    return QPixmap.fromImage(qimg)


class EditorPage(QWidget):
    def __init__(self):
        super().__init__()
        self.original = None
        self.result = None
        self.active_effect = None
        self.pending_crop = None

        outer = QVBoxLayout(self)
        outer.setContentsMargins(24, 20, 24, 20)
        outer.setSpacing(16)

        header = QHBoxLayout()
        title = QLabel("Editor")
        title.setStyleSheet(f"font-size: 18px; font-weight: 600; color: {GRAY_900};")
        header.addWidget(title)
        header.addStretch()
        outer.addLayout(header)

        card = QFrame()
        card.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 1px solid #e5e7eb;
                border-radius: 8px;
            }
        """)
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(16, 16, 16, 16)
        card_layout.setSpacing(12)

        self.preview = CropLabel()
        self.preview.crop_finished.connect(self.do_crop)
        card_layout.addWidget(self.preview)

        tools_label = QLabel("Tools")
        tools_label.setStyleSheet("font-size: 13px; font-weight: 500; color: #374151;")
        card_layout.addWidget(tools_label)

        tools_layout = QHBoxLayout()
        tools_layout.setSpacing(8)

        btn_rot_left = QPushButton("↺ 90° Left")
        btn_rot_left.setCursor(Qt.PointingHandCursor)
        btn_rot_left.clicked.connect(lambda: self.rotate(-90))

        btn_rot_right = QPushButton("↻ 90° Right")
        btn_rot_right.setCursor(Qt.PointingHandCursor)
        btn_rot_right.clicked.connect(lambda: self.rotate(90))

        btn_rot_180 = QPushButton("⟲ 180°")
        btn_rot_180.setCursor(Qt.PointingHandCursor)
        btn_rot_180.clicked.connect(lambda: self.rotate(180))

        btn_crop = QPushButton("✂ Crop")
        btn_crop.setCursor(Qt.PointingHandCursor)
        btn_crop.clicked.connect(self.apply_pending_crop)

        btn_reset = QPushButton("Reset")
        btn_reset.setCursor(Qt.PointingHandCursor)
        btn_reset.clicked.connect(self.reset_image)

        tools_layout.addWidget(btn_rot_left)
        tools_layout.addWidget(btn_rot_right)
        tools_layout.addWidget(btn_rot_180)
        tools_layout.addWidget(btn_crop)
        tools_layout.addStretch()
        tools_layout.addWidget(btn_reset)
        card_layout.addLayout(tools_layout)

        effects_label = QLabel("Effects")
        effects_label.setStyleSheet("font-size: 13px; font-weight: 500; color: #374151;")
        card_layout.addWidget(effects_label)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setFixedHeight(64)
        scroll.setStyleSheet("QScrollArea { border: none; background: transparent; }")

        scroll_content = QWidget()
        scroll_content.setStyleSheet("background: transparent;")
        effects_layout = QHBoxLayout(scroll_content)
        effects_layout.setContentsMargins(0, 0, 0, 0)
        effects_layout.setSpacing(8)

        for name in EFFECTS.keys():
            btn = QPushButton(name)
            btn.setObjectName("effect")
            btn.setCheckable(True)
            btn.setCursor(Qt.PointingHandCursor)
            btn.setMinimumHeight(36)
            btn.clicked.connect(lambda _, n=name, b=btn: self.apply(n, b))
            effects_layout.addWidget(btn)

        effects_layout.addStretch()
        scroll.setWidget(scroll_content)
        card_layout.addWidget(scroll)

        outer.addWidget(card, stretch=1)

        bottom = QHBoxLayout()
        btn_back = QPushButton("Back")
        btn_back.setCursor(Qt.PointingHandCursor)
        btn_back.clicked.connect(self.go_back)

        btn_save = QPushButton("Save Result")
        btn_save.setObjectName("success")
        btn_save.setCursor(Qt.PointingHandCursor)
        btn_save.clicked.connect(self.save_result)

        bottom.addWidget(btn_back)
        bottom.addStretch()
        bottom.addWidget(btn_save)
        outer.addLayout(bottom)

        self.on_back = None

    def load_image(self, path):
        img = cv2.imread(path)
        if img is None:
            QMessageBox.warning(self, "Error", "Could not open image.")
            return
        self.original = img
        self.result = img.copy()
        self.active_effect = None
        self.pending_crop = None
        self.show_image(img)

    def show_image(self, img_bgr):
        pix = cv_to_pixmap(img_bgr)
        self.preview.set_full_pixmap(pix)

    def rotate(self, angle):
        if self.result is None:
            return
        if angle == 90:
            rotated = cv2.rotate(self.result, cv2.ROTATE_90_CLOCKWISE)
        elif angle == -90:
            rotated = cv2.rotate(self.result, cv2.ROTATE_90_COUNTERCLOCKWISE)
        else:
            rotated = cv2.rotate(self.result, cv2.ROTATE_180)
        self.original = rotated.copy()
        self.result = rotated
        self.active_effect = None
        self.pending_crop = None
        self.show_image(self.result)

    def apply_pending_crop(self):
        if self.pending_crop is None:
            QMessageBox.information(
                self, "Crop", "Drag a rectangle on the image first."
            )
            return
        x, y, w, h = self.pending_crop
        self.original = self.original[y:y + h, x:x + w].copy()
        self.result = self.original.copy()
        self.pending_crop = None
        self.active_effect = None
        self.show_image(self.result)

    def do_crop(self, rect):
        if self.original is None:
            return
        disp = self.preview._display_rect()
        if disp.width() == 0 or disp.height() == 0:
            return
        img_h, img_w = self.original.shape[:2]
        scale_x = img_w / disp.width()
        scale_y = img_h / disp.height()
        x = int((rect.x() - disp.x()) * scale_x)
        y = int((rect.y() - disp.y()) * scale_y)
        w = int(rect.width() * scale_x)
        h = int(rect.height() * scale_y)
        x = max(0, min(x, img_w - 1))
        y = max(0, min(y, img_h - 1))
        w = max(1, min(w, img_w - x))
        h = max(1, min(h, img_h - y))
        self.pending_crop = (x, y, w, h)
        QMessageBox.information(
            self, "Crop", "Selection ready. Click Crop to apply."
        )

    def reset_image(self):
        if self.result is None:
            return
        self.original = self.result.copy()
        self.pending_crop = None
        self.active_effect = None
        self.show_image(self.result)

    def apply(self, effect_name, btn):
        if self.original is None:
            QMessageBox.information(self, "Info", "Load an image first.")
            btn.setChecked(False)
            return
        for other in self.findChildren(QPushButton, "effect"):
            if other is not btn:
                other.setChecked(False)
        try:
            src = self.original
            h, w = src.shape[:2]
            if max(h, w) > 1500:
                scale = 1500 / max(h, w)
                src = cv2.resize(src, (int(w * scale), int(h * scale)))
            self.result = apply_effect(src, effect_name)
            self.pending_crop = None
            self.show_image(self.result)
            self.active_effect = effect_name
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Effect failed:\n{e}")

    def save_result(self):
        if self.result is None:
            return
        os.makedirs("images", exist_ok=True)
        path, _ = QFileDialog.getSaveFileName(
            self, "Save Result", "images/pypicturesgarage_output.jpg",
            "JPEG (*.jpg);;PNG (*.png)"
        )
        if path:
            cv2.imwrite(path, self.result)
            QMessageBox.information(self, "Saved", f"Saved to:\n{path}")

    def go_back(self):
        if self.on_back:
            self.on_back()