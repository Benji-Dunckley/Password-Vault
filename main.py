import sys
import webbrowser as wb
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLineEdit, QLayout, QLabel, QStackedWidget
from PySide6.QtCore import QSize, Qt, Slot, QPoint
from PySide6.QtGui import QFont, QWindow, QPainterPath, QPixmap, QColor, QPainter
import database as db
from PIL import Image as I, ImageEnhance

#with I.open('Impostor.webp', 'r') as sussy:
    #enhancer = ImageEnhance.Brightness(sussy)
    #transparent_image = enhancer.enhance(0.3)'''


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedSize(1280, 720)

        f = QFont("Helvetica")
        f.setBold(True)
        f.setPointSizeF(40)

        m = QFont("Helvetica")
        m.setItalic(True)
        m.setPointSizeF(20)

        sidebar = QLabel(self)
        sidebar.setGeometry(0, 0, 250, 720)
        sidebar.setStyleSheet('''background-color: dark grey;
                                      border-right-width: 5px;
                                      border-style: solid;
                                      border-color: rgba(0,0,0, 50%)''')

        pixmap = QPixmap('bg.png').scaled(1030, 1000, aspectMode=Qt.KeepAspectRatio)
        pixmap = db.change_opacity(pixmap, 0.2)
        self.minty = QLabel(self)
        self.minty.setPixmap(pixmap)
        self.minty.setGeometry(250, 0, 1030, 720)
        self.minty.setHidden(True)

        title = QLabel('test', self)
        title.setGeometry(0, 0, 250, 200)
        title.setAlignment(Qt.AlignLeft)
        title.move(10, 20)
        title.setFont(f)

        self.test1 = QPushButton('Test', self)
        self.test1.clicked.connect(self.btn_close_clicked)
        self.test1.setGeometry(0, 150, 125, 60)

        self.test2 = QPushButton('Test', self)
        self.test2.clicked.connect(self.btn_close2_clicked)
        self.test2.setGeometry(0, 150, 50, 50)
        self.test2.setHidden(True)

        '''btn_close = QPushButton("x", self)
        btn_close.setFont(f)
        btn_close.setStyleSheet("background-color: transparent")
        btn_close.clicked.connect(self.btn_close_clicked)
        btn_close.setGeometry(1250, 0, 30, 30)  # Set geometry (x, y, width, height)'''

    @Slot()
    def btn_close_clicked(self):
        print('Button pressed.')
        pass

    @Slot()
    def btn_close2_clicked(self):
        print('Button 2 pressed.')
        pass

stylesheet = """
    MainWindow {
        background-repeat: no-repeat; 
        background-position: center;
        background-color: grey
        
    }
"""

app = QApplication(sys.argv)
app.setStyleSheet(stylesheet)
window = MainWindow()
window.show()
app.exec()
