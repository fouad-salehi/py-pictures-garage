import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget

from splash import Splash
from home import HomePage
from editor import EditorPage
from theme import APP_STYLE


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyPicturesGarage")
        self.resize(900, 640)
        self.setStyleSheet(APP_STYLE)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.home = HomePage()
        self.editor = EditorPage()

        self.stack.addWidget(self.home)
        self.stack.addWidget(self.editor)

        self.home.on_image_selected = self.open_editor
        self.editor.on_back = lambda: self.stack.setCurrentIndex(0)
        self.stack.setCurrentIndex(0)

    def open_editor(self, path):
        self.editor.load_image(path)
        self.stack.setCurrentIndex(1)


def main():
    app = QApplication(sys.argv)
    splash = Splash()
    splash.show()

    window = MainWindow()

    def finish():
        window.show()
        splash.finish(window)

    QTimer.singleShot(2000, finish)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()