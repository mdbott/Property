from PyQt4.QtCore import QSize, QDir, Qt
from PyQt4.QtGui import QTableWidget, QTableWidgetItem, QPixmap, QMainWindow, QApplication, QWidget, QVBoxLayout, QIcon
import os
import glob
import sys

THUMBNAIL_SIZE = 128
SPACING = 10
IMAGES_PER_ROW = 3


class TableWidget(QTableWidget):
    def __init__(self):
        QTableWidget.__init__(self)

        self.setIconSize(QSize(128, 128))
        self.setColumnCount(IMAGES_PER_ROW)
        self.setGridStyle(Qt.NoPen)

        # Set the default column width and hide the header
        self.verticalHeader().setDefaultSectionSize(THUMBNAIL_SIZE+SPACING)
        self.verticalHeader().hide()

        # Set the default row height and hide the header
        self.horizontalHeader().setDefaultSectionSize(THUMBNAIL_SIZE+SPACING)
        self.horizontalHeader().hide()

        # Set the table width to show all images without horizontal scrolling
        self.setMinimumWidth((THUMBNAIL_SIZE+SPACING)*IMAGES_PER_ROW+(SPACING*2))

    def addPicture(self, row, col, picturePath):
        item = QTableWidgetItem()

        # Scale the image by either height or width and then 'crop' it to the
        # desired size, this prevents distortion of the image.
        p = QPixmap(picturePath)
        if p.height() > p.width():
            p = p.scaledToWidth(THUMBNAIL_SIZE)
        else:
            p = p.scaledToHeight(THUMBNAIL_SIZE)
        p = p.copy(0, 0, THUMBNAIL_SIZE, THUMBNAIL_SIZE)
        item.setIcon(QIcon(p))

        self.setItem(row, col, item)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        centralWidget = QWidget(self)
        layout = QVBoxLayout(centralWidget)

        self.tableWidget = TableWidget()
        layout.addWidget(self.tableWidget)

        self.setCentralWidget(centralWidget)

        #picturesPath = QDesktopServices.storageLocation(QDesktopServices.PicturesLocation)
        picturesPath = "/home/max/PycharmProjects/plant-database/eden_site/media/plantimages/Q/Quercus/"
        #pictureDir = QDir(picturesPath)
        piclist = list()
        for infile in glob.glob(os.path.join(picturesPath, '*.jpg')):
            piclist.append(infile)
        #pictures = pictureDir.entryList(['*.jpg', '*.png', '*.gif'])

        rowCount = len(piclist)//IMAGES_PER_ROW
        if len(piclist) % IMAGES_PER_ROW:
            rowCount += 1
        print(piclist)
        self.tableWidget.setRowCount(rowCount)

        row = -1
        for i, picture in enumerate(piclist):
            col = i % IMAGES_PER_ROW
            if not col:
                row += 1
            self.tableWidget.addPicture(row, col, picture)

if __name__ == '__main__':
    from sys import argv, exit

    a = QApplication(argv)
    m = MainWindow()
    m.show()
    m.raise_()
    exit(a.exec_())
