from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog
from PySide6.QtGui import QPixmap
import sys


class ImageEncryptorDecryptor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Encryptor/Decryptor")
        self.layout = QVBoxLayout()

        self.loadImageButton = QPushButton("Load Image")
        self.loadImageButton.clicked.connect(self.loadImage)
        self.layout.addWidget(self.loadImageButton)

        self.encryptButton = QPushButton("Encrypt Image")
        self.encryptButton.clicked.connect(self.encryptImage)
        self.layout.addWidget(self.encryptButton)

        self.decryptButton = QPushButton("Decrypt Image")
        self.decryptButton.clicked.connect(self.decryptImage)
        self.layout.addWidget(self.decryptButton)

        self.imageLabel = QLabel()
        self.layout.addWidget(self.imageLabel)

        self.setLayout(self.layout)

    def loadImage(self):
        fileName, _ = QFileDialog.getOpenFileName(
            self, "Open Image", "", "Image Files (*.png *.jpg *.bmp)")
        if fileName:
            self.imagePath = fileName
            pixmap = QPixmap(fileName)
            self.imageLabel.setPixmap(pixmap)
            self.imageLabel.adjustSize()

    def encryptImage(self):
        from encryptor import encrypt_image
        encrypt_image(self.imagePath)
        self.imageLabel.setPixmap(QPixmap('encrypted_image.bmp'))
        self.imageLabel.adjustSize()

    def decryptImage(self):
        from decryptor import decrypt_image
        decrypt_image('encrypted_image.bmp', 'secret_key.npy')
        self.imageLabel.setPixmap(QPixmap('decrypted_image.jpg'))
        self.imageLabel.adjustSize()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageEncryptorDecryptor()
    window.show()
    sys.exit(app.exec())
