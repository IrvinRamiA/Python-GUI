import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


def main():
    app = QApplication(sys.argv)
    widget = QWidget()

    # Create label
    label = QLabel(widget)
    label.setText("Hello World")
    label.move(75, 75)

    # Title for widget
    widget.setWindowTitle("PyQt5")

    widget.resize(400, 150)
    widget.move(250, 250)

    widget.show()

    # Wait to exit
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
