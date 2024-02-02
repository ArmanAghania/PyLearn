import sys
import cv2
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        my_btn = QPushButton("Click me", self)
        my_btn.setText("Click me")

        self.layout.addWidget(my_btn)

        self.my_label = QLabel()
        self.layout.addWidget(self.my_label)

        image = cv2.imread("The-One-Piece-Movies-In-Order-1-1140x641.jpg")
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image_qt = QImage(
            image, image.shape[1], image.shape[0], QImage.Format.Format_RGB888)
        self.my_label.setPixmap(QPixmap.fromImage(image_qt))

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication()

    window = MyWindow()
    window.show()

    app.exec()
