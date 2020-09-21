import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

COLS = ROWS = 60


class myLabel(QLabel):
    postionClick = pyqtSignal(int, int)

    def __init__(self, x, y, objName=None, parent=None):
        QLabel.__init__(self, parent)
        self.setText(" ")
        self.setStyleSheet("border: 1px solid black;")
        self.x = x
        self.y = y
        self.setMouseTracking(True)
        if objName is not None:
            self.setObjectName(objName)

    def mouseMoveEvent(self, QMouseEvent):
        self.postionClick.emit(self.x, self.y)


class myGrid(QWidget):

    def __init__(self, flags=None, *args, **kwargs):
        super().__init__(flags, *args, **kwargs)
        self.grid = [[myLabel(j, i, str(i) + str(j)) for i in range(ROWS)] for j in range(COLS)]
        self.initGrid()

    def initGrid(self):
        gridLayout = QGridLayout()
        gridLayout.setSpacing(0)

        for i in range(ROWS):
            for j in range(COLS):
                self.grid[i][j].postionClick.connect(self.labelClicked)
                gridLayout.addWidget(self.grid[i][j], i, j)

        self.setLayout(gridLayout)
        self.setGeometry(0, 0, 1366, 768)
        self.show()

    def labelClicked(self, x, y):
        if 0 <= x < ROWS and 0 <= y < COLS:
            self.grid[x][y].setStyleSheet("background-color:#ff0000;")



def main():
    app = QApplication(sys.argv)
    gd = myGrid()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
