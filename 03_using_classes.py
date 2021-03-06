import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class MainPage(QWidget):
    def __init__(self, title=" "):
        super().__init__()  # Inherit init of QWidget
        self.title = title
        self.left = 250
        self.top = 250
        self.width = 400
        self.height = 150
        self.widget()

    def widget(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        label1 = QLabel("Hello World", self)
        label1.move(75, 75)

        self.show()


def main():
    app = QApplication(sys.argv)
    widget = MainPage(title="PyQt5")
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
