GRAY_50 = "#f9fafb"
GRAY_100 = "#f3f4f6"
GRAY_200 = "#e5e7eb"
GRAY_300 = "#d1d5db"
GRAY_400 = "#9ca3af"
GRAY_500 = "#6b7280"
GRAY_600 = "#4b5563"
GRAY_700 = "#374151"
GRAY_800 = "#1f2937"
GRAY_900 = "#111827"

BLUE_50 = "#eff6ff"
BLUE_200 = "#bfdbfe"
BLUE_500 = "#3b82f6"
BLUE_600 = "#2563eb"
BLUE_700 = "#1d4ed8"

GREEN_50 = "#ecfdf5"
GREEN_200 = "#a7f3d0"
GREEN_600 = "#059669"
GREEN_700 = "#047857"

RED_50 = "#fef2f2"
RED_300 = "#fca5a5"
RED_600 = "#dc2626"
RED_700 = "#b91c1c"

AMBER_50 = "#fffbeb"
AMBER_300 = "#fcd34d"
AMBER_800 = "#92400e"

FONT_SANS = '"Segoe UI", "Vazirmatn", system-ui, sans-serif'
FONT_MONO = '"Cascadia Code", "SF Mono", Consolas, monospace'


APP_STYLE = f"""
QMainWindow {{
    background-color: {GRAY_50};
}}

QWidget {{
    background-color: {GRAY_50};
    color: {GRAY_800};
    font-family: {FONT_SANS};
    font-size: 14px;
}}

QLabel {{
    background: transparent;
}}

QPushButton {{
    background-color: white;
    color: {GRAY_700};
    border: 1px solid {GRAY_300};
    border-radius: 5px;
    padding: 8px 16px;
    font-size: 13px;
    font-weight: 500;
}}

QPushButton:hover {{
    background-color: {GRAY_50};
    border-color: {GRAY_400};
}}

QPushButton:pressed {{
    background-color: {GRAY_100};
}}

QPushButton:disabled {{
    color: {GRAY_400};
    border-color: {GRAY_200};
}}

QPushButton#primary {{
    background-color: {BLUE_600};
    color: white;
    border: 1px solid {BLUE_600};
}}

QPushButton#primary:hover {{
    background-color: {BLUE_700};
    border-color: {BLUE_700};
}}

QPushButton#success {{
    background-color: {GREEN_600};
    color: white;
    border: 1px solid {GREEN_600};
}}

QPushButton#success:hover {{
    background-color: {GREEN_700};
    border-color: {GREEN_700};
}}

QPushButton#danger {{
    background-color: white;
    color: {RED_600};
    border: 1px solid {RED_300};
}}

QPushButton#danger:hover {{
    background-color: {RED_50};
}}

QPushButton#effect {{
    background-color: white;
    color: {GRAY_700};
    border: 1px solid {GRAY_200};
    border-radius: 6px;
    padding: 10px 14px;
    font-size: 13px;
}}

QPushButton#effect:hover {{
    border-color: {BLUE_500};
    color: {BLUE_700};
    background-color: {BLUE_50};
}}

QPushButton#effect:checked {{
    border-color: {BLUE_600};
    color: {BLUE_700};
    background-color: {BLUE_50};
}}

QLineEdit, QComboBox, QSpinBox, QDateEdit {{
    background-color: white;
    color: {GRAY_900};
    border: 1px solid {GRAY_300};
    border-radius: 5px;
    padding: 0 10px;
    min-height: 36px;
    font-size: 13px;
}}

QLineEdit:focus, QComboBox:focus, QSpinBox:focus, QDateEdit:focus {{
    border-color: {BLUE_500};
}}

QLineEdit::placeholder {{
    color: {GRAY_400};
}}

QComboBox::drop-down {{
    border: none;
    width: 24px;
}}

QComboBox QAbstractItemView {{
    background-color: white;
    border: 1px solid {GRAY_200};
    selection-background-color: {BLUE_50};
    selection-color: {BLUE_700};
    padding: 4px;
}}

QScrollArea {{
    border: none;
    background-color: transparent;
}}

QScrollBar:vertical {{
    background: transparent;
    width: 10px;
    margin: 0;
}}

QScrollBar::handle:vertical {{
    background: {GRAY_300};
    border-radius: 5px;
    min-height: 30px;
}}

QScrollBar::handle:vertical:hover {{
    background: {GRAY_400};
}}

QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical,
QScrollBar::add-page:vertical,
QScrollBar::sub-page:vertical {{
    background: none;
    height: 0;
}}

QScrollBar:horizontal {{
    background: transparent;
    height: 8px;
    margin: 0;
}}

QScrollBar::handle:horizontal {{
    background: {GRAY_300};
    border-radius: 4px;
    min-width: 30px;
}}

QScrollBar::handle:horizontal:hover {{
    background: {GRAY_400};
}}

QScrollBar::add-line:horizontal,
QScrollBar::sub-line:horizontal,
QScrollBar::add-page:horizontal,
QScrollBar::sub-page:horizontal {{
    background: none;
    width: 0;
}}

QMessageBox {{
    background-color: white;
}}

QMessageBox QLabel {{
    color: {GRAY_700};
    font-size: 14px;
}}
"""
