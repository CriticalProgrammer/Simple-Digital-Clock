import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QVBoxLayout
from PyQt5.QtCore import QTimer, Qt, QDateTime


class Clock(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Critical Programmer Digital Clock")
        self.setMinimumSize(450, 150)

        # Initialize the clock UI elements
        self.time_lcd = QLCDNumber()
        self.time_lcd.setSegmentStyle(QLCDNumber.Flat)
        self.time_lcd.setDigitCount(8)
        self.time_lcd.display(QDateTime.currentDateTime().toString("hh:mm:ss"))

        # Set up a layout to arrange the UI elements vertically
        layout = QVBoxLayout()
        layout.addWidget(self.time_lcd)

        self.setLayout(layout)

        # Set up a timer to update the clock display every second
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

    def update_time(self):
        self.time_lcd.display(QDateTime.currentDateTime().toString("hh:mm:ss"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = Clock()
    clock.show()
    sys.exit(app.exec_())
