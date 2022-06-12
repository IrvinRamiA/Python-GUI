import sys
from PyQt5.QtWidgets import QApplication, QWidget


def main():
    app = QApplication(sys.argv)
    w = QWidget()

    # Title for widget
    w.setWindowTitle("PyQt5")
    
    # Left margin, top margin, width, height
    # w.setGeometry(250, 250, 200, 150)
    # or use below two lines
    w.resize(500, 300)
    w.move(250, 250)
    w.show()

    # Wait to exit
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
